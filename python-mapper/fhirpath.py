import datetime
import dateutil
import inspect
import io
import re
import decimal
import math
from urllib.parse import urlparse

import dateutil.parser

time_units = ["year", "years", "month", "months", "week", "weeks", "day", "days", "hour", "hours", "minute", "minutes", "second", "seconds", "millisecond", "milliseconds"]

class SimpleTypeInfo(object):

    def __init__(self, namespace: str, name: str, baseType: str="System.Any") -> None:
        self.namespace = namespace
        self.name = name
        self.baseType = baseType

class ClassInfoElement(object):

    def __init__(self, name: str, type_: str, isOneBased: bool=None) -> None:
        self.name = name
        self.type = type_
        self.isOneBased = isOneBased

class ClassInfo(object):

    def __init__(self, namespace: str, name: str, baseType: str, element: list[ClassInfoElement]) -> None:
        self.namespace = namespace
        self.name = name
        self.baseType = baseType
        self.element = element

class QuanitityComparable(object):
    
    def __init__(self, quantity):
        self.value = decimal.Decimal(quantity.value.value)
        self.system = quantity.system.value if quantity.system else None
        self.code = quantity.code.value if quantity.code else None
        self.unit = quantity.unit.value if quantity.unit else None

    def __lt__(self, other):
        if not self.check_unit(other):
            return False
        return self.value < other.value

    def __le__(self, other):
        if not self.check_unit(other):
            return False
        return self.value <= other.value

    def __gt__(self, other):
        if not self.check_unit(other):
            return False
        return self.value > other.value

    def __ge__(self, other):
        if not self.check_unit(other):
            return False
        return self.value >= other.value

    def __eq__(self, other):
        if not isinstance(other, QuanitityComparable):
            return False
        if self.value != other.value:
            return False
        return self.check_unit(other)

    def check_unit(self, other):
        if self.system is not None and other.system is not None and self.system != other.system:
            return False
        if self.code is not None and other.code is not None:
            return self.code == other.code
        if self.unit is not None and other.unit is not None:
            return self.unit == other.unit
        if self.unit is not None and other.code is not None:
            return False
        if other.unit is not None and self.code is not None:
            return False
        return True

class FHIRPathUtils(object):

    def __init__(self, model):
        self.model = model
        self.SystemDate = type('SystemDate', (model.date,), {})
        self.SystemDateTime = type('SystemDateTime', (model.dateTime,), {})
        self.SystemTime = type('SystemTime', (model.time,), {})
        self.SystemQuantity = type('SystemQuantity', (model.Quantity,), {})
        self.simple_type_names = {
            str: "String",
            bool: "Boolean",
            self.SystemDate: "Date",
            self.SystemDateTime: "DateTime",
            self.SystemTime: "Time",
            int: "Integer",
            decimal.Decimal: "Decimal",
            self.SystemQuantity: "Quantity"
        }

    def get(self, val, attr, strip=False):
        try:
            result = getattr(val, attr) or []
        except AttributeError:
            found = False
            result = []
            annotations = inspect.get_annotations(type(val).__init__)
            for var, var_type in annotations.items():
                if var.startswith(attr):
                    found = True
                    result = getattr(val, var, []) or []
                    if result:
                        break
            if not found and hasattr(val, "__dict__"):
                for key in val.__dict__.keys():
                    if key.endswith("_nsprefix_"):
                        prefix = getattr(val, key)
                        if prefix and attr.lower() == (prefix + key[:-10]).lower():
                            result = getattr(val, key[:-10]) or []
        if result != [] and strip:
            result = str(result).strip()
        return result if isinstance(result, list) else [result]

    def string_value(self, val):
        if isinstance(val, str):
            return val
        elif isinstance(val, self.model.string) or isinstance(val, self.model.uri):
            return val.value
        elif isinstance(val, self.model.div):
            tmp = io.StringIO()
            val.export(tmp, 0)
            return tmp.getvalue()
        elif val == []:
            return val
        else:
            raise BaseException("Unexpected type, expected string: %s" % val)

    def boolean_value(self, val):
        if isinstance(val, list):
            if len(val) > 1:
                raise BaseException("Operation not supported for lists with more than one element")
            elif len(val) == 1:
                val = val[0]
            else:
                return []
        if isinstance(val, bool):
            return val
        elif isinstance(val, self.model.boolean):
            return val.value == "true"
        else:
            return True

    def at_index(self, val, index):
        [idx] = index
        if len(val) > idx:
            return [val[idx]]
        else:
            return []

    def flatten(self, val):
        result = []
        for v in val:
            if isinstance(v, list):
                result += v
            elif v is not None:
                result.append(v)
        return result

    def single(self, val):
        if len(val) > 1:
            raise BaseException("More than one element")
        else:
            return val

    def single_value(self, val, *expected_types):
        if isinstance(val, list):
            if len(val) > 1:
                raise BaseException("Operation not supported for lists with more than one element")
            elif len(val) == 1:
                val = val[0]
            else:
                return []
        if not expected_types:
            return val
        for expected_type in expected_types:
            if isinstance(val, expected_type):
                return val
        if bool in expected_types:
            return True
        elif str in expected_types:
            return str(val)
        else:
            raise BaseException("Unexpected type: %s (expected %s)" % (val, expected_types))

    def bool_and(self, val_a, val_b):
        val_a = self.boolean_value(val_a)
        val_b = self.boolean_value(val_b)
        if val_a == [] or val_b == []:
            if val_a == False or val_b == False:
                return [False]
            else:
                return []
        else:
            return [val_a and val_b]

    def bool_or(self, val_a, val_b):
        val_a = self.boolean_value(val_a)
        val_b = self.boolean_value(val_b)
        if val_a == [] or val_b == []:
            if val_a == True or val_b == True:
                return [True]
            else:
                return []
        else:
            return [val_a or val_b]

    def bool_xor(self, val_a, val_b):
        val_a = self.boolean_value(val_a)
        val_b = self.boolean_value(val_b)
        if val_a == [] or val_b == []:
            return []
        else:
            return [val_a != val_b]

    def bool_implies(self, val_a, val_b):
        val_a = self.boolean_value(val_a)
        val_b = self.boolean_value(val_b)
        if val_a:
            return val_b if val_b == [] else [val_b]
        elif val_a == False or val_b:
            return [True]
        else:
            return []

    def bool_not(self, val):
        val = self.boolean_value(val)
        if val == []:
            return []
        else:
            return [not val]

    def union(self, val_a, val_b):
        result_dict = {}
        for val in val_a + val_b:
            value_annotation = inspect.get_annotations(type(val).__init__).get("value", "")
            if value_annotation == type(val).__name__ + "Enum" or value_annotation == type(val).__name__ + "_primitive":
                key = val.value
            else:
                key = val
            result_dict[key] = val
        return list(result_dict.values())

    def membership(self, val_a, val_b):
        val_a = self.single_value(val_a)
        if val_a == []:
            return [False]
        value_annotation = inspect.get_annotations(type(val_a).__init__).get("value", "")
        if value_annotation == type(val_a).__name__ + "Enum" or value_annotation == type(val_a).__name__ + "_primitive":
            key_a = val_a.value
        else:
            key_a = val_a
        for val in val_b:
            value_annotation = inspect.get_annotations(type(val).__init__).get("value", "")
            if value_annotation == type(val).__name__ + "Enum" or value_annotation == type(val).__name__ + "_primitive":
                key = val.value
            else:
                key = val
            if key == key_a:
                return [True]
        return [False]

    def containership(self, val_a, val_b):
        return self.membership(val_b, val_a)

    def exclude(self, val_a, val_b):
        results = []
        list_b = []
        for val in val_b:
            value_annotation = inspect.get_annotations(type(val).__init__).get("value", "")
            if value_annotation == type(val).__name__ + "Enum" or value_annotation == type(val).__name__ + "_primitive":
                key = val.value
            else:
                key = val
            list_b.append(key)
        for val in val_a:
            value_annotation = inspect.get_annotations(type(val).__init__).get("value", "")
            if value_annotation == type(val).__name__ + "Enum" or value_annotation == type(val).__name__ + "_primitive":
                key = val.value
            else:
                key = val
            if key not in list_b:
                results.append(key)
        return results

    def add(self, val_a, val_b):
        val_a = self.single_value(val_a)
        val_b = self.single_value(val_b)
        if val_a == [] or val_b == []:
            return []
        else:
            if isinstance(val_a, (str, self.model.string)) or isinstance(val_b, (str, self.model.string)):
                if isinstance(val_a, self.model.string):
                    val_a = val_a.value
                elif isinstance(val_b, self.model.string):
                    val_b = val_b.value
            return [val_a + val_b] # TODO check types and add support for quantity 

    def subtract(self, val_a, val_b):
        val_a = self.single_value(val_a)
        val_b = self.single_value(val_b)
        if val_a == [] or val_b == []:
            return []
        else:
            return [val_a - val_b] # TODO check types and add support for quantity 

    def multiply(self, val_a, val_b):
        val_a = self.single_value(val_a)
        val_b = self.single_value(val_b)
        if val_a == [] or val_b == []:
            return []
        if isinstance(val_a, self.model.decimal):
            val_a = val_a.value.value
        if isinstance(val_b, self.model.decimal):
            val_b = val_b.value.value
        if isinstance(val_a, self.model.Quantity) or isinstance(val_b, self.model.Quantity):
            v_a = val_a.value.value if isinstance(val_a, self.model.Quantity) else val_a
            v_b = val_b.value.value if isinstance(val_b, self.model.Quantity) else val_b
            unit = val_a if isinstance(val_a, self.model.Quantity) else val_b # TODO multiply units (m * m -> m2)
            return [self.model.Quantity(value=self.model.decimal(value=v_a * v_b), unit=unit.unit, code=unit.code, system=unit.system)]
        else:
            return [val_a * val_b]

    def negate(self, val_a):
        return self.multiply(val_a, [-1])

    def divide(self, val_a, val_b):
        val_a = self.single_value(val_a)
        val_b = self.single_value(val_b)
        if val_a == [] or val_b == []:
            return []
        elif val_b == 0:
            return []
        if isinstance(val_a, self.model.Quantity) or isinstance(val_b, self.model.Quantity):
            v_a = val_a.value.value if isinstance(val_a, self.model.Quantity) else val_a
            v_b = val_b.value.value if isinstance(val_b, self.model.Quantity) else val_b
            if val_b == 0:
                return []
            unit = val_a if isinstance(val_a, self.model.Quantity) else val_b # TODO divide units (g / m -> g/m)
            return [self.model.Quantity(value=self.model.decimal(value=v_a / v_b), unit=unit.unit, code=unit.code, system=unit.system)]
        else:
            return [decimal.Decimal(round(val_a / val_b, 8))]

    def div(self, val_a, val_b):
        val_a = self.single_value(val_a)
        val_b = self.single_value(val_b)
        if val_a == [] or val_b == []:
            return []
        elif val_b == 0:
            return []
        else:
            return [int(val_a / val_b)]

    def mod(self, val_a, val_b):
        val_a = self.single_value(val_a)
        val_b = self.single_value(val_b)
        if val_a == [] or val_b == []:
            return []
        elif val_b == 0:
            return []
        else:
            return [val_a % val_b]
        
    def decimal_round(self, val_a, val_b):
        val_a = self.single_value(val_a) # check type
        val_b = self.single_value(val_b) # check type
        if val_b == [] or val_b < 0:
            raise BaseException("Invalid precision %s" % val_a)
        elif val_a == []:
            return []
        else:
            return [round(val_a, val_b)]
        
    def decimal_truncate(self, val_a):
        val_a = self.single_value(val_a) # check type
        if val_a == []:
            return []
        else:
            return [int(val_a)]
        
    def decimal_sqrt(self, val_a):
        val_a = self.single_value(val_a) # check type
        if val_a == []:
            return []
        elif val_a < 0:
            return []
        else:
            return [round(decimal.Decimal(val_a).sqrt(), 8)]
        
    def decimal_abs(self, val_a):
        val_a = self.single_value(val_a) # check type
        if val_a == []:
            return []
        elif isinstance(val_a, self.model.Quantity):
            return [self.model.Quantity(value=self.model.decimal(value=abs(val_a.value.value)), unit=val_a.unit, code=val_a.code, system=val_a.system)]
        else:
            return [abs(val_a)]

    def decimal_ceiling(self, val_a):
        val_a = self.single_value(val_a) # check type
        if val_a == []:
            return []
        else:
            return [math.ceil(val_a)]

    def decimal_floor(self, val_a):
        val_a = self.single_value(val_a) # check type
        if val_a == []:
            return []
        else:
            return [math.floor(val_a)]

    def decimal_exp(self, val_a):
        val_a = self.single_value(val_a) # check type
        if val_a == []:
            return []
        else:
            if isinstance(val_a, int):
                val_a = decimal.Decimal(val_a)
            return [round(val_a.exp(), 8)]

    def decimal_ln(self, val_a):
        val_a = self.single_value(val_a) # check type
        if val_a == []:
            return []
        else:
            if isinstance(val_a, int):
                val_a = decimal.Decimal(val_a)
            return [round(val_a.ln(), 8)]

    def decimal_log(self, val_a, val_b):
        val_a = self.single_value(val_a) # check type
        val_b = self.single_value(val_b) # check type
        if val_a == [] or val_b == []:
            return []
        else:
            return [decimal.Decimal(round(math.log(val_a, val_b), 8))]

    def decimal_power(self, val_a, val_b):
        val_a = self.single_value(val_a) # check type
        val_b = self.single_value(val_b) # check type
        if val_a == [] or val_b == []:
            return []
        elif val_a < 0 and val_b > 0 and val_b < 1:
            return []
        else:
            return [decimal.Decimal(round(math.pow(val_a, val_b), 8))]

    def lower(self, val):
        val = self.single_value(val, str)
        if val == []:
            return val
        else:
            return [val.lower()]

    def upper(self, val):
        val = self.single_value(val, str)
        if val == []:
            return val
        else:
            return [val.upper()]

    def substring(self, val, start, length):
        val = self.string_value(val)
        start = self.single_value(start, int)
        length = self.single_value(length, int)
        if val == [] or start == [] or start < 0 or start >= len(val):
            return []
        elif length == []:
            return [val[start:]]
        else:
            return [val[start:(start+length)]]

    def matches(self, val, regex):
        val = self.string_value(val)
        regex = self.string_value(self.single_value(regex, str, self.model.string))
        if val == [] or regex == []:
            return []
        else:
            return [re.fullmatch(val, regex)]

    def contains(self, val, other):
        val = self.string_value(val)
        other = self.string_value(self.single_value(other, str, self.model.string))
        if val == [] or other == []:
            return []
        else:
            return [other in val]

    def startswith(self, val, other):
        val = self.string_value(val)
        other = self.string_value(self.single_value(other, str, self.model.string))
        if val == [] or other == []:
            return []
        else:
            return [val.startswith(other)]

    def endswith(self, val, other):
        val = self.string_value(val)
        other = self.string_value(self.single_value(other, str, self.model.string))
        if val == [] or other == []:
            return []
        else:
            return [val.endswith(other)]

    def indexof(self, val, other):
        val = self.string_value(val)
        other = self.string_value(self.single_value(other, str, self.model.string))
        if val == [] or other == []:
            return []
        elif val == "":
            return [0]
        elif other in val:
            return [val.index(other)]
        else:
            return [-1]

    def concat(self, val, other):
        val = self.string_value(self.single_value(val, str, self.model.string))
        other = self.string_value(self.single_value(other, str, self.model.string))
        if val == []:
            val = ""
        if other == []:
            other = ""
        return [val + other]

    def skip(self, val, count):
        count = self.single_value(count, int, self.model.integer)
        if isinstance(count, self.model.integer):
            count = count.value
        if count <= 0:
            return val
        elif count >= len(val):
            return []
        else:
            return val[count:]

    def take(self, val, count):
        count = self.single_value(count, int, self.model.integer)
        if isinstance(count, self.model.integer):
            count = count.value
        if count <= 0:
            return []
        elif count >= len(val):
            return val
        else:
            return val[:count]

    def first(self, val):
        if val == []:
            return val
        else:
            return val[:1]

    def last(self, val):
        if val == []:
            return val
        else:
            return val[-1:]

    def tail(self, val):
        if val == []:
            return val
        else:
            return val[1:]

    def children(self, val):
        result = []
        for v in val:
            value_annotation = inspect.get_annotations(type(v).__init__)
            for elem in value_annotation:
                result += self.get(v, elem)
        return result

    def descendants(self, val):
        result = []
        queue = list(val)
        next_queue = queue
        while next_queue != []:
            next_queue = []
            for v in queue:
                value_annotation = inspect.get_annotations(type(v).__init__)
                for elem in value_annotation:
                    e = self.get(v, elem)
                    result += e
                    next_queue += e
            queue = next_queue
        return result

    def repeat(self, val, proj):
        result = []
        queue = list(val)
        next_queue = queue
        while next_queue != []:
            next_queue = []
            for v in queue:
                e = proj(v)
                result += e
                next_queue += e
            queue = next_queue
        return result

    def aggregate(self, val, aggr, init):
        result = init
        for idx, v in enumerate(val):
            result = aggr([v], idx, result)
        return result

    def allTrue(self, val):
        for v in val:
            if isinstance(v, bool):
                if not v:
                    return [False]
            elif isinstance(v, self.model.boolean):
                if v.value != "true":
                    return [False]
            else:
                raise BaseException("Unexpected type, expected boolean for allTrue: %s" % val)
        return [True]

    def allFalse(self, val):
        for v in val:
            if isinstance(v, bool):
                if v:
                    return [False]
            elif isinstance(v, self.model.boolean):
                if v.value == "true":
                    return [False]
            else:
                raise BaseException("Unexpected type, expected boolean for allFalse: %s" % val)
        return [True]

    def anyTrue(self, val):
        return not self.allFalse(val)

    def anyFalse(self, val):
        return not self.allTrue(val)

    def trace(self, val, name, projection=None):
        if projection is not None:
            print(f"TRACE {name}: {projection}")
        else:
            print(f"TRACE {name}: {val}")
        return val

    def subset_of(self, val, other):
        coll1, coll2 = [], []
        for src, trg in [(val, coll1), (other, coll2)]:
            for val in src:
                value_annotation = inspect.get_annotations(type(val).__init__).get("value", "")
                if value_annotation == type(val).__name__ + "Enum" or value_annotation == type(val).__name__ + "_primitive":
                    key = val.value
                else:
                    key = val
                trg.append(key)
        return [set(coll1) <= set(coll2)]

    def superset_of(self, val, other):
        coll1, coll2 = [], []
        for src, trg in [(val, coll1), (other, coll2)]:
            for val in src:
                value_annotation = inspect.get_annotations(type(val).__init__).get("value", "")
                if value_annotation == type(val).__name__ + "Enum" or value_annotation == type(val).__name__ + "_primitive":
                    key = val.value
                else:
                    key = val
                trg.append(key)
        return [set(coll1) >= set(coll2)]

    def intersect(self, val, other):
        coll1, coll2 = [], []
        for src, trg in [(val, coll1), (other, coll2)]:
            for val in src:
                value_annotation = inspect.get_annotations(type(val).__init__).get("value", "")
                if value_annotation == type(val).__name__ + "Enum" or value_annotation == type(val).__name__ + "_primitive":
                    key = val.value
                else:
                    key = val
                trg.append(key)
        return list(set(coll1) & set(coll2)) # TODO return container of basic types?

    def distinct(self, val):
        return self.union(val, [])

    def is_distinct(self, val):
        return [len(self.distinct(val)) == len(val)]

    def _make_comparable(self, val):
        if isinstance(val, self.model.integer) or isinstance(val, int):
            type_ = "number"
            prec = 0
            if isinstance(val, self.model.integer):
                key = int(val.value)
            else:
                key = val
        elif isinstance(val, self.model.decimal) or isinstance(val, decimal.Decimal):
            type_ = "number"
            prec = 0
            if isinstance(val, self.model.decimal):
                key = decimal.Decimal(val.value)
            else:
                key = val
        elif isinstance(val, self.model.string) or isinstance(val, str):
            type_ = "string"
            prec = 0
            if isinstance(val, self.model.string):
                key = val.value
            else:
                key = val
        elif isinstance(val, self.model.dateTime) or isinstance(val, datetime.datetime):
            val = val.value if isinstance(val, self.model.dateTime) else val
            key = dateutil.parser.parse(val) if isinstance(val, str) else val
            if isinstance(val, str):
                prec = -1 * len(val.split(":"))
                if key.tzinfo:
                    prec += -1
            elif key.tzinfo:
                prec = -4
            else:
                prec = -3
            type_ = "date"
        elif isinstance(val, self.model.date) or (isinstance(val, datetime.date) and not isinstance(val, datetime.datetime)):
            key = val.value if isinstance(val, self.model.date) else val
            if isinstance(key, str):
                prec = len(key.split("-"))
                if prec == 3:
                    key = dateutil.parser.parse(key).date()
            else:
                prec = 3
            type_ = "date"
        elif isinstance(val, self.model.time) or isinstance(val, datetime.time):
            if isinstance(val, self.model.time):
                key = val.value
                prec = len(key.split(":"))
                ms = "." in key
                tz = "+" in key or "-" in key
                form = ":".join("%H:%M:%S".split(":")[:prec]) + (".%f" if ms else "") + ("%Z" if tz else "")
                key = datetime.datetime.strptime(key, form).time()
            else:
                prec = 3
                key = val
            type_ = "time"
        elif isinstance(val, self.model.Quantity):
            key = QuanitityComparable(val)
            prec = 0
            type_ = "number"
        else:
            value_annotation = inspect.get_annotations(type(val).__init__).get("value", "")
            if value_annotation == type(val).__name__ + "Enum" or value_annotation == type(val).__name__ + "_primitive":
                key = val.value
                type_ = "string"
            else:
                key = val
                type_ = "complex"
            prec = 0
        return key, prec, type_

    def compare(self, val_a, operator, val_b):
        val_a, prec_a, type_a = self._make_comparable(self.single_value(val_a))
        val_b, prec_b, type_b = self._make_comparable(self.single_value(val_b))
        if isinstance(val_a, datetime.date) and not isinstance(val_a, datetime.datetime) and isinstance(val_b, datetime.datetime):
            val_b = val_b.date()
            prec_b = 3
        if isinstance(val_b, datetime.date) and not isinstance(val_b, datetime.datetime) and isinstance(val_a, datetime.datetime):
            val_a = val_a.date()
            prec_a = 3
        if isinstance(val_b, int) and isinstance(val_a, str):
            try:
                val_a = int(val_a)
                type_a = "number"
            except:
                pass
        elif isinstance(val_a, int) and isinstance(val_b, str):
            try:
                val_b = int(val_b)
                type_b = "number"
            except:
                pass
        if val_a == [] or val_b == []:
            return []
        elif type_a != type_b:
            raise BaseException("Invalid comparison with different types")
        elif type_a == "complex" or type_b == "complex":
            raise BaseException("Cannot compare complex types")
        elif prec_a != prec_b:
            return []
        elif operator == "<=":
            return [val_a <= val_b]
        elif operator == "<":
            return [val_a < val_b]
        elif operator == ">":
            return [val_a > val_b]
        elif operator == ">=":
            return [val_a >= val_b]
        else:
            raise BaseException("Invalid compare operator")

    def _item_equal(self, v1, p1, v2, p2):
        if isinstance(v1, int) and isinstance(v2, int) or isinstance(v1, bool) and isinstance(v2, bool):
            return v1 == v2
        elif (isinstance(v1, decimal.Decimal) or isinstance(v1, int)) and (isinstance(v2, decimal.Decimal) or isinstance(v2, int)):
            return v1 == v2
        elif isinstance(v1, str) and isinstance(v2, str):
            return v1 == v2
        elif isinstance(v1, datetime.date) and isinstance(v2, datetime.date) or isinstance(v1, datetime.time) and isinstance(v2. datetime.time):
            if p1 != p2:
                return []
            return v1 == v2
        elif isinstance(v1, QuanitityComparable) and isinstance(v2, QuanitityComparable):
            # TODO conversion for decimal?
            return v1 == v2
        elif isinstance(v1, self.model.Element) and isinstance(v2, self.model.Element) and type(v1) == type(v2):
            value_annotation = inspect.get_annotations(type(v1).__init__)
            for elem in value_annotation:
                e1 = self.get(v1, elem)
                e2 = self.get(v2, elem)
                if isinstance(e1, list):
                    if len(e1) != len(e2):
                        return False
                    for idx in range(0, len(e1)):
                        ev1 = e1[idx]
                        ev2 = e2[idx]
                        if not self._item_equal(ev1, 0, ev2, 0):
                            return False
                elif not self._item_equal(e1, 0, e2, 0):
                    return False
            return True
        else:
            return False

    def equals(self, val_a, operator, val_b):
        coll1, coll2, type1 = [], [], []
        prec1, prec2, type2 = [], [], []
        for src, trg, precs, types in [(val_a, coll1, prec1, type1), (val_b, coll2, prec2, type2)]:
            for val in src:
                key, prec, type_ = self._make_comparable(val)
                trg.append(key)
                precs.append(prec)
                types.append(type_)
        pos_result = operator == "=="
        if coll1 == [] or coll2 == []:
            return []
        elif len(coll1) != len(coll2):
            return [not pos_result]
        elif operator in ["==", "!="]:
            for idx in range(0, len(coll1)):
                v1 = coll1[idx]
                v2 = coll2[idx]
                p1 = prec1[idx]
                p2 = prec2[idx]
                result = self._item_equal(v1, p1, v2, p2)
                if not result:
                    return [not pos_result] if result != [] else []
            return [pos_result]
        else:
            raise BaseException("Invalid equals operator")

    def _item_equivalent(self, v1, v2):
        if isinstance(v1, int) and isinstance(v2, int) or isinstance(v1, bool) and isinstance(v2, bool):
            if v1 == v2:
                return True
        elif (isinstance(v1, decimal.Decimal) or isinstance(v1, int)) and (isinstance(v2, decimal.Decimal) or isinstance(v2, int)):
            prec = 8
            for v in [str(v1), str(v2)]:
                prec = min(prec, len(v[v.find("."):][1:].rstrip("0")))
            if round(v1, prec) == round(v2, prec):
                return True
        elif isinstance(v1, str) and isinstance(v2, str):
            v1_ = v1.lower().replace("\t", " ").replace("\t", " ").replace("\n", " ")
            v2_ = v2.lower().replace("\t", " ").replace("\t", " ").replace("\n", " ")
            if v1_ == v2_:
                return True
        elif isinstance(v1, datetime.date) and isinstance(v2, datetime.date) or isinstance(v1, datetime.time) and isinstance(v2. datetime.time):
            if v1 == v2:
                return True
        elif isinstance(v1, QuanitityComparable) and isinstance(v2, QuanitityComparable):
            if v1 == v2:
                return True
        elif isinstance(v1, self.model.Element) and isinstance(v2, self.model.Element) and type(v1) == type(v2):
            value_annotation = inspect.get_annotations(type(v1).__init__)
            for elem in value_annotation:
                e1 = self.get(v1, elem)
                e2 = self.get(v2, elem)
                if isinstance(e1, list):
                    for ev1 in e1:
                        found = False
                        for ev2 in e2:
                            if self._item_equivalent(ev1, ev2):
                                found = True
                                e2.remove(ev2)
                                break
                        if not found:
                            return False
                elif not self._item_equivalent(e1, e2):
                    return False
            return True
        else:
            return False

    def equivalent(self, val_a, operator, val_b):
        coll1, coll2 = [], []
        for src, trg in [(val_a, coll1), (val_b, coll2)]:
            for val in src:
                trg.append(self._make_comparable(val)[0])
        pos_result = operator == "~"
        if coll1 == [] and coll2 == []:
            return [pos_result]
        elif len(coll1) != len(coll2):
            return [not pos_result]
        elif operator in ["~", "!~"]:
            for v1 in coll1:
                found = False
                for v2 in coll2:
                    if self._item_equivalent(v1, v2):
                        found = True
                        coll2.remove(v2)
                        break
                if not found:
                    return [not pos_result]
            return [pos_result]
        else:
            raise BaseException("Invalid equals operator")

    def strlength(self, val):
        return [len(self.string_value(val))]

    def toChars(self, val):
        return list(self.string_value(val))

    def toString(self, val):
        val = self.single_value(val)
        if val == []:
            return []
        elif isinstance(val, self.model.dateTime) or isinstance(val, datetime.datetime):
            if isinstance(val, self.model.dateTime):
                result = val.value
            else:
                result = val.strftime("%Y-%m-%dT%H:%M:%S.%f%Z") # +/- for TZ? %f only if needed
        elif isinstance(val, self.model.date) or isinstance(val, datetime.date):
            if isinstance(val, self.model.date):
                result = val.value
            else:
                result = val.strftime("%Y-%m-%d")
        elif isinstance(val, self.model.time) or isinstance(val, datetime.time):
            if isinstance(val, self.model.time):
                result = val.value
            else:
                result = val.strftime("%H:%M:%S.%f%Z") # +/- for TZ? %f only if needed
        elif isinstance(val, self.model.string):
            result = val.value
        elif isinstance(val, str):
            result = val
        elif isinstance(val, self.model.Quantity):
            result = str(val.value.value)
            if val.unit:
                if val.unit.value in time_units:
                    result += " '{%s}'" % val.unit.value
                else:
                    result += " '%s'" % val.unit.value
            elif val.code:
                result += " '%s'" % val.code.value
        elif isinstance(val, self.model.boolean) or isinstance(val, bool):
            result = "true" if self.boolean_value(val) else "false"
        elif isinstance(val, self.model.integer) or isinstance(val, int):
            if isinstance(val, self.model.integer):
                result = val.value
            else:
                result = str(val)
        elif isinstance(val, self.model.decimal) or isinstance(val, decimal.Decimal):
            if isinstance(val, self.model.decimal):
                result = val.value
            else:
                result = str(val)
        else:
            result = False
        return [result]

    def convertsToString(self, val):
        return [self.toString(val) != False]

    def toBoolean(self, val):
        val = self.single_value(val)
        is_true = False
        is_false = False
        if val == []:
            pass
        elif isinstance(val, bool):
            return [val]
        elif isinstance(val, self.model.boolean):
            return [val.value == "true"]
        elif isinstance(val, self.model.integer) or isinstance(val, int):
            if isinstance(val, self.model.integer):
                is_true = val.value == "1"
                is_false = val.value == "0"
            else:
                is_true = val == 1
                is_false = val == 0
        elif isinstance(val, self.model.decimal) or isinstance(val, decimal.Decimal):
            if isinstance(val, self.model.decimal):
                is_true = val.value == "1.0"
                is_false = val.value == "0.0"
            else:
                is_true = str(val) == "1.0"
                is_false = str(val) == "0.0"
        elif isinstance(val, self.model.string) or isinstance(val, str):
            val = self.string_value(val)
            is_true = val.lower() in ["true", "t", "yes", "y", "1", "1.0"]
            is_false = val.lower() in ["false", "f", "no", "n", "0", "0.0"]
        if is_true or is_false:
            return [is_true]
        else:
            return []

    def convertsToBoolean(self, val):
        if val == []:
            return []
        else:
            return [self.toBoolean(val) != []]

    def toInteger(self, val):
        val = self.single_value(val)
        if val == []:
            return []
        elif isinstance(val, int):
            return [val]
        elif isinstance(val, self.model.integer):
            return [val.value]
        elif isinstance(val, self.model.boolean) or isinstance(val, bool):
            return [1 if self.boolean_value(val) else 0]
        elif isinstance(val, self.model.string) or isinstance(val, str):
            try:
                return [int(self.string_value(val))]
            except:
                return []
        else:
            return []

    def convertsToInteger(self, val):
        if val == []:
            return []
        else:
            return [self.toInteger(val) != []]

    def toDecimal(self, val):
        val = self.single_value(val)
        if val == []:
            return val
        elif isinstance(val, decimal.Decimal):
            return [val]
        elif isinstance(val, self.model.decimal):
            return [decimal.Decimal(val.value)]
        elif isinstance(val, self.model.integer) or isinstance(val, int):
            if isinstance(val, self.model.integer):
                return [decimal.Decimal(val.value)]
            else:
                return [decimal.Decimal(val)]
        elif isinstance(val, self.model.boolean) or isinstance(val, bool):
            return [decimal.Decimal("1.0") if self.boolean_value(val) else decimal.Decimal("0.0")]
        elif isinstance(val, self.model.string) or isinstance(val, str):
            try:
                return [decimal.Decimal(self.string_value(val))]
            except:
                return []
        else:
            return []

    def convertsToDecimal(self, val):
        if val == []:
            return []
        else:
            return [self.toDecimal(val) != []]

    def toDate(self, val):
        val = self.single_value(val)
        if val == []:
            return []
        elif isinstance(val, self.model.dateTime) or isinstance(val, datetime.datetime):
            if isinstance(val, self.model.dateTime):
                result = self.model.date(value=dateutil.parser.parse(val.value).date().isoformat())
            else:
                result = self.model.date(value=val.date().isoformat())
            return [result]
        elif isinstance(val, self.model.date):
            return [val]
        elif isinstance(val, datetime.date):
            return [self.model.date(value=val.isoformat())]
        elif isinstance(val, self.model.string) or isinstance(val, str):
            try:
                return [self.model.date(value=datetime.datetime.strptime(val,"-".join("%Y-%m-%d".split("-")[:len(val.split("-"))])).date().isoformat())]
            except:
                return []
        else:
            return []

    def convertsToDate(self, val):
        if val == []:
            return []
        else:
            return [self.toDate(val) != []]

    def toDateTime(self, val):
        val = self.single_value(val)
        if val == []:
            return []
        elif isinstance(val, self.model.dateTime):
            return [val]
        elif isinstance(val, datetime.datetime):
            return [self.model.dateTime(value=val.isoformat())]
        elif isinstance(val, self.model.date) or isinstance(val, datetime.date):
            return self.model.dateTime(value=val.value if isinstance(val, self.model.date) else val.strftime("%Y-%m-%d"))
        elif isinstance(val, self.model.string) or isinstance(val, str):
            try:
                if "T" in val or not "-" in val: # support for CDA dates
                    return [self.model.dateTime(value=dateutil.parser.parse(val).isoformat())]
                else:
                    return [self.model.dateTime(value=datetime.datetime.strptime(val,"-".join("%Y-%m-%d".split("-")[:len(val.split("-"))])).isoformat())]
            except:
                return []
        else:
            return []

    def convertsToDateTime(self, val):
        if val == []:
            return []
        else:
            return [self.toDateTime(val) != []]

    def toTime(self, val):
        val = self.single_value(val)
        if val == []:
            return []
        elif isinstance(val, self.model.time):
            return [self.model.time(value=val.value)]
        elif isinstance(val, datetime.time):
            return [self.model.time(value=val.isoformat())]
        elif isinstance(val, self.model.string) or isinstance(val, str):
            ms = "." in val
            tz = "+" in val or "-" in val
            parts = len(val.split(":"))
            form = ":".join("%H:%M:%S".split(":")[:parts]) + (".%f" if ms else "") + ("%Z" if tz else "")
            try:
                return [self.model.time(value=datetime.datetime.strptime(val, form).time().isoformat())]
            except:
                return []
        else:
            return []

    def convertsToTime(self, val):
        if val == []:
            return []
        else:
            return [self.toTime(val) != []]

    def toQuantity(self, val, unit):
        val = self.single_value(val)
        if val == []:
            return val
        elif isinstance(val, self.model.Quantity):
            if unit and (val.unit and unit != val.unit.value or val.code and unit != val.code.value):
                return [] # TODO implement conversions
            else:
                return val
        elif isinstance(val, self.model.decimal) or isinstance(val, decimal.Decimal) or isinstance(val, self.model.integer) or isinstance(val, int):
            if isinstance(val, self.model.integer) or isinstance(val, self.model.decimal):
                value = val.value
            else:
                value = str(val)
            return [self.model.Quantity(value=self.model.decimal(value=value), code=self.model.string(value="1"))]
        elif isinstance(val, self.model.boolean) or isinstance(val, bool):
            value = "1.0" if self.boolean_value(val) else "0.0"
            return [self.model.Quantity(value=self.model.decimal(value=value), code=self.model.string(value="1"))]
        elif isinstance(val, self.model.string) or isinstance(val, str):
            match = re.fullmatch("(?P<value>(\\+|-)?\\d+(\\.\\d+)?)\\s*('(?P<unit>[^']+)'|(?P<time>[a-zA-Z]+))?", val)
            if match:
                try:
                    value = decimal.Decimal(self.string_value(match.groupdict()["value"]))
                except:
                    return []
                time_unit = match.groupdict().get("time", None)
                if time_unit and time_unit not in time_units:
                    return []
                unit = match.groupdict().get("unit", None)
                if time_unit:
                    return [self.model.Quantity(value=self.model.decimal(value=value), unit=self.model.string(value=time_unit))]
                else:
                    return [self.model.Quantity(value=self.model.decimal(value=value), code=self.model.string(value=(unit or "1")))]
            else:
                return []
        else:
            return []

    def convertsToQuantity(self, val, unit):
        if val == []:
            return []
        else:
            return [self.toQuantity(val, unit) != []]

    def gettype(self, val):
        if type(val) in self.simple_type_names:
            return [SimpleTypeInfo(namespace="System", name=self.simple_type_names[type(val)])]
        elif isinstance(val, list):
            pass # TODO: return type info obj
            return []
        else:
            elements = []
            value_annotation = inspect.get_annotations(type(val).__init__)
            for elem, type_ in value_annotation.items():
                if isinstance(type_, str):
                    elements.append(ClassInfoElement(elem, type_="FHIR."+type_))
                else:
                    elements.append(ClassInfoElement(elem, type_="List<%s>" % type_.__args__[0].__forward_arg__))
            return [ClassInfo(namespace="FHIR", name=type(val).__name__, baseType="FHIR." + type(val).__base__.__name__, element=elements)]

    def gettype_fromspec(self, type_):
        parts = type_.split(".")
        type_class = None
        type_name = parts[-1]
        type_ns = parts[0] if len(parts) > 1 else None
        if type_ns == "FHIR" or type_ns is None:
            try:
                type_class = getattr(self.model, type_name)
            except:
                if type_ns is not None:
                    raise BaseException("Unknown type %s" % type_)
        if type_ns == "System" or (type_ns is None and not type_class):
            for key, t_name in self.simple_type_names.items():
                if type_name == t_name:
                    type_class = key
            if not type_class:
                raise BaseException("Unknown type %s" % type_)
        return type_class

    def is_type(self, val, type_):
        val = self.single_value(val)
        if val == []:
            return []
        if isinstance(type_, str):
            type_class = self.gettype_fromspec(type_)
            if isinstance(val, bool) and type_class == int:
                return [False]
            else:
                return [isinstance(val, type_class)]
        elif isinstance(type_, list):
            return [False]

    def as_type(self, val, type_):
        return val if self.is_type(val, type_) == [True] else []

    def conformsTo(self, val, profile):
        if len(val) != 1 and len(profile) != 1:
            return [False]
        elif not isinstance(val[0], self.model.Element) and not (isinstance(profile[0], str) or isinstance(profile[0], self.model.string)):
            return [False]
        else:
            profile = self.string_value(profile[0])
            if profile.startswith("http://hl7.org/fhir/StructureDefinition/"):
                return type(val[0]).__name__ == profile.rstrip("/").split("/")[-1]
            else:
                meta = self.get(val[0], "meta") # TODO add test
                if not meta:
                    return False
                profiles = self.get(meta, "profile")
                for p in profiles:
                    p = self.string_value(p)
                    if p == profile:
                        return True
                return False

    def extension(self, val, extension):
        if val == [] or extension == []:
            return []
        else:
            extension = self.string_value(self.single_value(extension, str, self.model.string))
            for ext in self.get(val, "extension"):
                if ext.url == extension:
                    return [ext]
            return []

    def resolve(self, reference, context):
        reference = self.string_value(reference)
        is_absolute = bool(urlparse(reference).netloc)
        roots = set()
        for ctx in context:
            while getattr(ctx, "parent_object_", []):
                if ctx.parent_object_.__class__.__name__ == "ResourceContainer" and reference.startswith("#"):
                    break
                ctx = ctx.parent_object_
            if hasattr(ctx, "parent_object_"):
                roots.add(ctx)
        for root in roots:
            if root.gds_elementtree_node_.__class__.__module__ == "lxml.etree": # XML input
                parts = reference.split("/")
                if reference.startswith("#"):
                    elem = root.gds_elementtree_node_.xpath(".//*[@id='{0}' or @ID='{0}']".format(reference[1:]))
                    if elem:
                        return [_get_module(root).node_dict[elem[0]]]
                    else:
                        elem = root.gds_elementtree_node_.xpath(".//*[local-name()='id' and @value='{0}']".format(reference[1:]))
                        if elem:
                            return [_get_module(root).node_dict[elem[0]].parent_object_]
                elif not is_absolute and len(parts) == 2:
                    elem = root.gds_elementtree_node_.xpath("//*[local-name()='{0}']/*[local-name()='id' and @value='{1}']".format(parts[0], parts[1]))
                    if elem:
                        return [_get_module(root).node_dict[elem[0]].parent_object_]
                elif not is_absolute and len(parts) == 1:
                    elem = root.gds_elementtree_node_.xpath("//*[local-name()='id' and @value='{0}']".format(reference))
                    if elem:
                        return [_get_module(root).node_dict[elem[0]].parent_object_]
                else:
                    raise NotImplementedError("Resolve not implemented for non-local references")
            elif isinstance(root.gds_elementtree_node_, dict):
                def lookup(dict_var, type_, id):
                    for k, v in dict_var.items():
                        if k == "id" and v == id:
                            if type_ is not None and dict_var["resourceType"] != type_:
                                continue
                            yield dict_var
                        elif isinstance(v, list):
                            for v_ in v:
                                for id_val in lookup(v_, type_, id):
                                    yield id_val
                        elif isinstance(v, dict):
                            for id_val in lookup(v, type_, id):
                                yield id_val
                parts = reference.split("/")
                if reference.startswith("#"):
                    elem = next(iter(lookup(root.gds_elementtree_node_, None, reference[1:])), None)
                    if elem:
                        return [elem["@node"]]
                elif not is_absolute and len(parts) == 2:
                    elem = next(iter(lookup(root.gds_elementtree_node_, parts[0], parts[1])), None)
                    if elem:
                        return [elem["@node"]]
                elif not is_absolute and len(parts) == 1:
                    elem = next(iter(lookup(root.gds_elementtree_node_, None, parts[1])), None)
                    if elem:
                        return [elem["@node"]]
                else:
                    raise NotImplementedError("Resolve not implemented for non-local references")
            else:
                raise NotImplementedError("Resolve not implemented for input format")
        return []

def single(lst):
    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return lst[0]
    else:
        raise BaseException("Single value expected, multiple found.")

def _get_module(var_type):
    mod_split = var_type.__module__.split(".")
    return getattr(__import__(".".join(mod_split[0:-1]), fromlist=[mod_split[-1]]), mod_split[-1])
