#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Tue Feb 18 19:14:07 2025 by generateDS.py version 2.43.3.
# Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)]
#
# Command line options:
#   ('-o', 'vidi.py')
#   ('--no-questions', '')
#   ('-f', '')
#   ('--export', 'write json')
#   ('--create-mandatory-children', '')
#
# Command line arguments:
#   C:\Users\nikol\gitrepos\vidi-map\schemas\VIDi.xsd
#
# Command line:
#   generateDS.py -o "vidi.py" --no-questions -f --export="write json" --create-mandatory-children C:\Users\nikol\gitrepos\vidi-map\schemas\VIDi.xsd
#
# Current working directory (os.getcwd()):
#   generateds
#

import sys
try:
    ModulenotfoundExp_ = ModuleNotFoundError
except NameError:
    ModulenotfoundExp_ = ImportError
from six.moves import zip_longest
import os
import re as re_
import base64
# imports for django and/or sqlalchemy
import json as json_
import datetime as datetime_
import decimal as decimal_
from lxml import etree as etree_
from typing import List as List_


Validate_simpletypes_ = True
SaveElementTreeNode = True
SaveNodeDict = True
TagNamePrefix = ""
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str
node_dict = {}


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the _exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ModulenotfoundExp_ :
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ModulenotfoundExp_ :
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ModulenotfoundExp_ :

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ModulenotfoundExp_ :
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ModulenotfoundExp_ as exp:
    try:
        from generatedssupersuper import GeneratedsSuperSuper
    except ModulenotfoundExp_ as exp:
        class GeneratedsSuperSuper(object):
            pass
    
    class GeneratedsSuper(GeneratedsSuperSuper):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name
            def utcoffset(self, dt):
                return self.__offset
            def tzname(self, dt):
                return self.__name
            def dst(self, dt):
                return None
        def __str__(self):
            settings = {
                'str_pretty_print': True,
                'str_indent_level': 0,
                'str_namespaceprefix': '',
                'str_name': self.__class__.__name__,
                'str_namespacedefs': '',
            }
            for n in settings:
                if hasattr(self, n):
                    settings[n] = getattr(self, n)
            if sys.version_info.major == 2:
                from StringIO import StringIO
            else:
                from io import StringIO
            output = StringIO()
            self.export(
                output,
                settings['str_indent_level'],
                pretty_print=settings['str_pretty_print'],
                namespaceprefix_=settings['str_namespaceprefix'],
                name_=settings['str_name'],
                namespacedef_=settings['str_namespacedefs']
            )
            strval = output.getvalue()
            output.close()
            return strval
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_parse_string(self, input_data, node=None, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node=None, input_name=''):
            if not input_data:
                return ''
            else:
                return input_data
        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data).decode('ascii')
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % int(input_data)
        def gds_parse_integer(self, input_data, node=None, input_name=''):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires integer value: %s' % exp)
            return ival
        def gds_validate_integer(self, input_data, node=None, input_name=''):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires integer value')
            return value
        def gds_format_integer_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer values')
            return values
        def gds_format_float(self, input_data, input_name=''):
            value = ('%.15f' % float(input_data)).rstrip('0')
            if value.endswith('.'):
                value += '0'
            return value
    
        def gds_parse_float(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires float or double value: %s' % exp)
            return fval_
        def gds_validate_float(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires float value')
            return value
        def gds_format_float_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_float_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of float values')
            return values
        def gds_format_decimal(self, input_data, input_name=''):
            return_value = '%s' % input_data
            if '.' in return_value:
                return_value = return_value.rstrip('0')
                if return_value.endswith('.'):
                    return_value = return_value.rstrip('.')
            return return_value
        def gds_parse_decimal(self, input_data, node=None, input_name=''):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return decimal_value
        def gds_validate_decimal(self, input_data, node=None, input_name=''):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return value
        def gds_format_decimal_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return ' '.join([self.gds_format_decimal(item) for item in input_data])
        def gds_validate_decimal_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of decimal values')
            return values
        def gds_format_double(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_parse_double(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires double or float value: %s' % exp)
            return fval_
        def gds_validate_double(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires double or float value')
            return value
        def gds_format_double_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_double_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, 'Requires sequence of double or float values')
            return values
        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()
        def gds_parse_boolean(self, input_data, node=None, input_name=''):
            input_data = input_data.strip()
            if input_data in ('true', '1'):
                bval = True
            elif input_data in ('false', '0'):
                bval = False
            else:
                raise_parse_error(node, 'Requires boolean value')
            return bval
        def gds_validate_boolean(self, input_data, node=None, input_name=''):
            if input_data not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires boolean value '
                    '(one of True, 1, False, 0)')
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                value = self.gds_parse_boolean(value, node, input_name)
                if value not in (True, 1, False, 0, ):
                    raise_parse_error(
                        node,
                        'Requires sequence of boolean values '
                        '(one of True, 1, False, 0)')
            return values
        def gds_validate_datetime(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_datetime(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split('.')
            if len(time_parts) > 1:
                micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
                input_data = '%s.%s' % (
                    time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt
        def gds_validate_date(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_date(self, input_data, input_name=''):
            _svalue = '%04d-%02d-%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += 'Z'
                        else:
                            if total_seconds < 0:
                                _svalue += '-'
                                total_seconds *= -1
                            else:
                                _svalue += '+'
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += '{0:02d}:{1:02d}'.format(
                                hours, minutes)
            except AttributeError:
                pass
            return _svalue
        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
            dt = dt.replace(tzinfo=tz)
            return dt.date()
        def gds_validate_time(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_time(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%02d:%02d:%02d' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%02d:%02d:%02d.%s' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            target = str(target)
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1
        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.time()
        def gds_check_cardinality_(
                self, value, input_name,
                min_occurs=0, max_occurs=1, required=None):
            if value is None:
                length = 0
            elif isinstance(value, list):
                length = len(value)
            else:
                length = 1
            if required is not None :
                if required and length < 1:
                    self.gds_collector_.add_message(
                        "Required value {}{} is missing".format(
                            input_name, self.gds_get_node_lineno_()))
            if length < min_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is below "
                    "the minimum allowed, "
                    "expected at least {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        min_occurs, length))
            elif length > max_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is above "
                    "the maximum allowed, "
                    "expected at most {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        max_occurs, length))
        def gds_validate_builtin_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_validate_defined_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content
        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in mapping.items()))
        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = 'utf-8'
                return instring.encode(encoding)
            else:
                return instring
        @staticmethod
        def convert_unicode(instring):
            if instring is None:
                result = ""
            elif isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring, unicode):
                result = quote_xml(instring).encode('utf8')
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result
        def __eq__(self, other):
            def excl_select_objs_(obj):
                return (obj[0] != 'parent_object_' and
                        obj[0] != 'gds_collector_')
            if type(self) != type(other):
                return False
            return all(x == y for x, y in zip_longest(
                filter(excl_select_objs_, self.__dict__.items()),
                filter(excl_select_objs_, other.__dict__.items())))
        def __ne__(self, other):
            return not self.__eq__(other)
        # Django ETL transform hooks.
        def gds_djo_etl_transform(self):
            pass
        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass
        # SQLAlchemy ETL transform hooks.
        def gds_sqa_etl_transform(self):
            return 0, None
        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass
        def gds_get_node_lineno_(self):
            if (hasattr(self, "gds_elementtree_node_") and
                    self.gds_elementtree_node_ is not None):
                return ' near line {}'.format(
                    self.gds_elementtree_node_.sourceline)
            else:
                return ""
    
    
    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + 'Sub'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    s1 = s1.replace('\n', '&#10;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        if prefix == 'xml':
            namespace = 'http://www.w3.org/XML/1998/namespace'
        else:
            namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))
    def to_etree(self, element, mapping_=None, reverse_mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self, mapping_=None, reverse_mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)


#
# Start enum classes
#
#
# Start data representation classes
#
class vidi(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, v_current_medication_data: 'v_current_medication_dataType' = None, i_current_medication_data: 'i_current_medication_dataType' = None, v_past_medication_data: 'v_past_medication_dataType' = None, i_past_medication_data: 'i_past_medication_dataType' = None, v_allergies_data: 'v_allergies_dataType' = None, i_allergies_data: 'i_allergies_dataType' = None, v_current_problems_data: 'v_current_problems_dataType' = None, i_current_problems_data: 'i_current_problems_dataType' = None, v_past_problems_data: 'v_past_problems_dataType' = None, i_past_problems_data: 'i_past_problems_dataType' = None, v_family_problems_data: 'v_family_problems_dataType' = None, i_family_problems_data: 'i_family_problems_dataType' = None, v_procedures_data: 'v_procedures_dataType' = None, i_procedures_data: 'i_procedures_dataType' = None, v_results_data: 'v_results_dataType' = None, i_results_data: 'i_results_dataType' = None, v_vitalsigns_data: 'v_vitalsigns_dataType' = None, i_vitalsigns_data: 'i_vitalsigns_dataType' = None, v_socialhistory_data: 'v_socialhistory_dataType' = None, i_socialhistory_data: 'i_socialhistory_dataType' = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if v_current_medication_data is None:
            self.v_current_medication_data = globals()["v_current_medication_dataType"]()
        else:
            self.v_current_medication_data = v_current_medication_data
        self.v_current_medication_data_nsprefix_ = None
        if i_current_medication_data is None:
            self.i_current_medication_data = globals()["i_current_medication_dataType"]()
        else:
            self.i_current_medication_data = i_current_medication_data
        self.i_current_medication_data_nsprefix_ = None
        if v_past_medication_data is None:
            self.v_past_medication_data = globals()["v_past_medication_dataType"]()
        else:
            self.v_past_medication_data = v_past_medication_data
        self.v_past_medication_data_nsprefix_ = None
        if i_past_medication_data is None:
            self.i_past_medication_data = globals()["i_past_medication_dataType"]()
        else:
            self.i_past_medication_data = i_past_medication_data
        self.i_past_medication_data_nsprefix_ = None
        if v_allergies_data is None:
            self.v_allergies_data = globals()["v_allergies_dataType"]()
        else:
            self.v_allergies_data = v_allergies_data
        self.v_allergies_data_nsprefix_ = None
        if i_allergies_data is None:
            self.i_allergies_data = globals()["i_allergies_dataType"]()
        else:
            self.i_allergies_data = i_allergies_data
        self.i_allergies_data_nsprefix_ = None
        if v_current_problems_data is None:
            self.v_current_problems_data = globals()["v_current_problems_dataType"]()
        else:
            self.v_current_problems_data = v_current_problems_data
        self.v_current_problems_data_nsprefix_ = None
        if i_current_problems_data is None:
            self.i_current_problems_data = globals()["i_current_problems_dataType"]()
        else:
            self.i_current_problems_data = i_current_problems_data
        self.i_current_problems_data_nsprefix_ = None
        if v_past_problems_data is None:
            self.v_past_problems_data = globals()["v_past_problems_dataType"]()
        else:
            self.v_past_problems_data = v_past_problems_data
        self.v_past_problems_data_nsprefix_ = None
        if i_past_problems_data is None:
            self.i_past_problems_data = globals()["i_past_problems_dataType"]()
        else:
            self.i_past_problems_data = i_past_problems_data
        self.i_past_problems_data_nsprefix_ = None
        if v_family_problems_data is None:
            self.v_family_problems_data = globals()["v_family_problems_dataType"]()
        else:
            self.v_family_problems_data = v_family_problems_data
        self.v_family_problems_data_nsprefix_ = None
        if i_family_problems_data is None:
            self.i_family_problems_data = globals()["i_family_problems_dataType"]()
        else:
            self.i_family_problems_data = i_family_problems_data
        self.i_family_problems_data_nsprefix_ = None
        if v_procedures_data is None:
            self.v_procedures_data = globals()["v_procedures_dataType"]()
        else:
            self.v_procedures_data = v_procedures_data
        self.v_procedures_data_nsprefix_ = None
        if i_procedures_data is None:
            self.i_procedures_data = globals()["i_procedures_dataType"]()
        else:
            self.i_procedures_data = i_procedures_data
        self.i_procedures_data_nsprefix_ = None
        if v_results_data is None:
            self.v_results_data = globals()["v_results_dataType"]()
        else:
            self.v_results_data = v_results_data
        self.v_results_data_nsprefix_ = None
        if i_results_data is None:
            self.i_results_data = globals()["i_results_dataType"]()
        else:
            self.i_results_data = i_results_data
        self.i_results_data_nsprefix_ = None
        if v_vitalsigns_data is None:
            self.v_vitalsigns_data = globals()["v_vitalsigns_dataType"]()
        else:
            self.v_vitalsigns_data = v_vitalsigns_data
        self.v_vitalsigns_data_nsprefix_ = None
        if i_vitalsigns_data is None:
            self.i_vitalsigns_data = globals()["i_vitalsigns_dataType"]()
        else:
            self.i_vitalsigns_data = i_vitalsigns_data
        self.i_vitalsigns_data_nsprefix_ = None
        if v_socialhistory_data is None:
            self.v_socialhistory_data = globals()["v_socialhistory_dataType"]()
        else:
            self.v_socialhistory_data = v_socialhistory_data
        self.v_socialhistory_data_nsprefix_ = None
        if i_socialhistory_data is None:
            self.i_socialhistory_data = globals()["i_socialhistory_dataType"]()
        else:
            self.i_socialhistory_data = i_socialhistory_data
        self.i_socialhistory_data_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, vidi)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if vidi.subclass:
            return vidi.subclass(*args_, **kwargs_)
        else:
            return vidi(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_v_current_medication_data(self):
        return self.v_current_medication_data
    def set_v_current_medication_data(self, v_current_medication_data):
        self.v_current_medication_data = v_current_medication_data
    def get_i_current_medication_data(self):
        return self.i_current_medication_data
    def set_i_current_medication_data(self, i_current_medication_data):
        self.i_current_medication_data = i_current_medication_data
    def get_v_past_medication_data(self):
        return self.v_past_medication_data
    def set_v_past_medication_data(self, v_past_medication_data):
        self.v_past_medication_data = v_past_medication_data
    def get_i_past_medication_data(self):
        return self.i_past_medication_data
    def set_i_past_medication_data(self, i_past_medication_data):
        self.i_past_medication_data = i_past_medication_data
    def get_v_allergies_data(self):
        return self.v_allergies_data
    def set_v_allergies_data(self, v_allergies_data):
        self.v_allergies_data = v_allergies_data
    def get_i_allergies_data(self):
        return self.i_allergies_data
    def set_i_allergies_data(self, i_allergies_data):
        self.i_allergies_data = i_allergies_data
    def get_v_current_problems_data(self):
        return self.v_current_problems_data
    def set_v_current_problems_data(self, v_current_problems_data):
        self.v_current_problems_data = v_current_problems_data
    def get_i_current_problems_data(self):
        return self.i_current_problems_data
    def set_i_current_problems_data(self, i_current_problems_data):
        self.i_current_problems_data = i_current_problems_data
    def get_v_past_problems_data(self):
        return self.v_past_problems_data
    def set_v_past_problems_data(self, v_past_problems_data):
        self.v_past_problems_data = v_past_problems_data
    def get_i_past_problems_data(self):
        return self.i_past_problems_data
    def set_i_past_problems_data(self, i_past_problems_data):
        self.i_past_problems_data = i_past_problems_data
    def get_v_family_problems_data(self):
        return self.v_family_problems_data
    def set_v_family_problems_data(self, v_family_problems_data):
        self.v_family_problems_data = v_family_problems_data
    def get_i_family_problems_data(self):
        return self.i_family_problems_data
    def set_i_family_problems_data(self, i_family_problems_data):
        self.i_family_problems_data = i_family_problems_data
    def get_v_procedures_data(self):
        return self.v_procedures_data
    def set_v_procedures_data(self, v_procedures_data):
        self.v_procedures_data = v_procedures_data
    def get_i_procedures_data(self):
        return self.i_procedures_data
    def set_i_procedures_data(self, i_procedures_data):
        self.i_procedures_data = i_procedures_data
    def get_v_results_data(self):
        return self.v_results_data
    def set_v_results_data(self, v_results_data):
        self.v_results_data = v_results_data
    def get_i_results_data(self):
        return self.i_results_data
    def set_i_results_data(self, i_results_data):
        self.i_results_data = i_results_data
    def get_v_vitalsigns_data(self):
        return self.v_vitalsigns_data
    def set_v_vitalsigns_data(self, v_vitalsigns_data):
        self.v_vitalsigns_data = v_vitalsigns_data
    def get_i_vitalsigns_data(self):
        return self.i_vitalsigns_data
    def set_i_vitalsigns_data(self, i_vitalsigns_data):
        self.i_vitalsigns_data = i_vitalsigns_data
    def get_v_socialhistory_data(self):
        return self.v_socialhistory_data
    def set_v_socialhistory_data(self, v_socialhistory_data):
        self.v_socialhistory_data = v_socialhistory_data
    def get_i_socialhistory_data(self):
        return self.i_socialhistory_data
    def set_i_socialhistory_data(self, i_socialhistory_data):
        self.i_socialhistory_data = i_socialhistory_data
    def has__content(self):
        if (
            self.v_current_medication_data is not None or
            self.i_current_medication_data is not None or
            self.v_past_medication_data is not None or
            self.i_past_medication_data is not None or
            self.v_allergies_data is not None or
            self.i_allergies_data is not None or
            self.v_current_problems_data is not None or
            self.i_current_problems_data is not None or
            self.v_past_problems_data is not None or
            self.i_past_problems_data is not None or
            self.v_family_problems_data is not None or
            self.i_family_problems_data is not None or
            self.v_procedures_data is not None or
            self.i_procedures_data is not None or
            self.v_results_data is not None or
            self.i_results_data is not None or
            self.v_vitalsigns_data is not None or
            self.i_vitalsigns_data is not None or
            self.v_socialhistory_data is not None or
            self.i_socialhistory_data is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='vidi', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('vidi')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'vidi':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='vidi')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='vidi', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='vidi'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='vidi', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.v_current_medication_data is not None:
            namespaceprefix_ = self.v_current_medication_data_nsprefix_ + ':' if (UseCapturedNS_ and self.v_current_medication_data_nsprefix_) else ''
            self.v_current_medication_data.export(outfile, level, namespaceprefix_, namespacedef_='', name_='v_current_medication_data', pretty_print=pretty_print)
        if self.i_current_medication_data is not None:
            namespaceprefix_ = self.i_current_medication_data_nsprefix_ + ':' if (UseCapturedNS_ and self.i_current_medication_data_nsprefix_) else ''
            self.i_current_medication_data.export(outfile, level, namespaceprefix_, namespacedef_='', name_='i_current_medication_data', pretty_print=pretty_print)
        if self.v_past_medication_data is not None:
            namespaceprefix_ = self.v_past_medication_data_nsprefix_ + ':' if (UseCapturedNS_ and self.v_past_medication_data_nsprefix_) else ''
            self.v_past_medication_data.export(outfile, level, namespaceprefix_, namespacedef_='', name_='v_past_medication_data', pretty_print=pretty_print)
        if self.i_past_medication_data is not None:
            namespaceprefix_ = self.i_past_medication_data_nsprefix_ + ':' if (UseCapturedNS_ and self.i_past_medication_data_nsprefix_) else ''
            self.i_past_medication_data.export(outfile, level, namespaceprefix_, namespacedef_='', name_='i_past_medication_data', pretty_print=pretty_print)
        if self.v_allergies_data is not None:
            namespaceprefix_ = self.v_allergies_data_nsprefix_ + ':' if (UseCapturedNS_ and self.v_allergies_data_nsprefix_) else ''
            self.v_allergies_data.export(outfile, level, namespaceprefix_, namespacedef_='', name_='v_allergies_data', pretty_print=pretty_print)
        if self.i_allergies_data is not None:
            namespaceprefix_ = self.i_allergies_data_nsprefix_ + ':' if (UseCapturedNS_ and self.i_allergies_data_nsprefix_) else ''
            self.i_allergies_data.export(outfile, level, namespaceprefix_, namespacedef_='', name_='i_allergies_data', pretty_print=pretty_print)
        if self.v_current_problems_data is not None:
            namespaceprefix_ = self.v_current_problems_data_nsprefix_ + ':' if (UseCapturedNS_ and self.v_current_problems_data_nsprefix_) else ''
            self.v_current_problems_data.export(outfile, level, namespaceprefix_, namespacedef_='', name_='v_current_problems_data', pretty_print=pretty_print)
        if self.i_current_problems_data is not None:
            namespaceprefix_ = self.i_current_problems_data_nsprefix_ + ':' if (UseCapturedNS_ and self.i_current_problems_data_nsprefix_) else ''
            self.i_current_problems_data.export(outfile, level, namespaceprefix_, namespacedef_='', name_='i_current_problems_data', pretty_print=pretty_print)
        if self.v_past_problems_data is not None:
            namespaceprefix_ = self.v_past_problems_data_nsprefix_ + ':' if (UseCapturedNS_ and self.v_past_problems_data_nsprefix_) else ''
            self.v_past_problems_data.export(outfile, level, namespaceprefix_, namespacedef_='', name_='v_past_problems_data', pretty_print=pretty_print)
        if self.i_past_problems_data is not None:
            namespaceprefix_ = self.i_past_problems_data_nsprefix_ + ':' if (UseCapturedNS_ and self.i_past_problems_data_nsprefix_) else ''
            self.i_past_problems_data.export(outfile, level, namespaceprefix_, namespacedef_='', name_='i_past_problems_data', pretty_print=pretty_print)
        if self.v_family_problems_data is not None:
            namespaceprefix_ = self.v_family_problems_data_nsprefix_ + ':' if (UseCapturedNS_ and self.v_family_problems_data_nsprefix_) else ''
            self.v_family_problems_data.export(outfile, level, namespaceprefix_, namespacedef_='', name_='v_family_problems_data', pretty_print=pretty_print)
        if self.i_family_problems_data is not None:
            namespaceprefix_ = self.i_family_problems_data_nsprefix_ + ':' if (UseCapturedNS_ and self.i_family_problems_data_nsprefix_) else ''
            self.i_family_problems_data.export(outfile, level, namespaceprefix_, namespacedef_='', name_='i_family_problems_data', pretty_print=pretty_print)
        if self.v_procedures_data is not None:
            namespaceprefix_ = self.v_procedures_data_nsprefix_ + ':' if (UseCapturedNS_ and self.v_procedures_data_nsprefix_) else ''
            self.v_procedures_data.export(outfile, level, namespaceprefix_, namespacedef_='', name_='v_procedures_data', pretty_print=pretty_print)
        if self.i_procedures_data is not None:
            namespaceprefix_ = self.i_procedures_data_nsprefix_ + ':' if (UseCapturedNS_ and self.i_procedures_data_nsprefix_) else ''
            self.i_procedures_data.export(outfile, level, namespaceprefix_, namespacedef_='', name_='i_procedures_data', pretty_print=pretty_print)
        if self.v_results_data is not None:
            namespaceprefix_ = self.v_results_data_nsprefix_ + ':' if (UseCapturedNS_ and self.v_results_data_nsprefix_) else ''
            self.v_results_data.export(outfile, level, namespaceprefix_, namespacedef_='', name_='v_results_data', pretty_print=pretty_print)
        if self.i_results_data is not None:
            namespaceprefix_ = self.i_results_data_nsprefix_ + ':' if (UseCapturedNS_ and self.i_results_data_nsprefix_) else ''
            self.i_results_data.export(outfile, level, namespaceprefix_, namespacedef_='', name_='i_results_data', pretty_print=pretty_print)
        if self.v_vitalsigns_data is not None:
            namespaceprefix_ = self.v_vitalsigns_data_nsprefix_ + ':' if (UseCapturedNS_ and self.v_vitalsigns_data_nsprefix_) else ''
            self.v_vitalsigns_data.export(outfile, level, namespaceprefix_, namespacedef_='', name_='v_vitalsigns_data', pretty_print=pretty_print)
        if self.i_vitalsigns_data is not None:
            namespaceprefix_ = self.i_vitalsigns_data_nsprefix_ + ':' if (UseCapturedNS_ and self.i_vitalsigns_data_nsprefix_) else ''
            self.i_vitalsigns_data.export(outfile, level, namespaceprefix_, namespacedef_='', name_='i_vitalsigns_data', pretty_print=pretty_print)
        if self.v_socialhistory_data is not None:
            namespaceprefix_ = self.v_socialhistory_data_nsprefix_ + ':' if (UseCapturedNS_ and self.v_socialhistory_data_nsprefix_) else ''
            self.v_socialhistory_data.export(outfile, level, namespaceprefix_, namespacedef_='', name_='v_socialhistory_data', pretty_print=pretty_print)
        if self.i_socialhistory_data is not None:
            namespaceprefix_ = self.i_socialhistory_data_nsprefix_ + ':' if (UseCapturedNS_ and self.i_socialhistory_data_nsprefix_) else ''
            self.i_socialhistory_data.export(outfile, level, namespaceprefix_, namespacedef_='', name_='i_socialhistory_data', pretty_print=pretty_print)
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.v_current_medication_data is not None:
            child_dict = self.v_current_medication_data.exportJson(json_dict, 'v_current_medication_data', False)
            if child_dict:
                json_dict['v_current_medication_data'] = child_dict
        if self.i_current_medication_data is not None:
            child_dict = self.i_current_medication_data.exportJson(json_dict, 'i_current_medication_data', False)
            if child_dict:
                json_dict['i_current_medication_data'] = child_dict
        if self.v_past_medication_data is not None:
            child_dict = self.v_past_medication_data.exportJson(json_dict, 'v_past_medication_data', False)
            if child_dict:
                json_dict['v_past_medication_data'] = child_dict
        if self.i_past_medication_data is not None:
            child_dict = self.i_past_medication_data.exportJson(json_dict, 'i_past_medication_data', False)
            if child_dict:
                json_dict['i_past_medication_data'] = child_dict
        if self.v_allergies_data is not None:
            child_dict = self.v_allergies_data.exportJson(json_dict, 'v_allergies_data', False)
            if child_dict:
                json_dict['v_allergies_data'] = child_dict
        if self.i_allergies_data is not None:
            child_dict = self.i_allergies_data.exportJson(json_dict, 'i_allergies_data', False)
            if child_dict:
                json_dict['i_allergies_data'] = child_dict
        if self.v_current_problems_data is not None:
            child_dict = self.v_current_problems_data.exportJson(json_dict, 'v_current_problems_data', False)
            if child_dict:
                json_dict['v_current_problems_data'] = child_dict
        if self.i_current_problems_data is not None:
            child_dict = self.i_current_problems_data.exportJson(json_dict, 'i_current_problems_data', False)
            if child_dict:
                json_dict['i_current_problems_data'] = child_dict
        if self.v_past_problems_data is not None:
            child_dict = self.v_past_problems_data.exportJson(json_dict, 'v_past_problems_data', False)
            if child_dict:
                json_dict['v_past_problems_data'] = child_dict
        if self.i_past_problems_data is not None:
            child_dict = self.i_past_problems_data.exportJson(json_dict, 'i_past_problems_data', False)
            if child_dict:
                json_dict['i_past_problems_data'] = child_dict
        if self.v_family_problems_data is not None:
            child_dict = self.v_family_problems_data.exportJson(json_dict, 'v_family_problems_data', False)
            if child_dict:
                json_dict['v_family_problems_data'] = child_dict
        if self.i_family_problems_data is not None:
            child_dict = self.i_family_problems_data.exportJson(json_dict, 'i_family_problems_data', False)
            if child_dict:
                json_dict['i_family_problems_data'] = child_dict
        if self.v_procedures_data is not None:
            child_dict = self.v_procedures_data.exportJson(json_dict, 'v_procedures_data', False)
            if child_dict:
                json_dict['v_procedures_data'] = child_dict
        if self.i_procedures_data is not None:
            child_dict = self.i_procedures_data.exportJson(json_dict, 'i_procedures_data', False)
            if child_dict:
                json_dict['i_procedures_data'] = child_dict
        if self.v_results_data is not None:
            child_dict = self.v_results_data.exportJson(json_dict, 'v_results_data', False)
            if child_dict:
                json_dict['v_results_data'] = child_dict
        if self.i_results_data is not None:
            child_dict = self.i_results_data.exportJson(json_dict, 'i_results_data', False)
            if child_dict:
                json_dict['i_results_data'] = child_dict
        if self.v_vitalsigns_data is not None:
            child_dict = self.v_vitalsigns_data.exportJson(json_dict, 'v_vitalsigns_data', False)
            if child_dict:
                json_dict['v_vitalsigns_data'] = child_dict
        if self.i_vitalsigns_data is not None:
            child_dict = self.i_vitalsigns_data.exportJson(json_dict, 'i_vitalsigns_data', False)
            if child_dict:
                json_dict['i_vitalsigns_data'] = child_dict
        if self.v_socialhistory_data is not None:
            child_dict = self.v_socialhistory_data.exportJson(json_dict, 'v_socialhistory_data', False)
            if child_dict:
                json_dict['v_socialhistory_data'] = child_dict
        if self.i_socialhistory_data is not None:
            child_dict = self.i_socialhistory_data.exportJson(json_dict, 'i_socialhistory_data', False)
            if child_dict:
                json_dict['i_socialhistory_data'] = child_dict
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'v_current_medication_data':
            obj_ = v_current_medication_dataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.v_current_medication_data = obj_
            obj_.original_tagname_ = 'v_current_medication_data'
        elif nodeName_ == 'i_current_medication_data':
            obj_ = i_current_medication_dataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.i_current_medication_data = obj_
            obj_.original_tagname_ = 'i_current_medication_data'
        elif nodeName_ == 'v_past_medication_data':
            obj_ = v_past_medication_dataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.v_past_medication_data = obj_
            obj_.original_tagname_ = 'v_past_medication_data'
        elif nodeName_ == 'i_past_medication_data':
            obj_ = i_past_medication_dataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.i_past_medication_data = obj_
            obj_.original_tagname_ = 'i_past_medication_data'
        elif nodeName_ == 'v_allergies_data':
            obj_ = v_allergies_dataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.v_allergies_data = obj_
            obj_.original_tagname_ = 'v_allergies_data'
        elif nodeName_ == 'i_allergies_data':
            obj_ = i_allergies_dataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.i_allergies_data = obj_
            obj_.original_tagname_ = 'i_allergies_data'
        elif nodeName_ == 'v_current_problems_data':
            obj_ = v_current_problems_dataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.v_current_problems_data = obj_
            obj_.original_tagname_ = 'v_current_problems_data'
        elif nodeName_ == 'i_current_problems_data':
            obj_ = i_current_problems_dataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.i_current_problems_data = obj_
            obj_.original_tagname_ = 'i_current_problems_data'
        elif nodeName_ == 'v_past_problems_data':
            obj_ = v_past_problems_dataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.v_past_problems_data = obj_
            obj_.original_tagname_ = 'v_past_problems_data'
        elif nodeName_ == 'i_past_problems_data':
            obj_ = i_past_problems_dataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.i_past_problems_data = obj_
            obj_.original_tagname_ = 'i_past_problems_data'
        elif nodeName_ == 'v_family_problems_data':
            obj_ = v_family_problems_dataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.v_family_problems_data = obj_
            obj_.original_tagname_ = 'v_family_problems_data'
        elif nodeName_ == 'i_family_problems_data':
            obj_ = i_family_problems_dataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.i_family_problems_data = obj_
            obj_.original_tagname_ = 'i_family_problems_data'
        elif nodeName_ == 'v_procedures_data':
            obj_ = v_procedures_dataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.v_procedures_data = obj_
            obj_.original_tagname_ = 'v_procedures_data'
        elif nodeName_ == 'i_procedures_data':
            obj_ = i_procedures_dataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.i_procedures_data = obj_
            obj_.original_tagname_ = 'i_procedures_data'
        elif nodeName_ == 'v_results_data':
            obj_ = v_results_dataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.v_results_data = obj_
            obj_.original_tagname_ = 'v_results_data'
        elif nodeName_ == 'i_results_data':
            obj_ = i_results_dataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.i_results_data = obj_
            obj_.original_tagname_ = 'i_results_data'
        elif nodeName_ == 'v_vitalsigns_data':
            obj_ = v_vitalsigns_dataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.v_vitalsigns_data = obj_
            obj_.original_tagname_ = 'v_vitalsigns_data'
        elif nodeName_ == 'i_vitalsigns_data':
            obj_ = i_vitalsigns_dataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.i_vitalsigns_data = obj_
            obj_.original_tagname_ = 'i_vitalsigns_data'
        elif nodeName_ == 'v_socialhistory_data':
            obj_ = v_socialhistory_dataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.v_socialhistory_data = obj_
            obj_.original_tagname_ = 'v_socialhistory_data'
        elif nodeName_ == 'i_socialhistory_data':
            obj_ = i_socialhistory_dataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.i_socialhistory_data = obj_
            obj_.original_tagname_ = 'i_socialhistory_data'
# end class vidi


class v_current_medication_dataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, movableColumns: 'boolean' = False, data: List_['dataType'] = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.movableColumns = movableColumns
        self.movableColumns_nsprefix_ = None
        if data is None:
            self.data = []
        else:
            self.data = data
        self.data_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, v_current_medication_dataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if v_current_medication_dataType.subclass:
            return v_current_medication_dataType.subclass(*args_, **kwargs_)
        else:
            return v_current_medication_dataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_movableColumns(self):
        return self.movableColumns
    def set_movableColumns(self, movableColumns):
        self.movableColumns = movableColumns
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def add_data(self, value):
        self.data.append(value)
    def insert_data_at(self, index, value):
        self.data.insert(index, value)
    def replace_data_at(self, index, value):
        self.data[index] = value
    def has__content(self):
        if (
            self.movableColumns or
            self.data
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='v_current_medication_dataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('v_current_medication_dataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'v_current_medication_dataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='v_current_medication_dataType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='v_current_medication_dataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='v_current_medication_dataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='v_current_medication_dataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.movableColumns is not None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>%s</%smovableColumns>%s' % (namespaceprefix_ , self.gds_format_boolean(self.movableColumns, input_name='movableColumns'), namespaceprefix_ , eol_))
        if self.movableColumns is None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>false</%smovableColumns/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        for data_ in self.data:
            namespaceprefix_ = self.data_nsprefix_ + ':' if (UseCapturedNS_ and self.data_nsprefix_) else ''
            data_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='data', pretty_print=pretty_print)
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.movableColumns is not None:
            json_dict['movableColumns'] = self.movableColumns
        child_list = []
        for child in self.data:
            child_dict = child.exportJson(json_dict, 'data', True)
            if child_dict:
                child_list.append(child_dict)
        if child_list:
            json_dict['data'] = child_list
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'movableColumns':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'movableColumns')
            ival_ = self.gds_validate_boolean(ival_, node, 'movableColumns')
            self.movableColumns = ival_
            self.movableColumns_nsprefix_ = child_.prefix
        elif nodeName_ == 'data':
            obj_ = dataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.data.append(obj_)
            obj_.original_tagname_ = 'data'
# end class v_current_medication_dataType


class dataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name: 'string' = 'Keine aktuelle Medikation bekannt', dosis: 'string' = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = name
        self.name_nsprefix_ = None
        self.dosis = dosis
        self.dosis_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dataType.subclass:
            return dataType.subclass(*args_, **kwargs_)
        else:
            return dataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_dosis(self):
        return self.dosis
    def set_dosis(self, dosis):
        self.dosis = dosis
    def has__content(self):
        if (
            self.name != "Keine aktuelle Medikation bekannt" or
            self.dosis is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dataType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sname>%s</%sname>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.name), input_name='name')), namespaceprefix_ , eol_))
        if self.name is None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sname>Keine aktuelle Medikation bekannt</%sname/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.dosis is not None:
            namespaceprefix_ = self.dosis_nsprefix_ + ':' if (UseCapturedNS_ and self.dosis_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdosis>%s</%sdosis>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.dosis), input_name='dosis')), namespaceprefix_ , eol_))
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.name is not None:
            json_dict['name'] = self.name
        if self.dosis is not None:
            json_dict['dosis'] = self.dosis
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
        elif nodeName_ == 'dosis':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'dosis')
            value_ = self.gds_validate_string(value_, node, 'dosis')
            self.dosis = value_
            self.dosis_nsprefix_ = child_.prefix
# end class dataType


class i_current_medication_dataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, movableColumns: 'string' = None, data: List_['dataType1'] = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.movableColumns = movableColumns
        self.movableColumns_nsprefix_ = None
        if data is None:
            self.data = []
        else:
            self.data = data
        self.data_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, i_current_medication_dataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if i_current_medication_dataType.subclass:
            return i_current_medication_dataType.subclass(*args_, **kwargs_)
        else:
            return i_current_medication_dataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_movableColumns(self):
        return self.movableColumns
    def set_movableColumns(self, movableColumns):
        self.movableColumns = movableColumns
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def add_data(self, value):
        self.data.append(value)
    def insert_data_at(self, index, value):
        self.data.insert(index, value)
    def replace_data_at(self, index, value):
        self.data[index] = value
    def has__content(self):
        if (
            self.movableColumns is not None or
            self.data
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='i_current_medication_dataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('i_current_medication_dataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'i_current_medication_dataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='i_current_medication_dataType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='i_current_medication_dataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='i_current_medication_dataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='i_current_medication_dataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.movableColumns is not None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>%s</%smovableColumns>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.movableColumns), input_name='movableColumns')), namespaceprefix_ , eol_))
        for data_ in self.data:
            namespaceprefix_ = self.data_nsprefix_ + ':' if (UseCapturedNS_ and self.data_nsprefix_) else ''
            data_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='data', pretty_print=pretty_print)
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.movableColumns is not None:
            json_dict['movableColumns'] = self.movableColumns
        child_list = []
        for child in self.data:
            child_dict = child.exportJson(json_dict, 'data', True)
            if child_dict:
                child_list.append(child_dict)
        if child_list:
            json_dict['data'] = child_list
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'movableColumns':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'movableColumns')
            value_ = self.gds_validate_string(value_, node, 'movableColumns')
            self.movableColumns = value_
            self.movableColumns_nsprefix_ = child_.prefix
        elif nodeName_ == 'data':
            obj_ = dataType1.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.data.append(obj_)
            obj_.original_tagname_ = 'data'
# end class i_current_medication_dataType


class dataType1(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name: 'string' = 'Keine aktuelle Medikation bekannt', dosis: 'string' = None, beginn: 'string' = None, status: 'string' = None, code: 'string' = None, codesystem: 'string' = None, codesystem_type: 'string' = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = name
        self.name_nsprefix_ = None
        self.dosis = dosis
        self.dosis_nsprefix_ = None
        self.beginn = beginn
        self.beginn_nsprefix_ = None
        self.status = status
        self.status_nsprefix_ = None
        self.code = code
        self.code_nsprefix_ = None
        self.codesystem = codesystem
        self.codesystem_nsprefix_ = None
        self.codesystem_type = codesystem_type
        self.codesystem_type_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dataType1)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dataType1.subclass:
            return dataType1.subclass(*args_, **kwargs_)
        else:
            return dataType1(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_dosis(self):
        return self.dosis
    def set_dosis(self, dosis):
        self.dosis = dosis
    def get_beginn(self):
        return self.beginn
    def set_beginn(self, beginn):
        self.beginn = beginn
    def get_status(self):
        return self.status
    def set_status(self, status):
        self.status = status
    def get_code(self):
        return self.code
    def set_code(self, code):
        self.code = code
    def get_codesystem(self):
        return self.codesystem
    def set_codesystem(self, codesystem):
        self.codesystem = codesystem
    def get_codesystem_type(self):
        return self.codesystem_type
    def set_codesystem_type(self, codesystem_type):
        self.codesystem_type = codesystem_type
    def has__content(self):
        if (
            self.name != "Keine aktuelle Medikation bekannt" or
            self.dosis is not None or
            self.beginn is not None or
            self.status is not None or
            self.code is not None or
            self.codesystem is not None or
            self.codesystem_type is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType1', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dataType1')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dataType1':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dataType1')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dataType1', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dataType1'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType1', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sname>%s</%sname>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.name), input_name='name')), namespaceprefix_ , eol_))
        if self.name is None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sname>Keine aktuelle Medikation bekannt</%sname/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.dosis is not None:
            namespaceprefix_ = self.dosis_nsprefix_ + ':' if (UseCapturedNS_ and self.dosis_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdosis>%s</%sdosis>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.dosis), input_name='dosis')), namespaceprefix_ , eol_))
        if self.beginn is not None:
            namespaceprefix_ = self.beginn_nsprefix_ + ':' if (UseCapturedNS_ and self.beginn_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbeginn>%s</%sbeginn>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.beginn), input_name='beginn')), namespaceprefix_ , eol_))
        if self.status is not None:
            namespaceprefix_ = self.status_nsprefix_ + ':' if (UseCapturedNS_ and self.status_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstatus>%s</%sstatus>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.status), input_name='status')), namespaceprefix_ , eol_))
        if self.code is not None:
            namespaceprefix_ = self.code_nsprefix_ + ':' if (UseCapturedNS_ and self.code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scode>%s</%scode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.code), input_name='code')), namespaceprefix_ , eol_))
        if self.codesystem is not None:
            namespaceprefix_ = self.codesystem_nsprefix_ + ':' if (UseCapturedNS_ and self.codesystem_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodesystem>%s</%scodesystem>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codesystem), input_name='codesystem')), namespaceprefix_ , eol_))
        if self.codesystem_type is not None:
            namespaceprefix_ = self.codesystem_type_nsprefix_ + ':' if (UseCapturedNS_ and self.codesystem_type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodesystem_type>%s</%scodesystem_type>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codesystem_type), input_name='codesystem_type')), namespaceprefix_ , eol_))
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.name is not None:
            json_dict['name'] = self.name
        if self.dosis is not None:
            json_dict['dosis'] = self.dosis
        if self.beginn is not None:
            json_dict['beginn'] = self.beginn
        if self.status is not None:
            json_dict['status'] = self.status
        if self.code is not None:
            json_dict['code'] = self.code
        if self.codesystem is not None:
            json_dict['codesystem'] = self.codesystem
        if self.codesystem_type is not None:
            json_dict['codesystem_type'] = self.codesystem_type
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
        elif nodeName_ == 'dosis':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'dosis')
            value_ = self.gds_validate_string(value_, node, 'dosis')
            self.dosis = value_
            self.dosis_nsprefix_ = child_.prefix
        elif nodeName_ == 'beginn':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'beginn')
            value_ = self.gds_validate_string(value_, node, 'beginn')
            self.beginn = value_
            self.beginn_nsprefix_ = child_.prefix
        elif nodeName_ == 'status':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'status')
            value_ = self.gds_validate_string(value_, node, 'status')
            self.status = value_
            self.status_nsprefix_ = child_.prefix
        elif nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
        elif nodeName_ == 'codesystem':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codesystem')
            value_ = self.gds_validate_string(value_, node, 'codesystem')
            self.codesystem = value_
            self.codesystem_nsprefix_ = child_.prefix
        elif nodeName_ == 'codesystem_type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codesystem_type')
            value_ = self.gds_validate_string(value_, node, 'codesystem_type')
            self.codesystem_type = value_
            self.codesystem_type_nsprefix_ = child_.prefix
# end class dataType1


class v_past_medication_dataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, movableColumns: 'boolean' = False, data: List_['dataType2'] = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.movableColumns = movableColumns
        self.movableColumns_nsprefix_ = None
        if data is None:
            self.data = []
        else:
            self.data = data
        self.data_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, v_past_medication_dataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if v_past_medication_dataType.subclass:
            return v_past_medication_dataType.subclass(*args_, **kwargs_)
        else:
            return v_past_medication_dataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_movableColumns(self):
        return self.movableColumns
    def set_movableColumns(self, movableColumns):
        self.movableColumns = movableColumns
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def add_data(self, value):
        self.data.append(value)
    def insert_data_at(self, index, value):
        self.data.insert(index, value)
    def replace_data_at(self, index, value):
        self.data[index] = value
    def has__content(self):
        if (
            self.movableColumns or
            self.data
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='v_past_medication_dataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('v_past_medication_dataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'v_past_medication_dataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='v_past_medication_dataType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='v_past_medication_dataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='v_past_medication_dataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='v_past_medication_dataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.movableColumns is not None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>%s</%smovableColumns>%s' % (namespaceprefix_ , self.gds_format_boolean(self.movableColumns, input_name='movableColumns'), namespaceprefix_ , eol_))
        if self.movableColumns is None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>false</%smovableColumns/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        for data_ in self.data:
            namespaceprefix_ = self.data_nsprefix_ + ':' if (UseCapturedNS_ and self.data_nsprefix_) else ''
            data_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='data', pretty_print=pretty_print)
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.movableColumns is not None:
            json_dict['movableColumns'] = self.movableColumns
        child_list = []
        for child in self.data:
            child_dict = child.exportJson(json_dict, 'data', True)
            if child_dict:
                child_list.append(child_dict)
        if child_list:
            json_dict['data'] = child_list
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'movableColumns':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'movableColumns')
            ival_ = self.gds_validate_boolean(ival_, node, 'movableColumns')
            self.movableColumns = ival_
            self.movableColumns_nsprefix_ = child_.prefix
        elif nodeName_ == 'data':
            obj_ = dataType2.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.data.append(obj_)
            obj_.original_tagname_ = 'data'
# end class v_past_medication_dataType


class dataType2(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name: 'string' = 'Keine vergangene Medikation bekannt', dosis: 'string' = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = name
        self.name_nsprefix_ = None
        self.dosis = dosis
        self.dosis_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dataType2)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dataType2.subclass:
            return dataType2.subclass(*args_, **kwargs_)
        else:
            return dataType2(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_dosis(self):
        return self.dosis
    def set_dosis(self, dosis):
        self.dosis = dosis
    def has__content(self):
        if (
            self.name != "Keine vergangene Medikation bekannt" or
            self.dosis is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType2', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dataType2')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dataType2':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dataType2')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dataType2', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dataType2'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType2', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sname>%s</%sname>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.name), input_name='name')), namespaceprefix_ , eol_))
        if self.name is None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sname>Keine vergangene Medikation bekannt</%sname/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.dosis is not None:
            namespaceprefix_ = self.dosis_nsprefix_ + ':' if (UseCapturedNS_ and self.dosis_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdosis>%s</%sdosis>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.dosis), input_name='dosis')), namespaceprefix_ , eol_))
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.name is not None:
            json_dict['name'] = self.name
        if self.dosis is not None:
            json_dict['dosis'] = self.dosis
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
        elif nodeName_ == 'dosis':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'dosis')
            value_ = self.gds_validate_string(value_, node, 'dosis')
            self.dosis = value_
            self.dosis_nsprefix_ = child_.prefix
# end class dataType2


class i_past_medication_dataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, movableColumns: 'boolean' = True, data: List_['dataType3'] = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.movableColumns = movableColumns
        self.movableColumns_nsprefix_ = None
        if data is None:
            self.data = []
        else:
            self.data = data
        self.data_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, i_past_medication_dataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if i_past_medication_dataType.subclass:
            return i_past_medication_dataType.subclass(*args_, **kwargs_)
        else:
            return i_past_medication_dataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_movableColumns(self):
        return self.movableColumns
    def set_movableColumns(self, movableColumns):
        self.movableColumns = movableColumns
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def add_data(self, value):
        self.data.append(value)
    def insert_data_at(self, index, value):
        self.data.insert(index, value)
    def replace_data_at(self, index, value):
        self.data[index] = value
    def has__content(self):
        if (
            not self.movableColumns or
            self.data
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='i_past_medication_dataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('i_past_medication_dataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'i_past_medication_dataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='i_past_medication_dataType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='i_past_medication_dataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='i_past_medication_dataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='i_past_medication_dataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.movableColumns is not None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>%s</%smovableColumns>%s' % (namespaceprefix_ , self.gds_format_boolean(self.movableColumns, input_name='movableColumns'), namespaceprefix_ , eol_))
        if self.movableColumns is None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>true</%smovableColumns/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        for data_ in self.data:
            namespaceprefix_ = self.data_nsprefix_ + ':' if (UseCapturedNS_ and self.data_nsprefix_) else ''
            data_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='data', pretty_print=pretty_print)
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.movableColumns is not None:
            json_dict['movableColumns'] = self.movableColumns
        child_list = []
        for child in self.data:
            child_dict = child.exportJson(json_dict, 'data', True)
            if child_dict:
                child_list.append(child_dict)
        if child_list:
            json_dict['data'] = child_list
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'movableColumns':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'movableColumns')
            ival_ = self.gds_validate_boolean(ival_, node, 'movableColumns')
            self.movableColumns = ival_
            self.movableColumns_nsprefix_ = child_.prefix
        elif nodeName_ == 'data':
            obj_ = dataType3.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.data.append(obj_)
            obj_.original_tagname_ = 'data'
# end class i_past_medication_dataType


class dataType3(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name: 'string' = 'Keine vergangene Medikation bekannt', dosis: 'string' = None, beginn: 'string' = None, status: 'string' = None, code: 'string' = None, codesystem: 'string' = None, codesystem_type: 'string' = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = name
        self.name_nsprefix_ = None
        self.dosis = dosis
        self.dosis_nsprefix_ = None
        self.beginn = beginn
        self.beginn_nsprefix_ = None
        self.status = status
        self.status_nsprefix_ = None
        self.code = code
        self.code_nsprefix_ = None
        self.codesystem = codesystem
        self.codesystem_nsprefix_ = None
        self.codesystem_type = codesystem_type
        self.codesystem_type_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dataType3)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dataType3.subclass:
            return dataType3.subclass(*args_, **kwargs_)
        else:
            return dataType3(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_dosis(self):
        return self.dosis
    def set_dosis(self, dosis):
        self.dosis = dosis
    def get_beginn(self):
        return self.beginn
    def set_beginn(self, beginn):
        self.beginn = beginn
    def get_status(self):
        return self.status
    def set_status(self, status):
        self.status = status
    def get_code(self):
        return self.code
    def set_code(self, code):
        self.code = code
    def get_codesystem(self):
        return self.codesystem
    def set_codesystem(self, codesystem):
        self.codesystem = codesystem
    def get_codesystem_type(self):
        return self.codesystem_type
    def set_codesystem_type(self, codesystem_type):
        self.codesystem_type = codesystem_type
    def has__content(self):
        if (
            self.name != "Keine vergangene Medikation bekannt" or
            self.dosis is not None or
            self.beginn is not None or
            self.status is not None or
            self.code is not None or
            self.codesystem is not None or
            self.codesystem_type is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType3', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dataType3')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dataType3':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dataType3')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dataType3', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dataType3'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType3', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sname>%s</%sname>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.name), input_name='name')), namespaceprefix_ , eol_))
        if self.name is None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sname>Keine vergangene Medikation bekannt</%sname/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.dosis is not None:
            namespaceprefix_ = self.dosis_nsprefix_ + ':' if (UseCapturedNS_ and self.dosis_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdosis>%s</%sdosis>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.dosis), input_name='dosis')), namespaceprefix_ , eol_))
        if self.beginn is not None:
            namespaceprefix_ = self.beginn_nsprefix_ + ':' if (UseCapturedNS_ and self.beginn_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbeginn>%s</%sbeginn>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.beginn), input_name='beginn')), namespaceprefix_ , eol_))
        if self.status is not None:
            namespaceprefix_ = self.status_nsprefix_ + ':' if (UseCapturedNS_ and self.status_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstatus>%s</%sstatus>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.status), input_name='status')), namespaceprefix_ , eol_))
        if self.code is not None:
            namespaceprefix_ = self.code_nsprefix_ + ':' if (UseCapturedNS_ and self.code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scode>%s</%scode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.code), input_name='code')), namespaceprefix_ , eol_))
        if self.codesystem is not None:
            namespaceprefix_ = self.codesystem_nsprefix_ + ':' if (UseCapturedNS_ and self.codesystem_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodesystem>%s</%scodesystem>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codesystem), input_name='codesystem')), namespaceprefix_ , eol_))
        if self.codesystem_type is not None:
            namespaceprefix_ = self.codesystem_type_nsprefix_ + ':' if (UseCapturedNS_ and self.codesystem_type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodesystem_type>%s</%scodesystem_type>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codesystem_type), input_name='codesystem_type')), namespaceprefix_ , eol_))
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.name is not None:
            json_dict['name'] = self.name
        if self.dosis is not None:
            json_dict['dosis'] = self.dosis
        if self.beginn is not None:
            json_dict['beginn'] = self.beginn
        if self.status is not None:
            json_dict['status'] = self.status
        if self.code is not None:
            json_dict['code'] = self.code
        if self.codesystem is not None:
            json_dict['codesystem'] = self.codesystem
        if self.codesystem_type is not None:
            json_dict['codesystem_type'] = self.codesystem_type
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
        elif nodeName_ == 'dosis':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'dosis')
            value_ = self.gds_validate_string(value_, node, 'dosis')
            self.dosis = value_
            self.dosis_nsprefix_ = child_.prefix
        elif nodeName_ == 'beginn':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'beginn')
            value_ = self.gds_validate_string(value_, node, 'beginn')
            self.beginn = value_
            self.beginn_nsprefix_ = child_.prefix
        elif nodeName_ == 'status':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'status')
            value_ = self.gds_validate_string(value_, node, 'status')
            self.status = value_
            self.status_nsprefix_ = child_.prefix
        elif nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
        elif nodeName_ == 'codesystem':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codesystem')
            value_ = self.gds_validate_string(value_, node, 'codesystem')
            self.codesystem = value_
            self.codesystem_nsprefix_ = child_.prefix
        elif nodeName_ == 'codesystem_type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codesystem_type')
            value_ = self.gds_validate_string(value_, node, 'codesystem_type')
            self.codesystem_type = value_
            self.codesystem_type_nsprefix_ = child_.prefix
# end class dataType3


class v_allergies_dataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, movableColumns: 'boolean' = False, data: List_['dataType4'] = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.movableColumns = movableColumns
        self.movableColumns_nsprefix_ = None
        if data is None:
            self.data = []
        else:
            self.data = data
        self.data_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, v_allergies_dataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if v_allergies_dataType.subclass:
            return v_allergies_dataType.subclass(*args_, **kwargs_)
        else:
            return v_allergies_dataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_movableColumns(self):
        return self.movableColumns
    def set_movableColumns(self, movableColumns):
        self.movableColumns = movableColumns
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def add_data(self, value):
        self.data.append(value)
    def insert_data_at(self, index, value):
        self.data.insert(index, value)
    def replace_data_at(self, index, value):
        self.data[index] = value
    def has__content(self):
        if (
            self.movableColumns or
            self.data
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='v_allergies_dataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('v_allergies_dataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'v_allergies_dataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='v_allergies_dataType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='v_allergies_dataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='v_allergies_dataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='v_allergies_dataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.movableColumns is not None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>%s</%smovableColumns>%s' % (namespaceprefix_ , self.gds_format_boolean(self.movableColumns, input_name='movableColumns'), namespaceprefix_ , eol_))
        if self.movableColumns is None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>false</%smovableColumns/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        for data_ in self.data:
            namespaceprefix_ = self.data_nsprefix_ + ':' if (UseCapturedNS_ and self.data_nsprefix_) else ''
            data_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='data', pretty_print=pretty_print)
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.movableColumns is not None:
            json_dict['movableColumns'] = self.movableColumns
        child_list = []
        for child in self.data:
            child_dict = child.exportJson(json_dict, 'data', True)
            if child_dict:
                child_list.append(child_dict)
        if child_list:
            json_dict['data'] = child_list
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'movableColumns':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'movableColumns')
            ival_ = self.gds_validate_boolean(ival_, node, 'movableColumns')
            self.movableColumns = ival_
            self.movableColumns_nsprefix_ = child_.prefix
        elif nodeName_ == 'data':
            obj_ = dataType4.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.data.append(obj_)
            obj_.original_tagname_ = 'data'
# end class v_allergies_dataType


class dataType4(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, allergien: 'string' = 'Keine Allergien bekannt', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.allergien = allergien
        self.allergien_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dataType4)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dataType4.subclass:
            return dataType4.subclass(*args_, **kwargs_)
        else:
            return dataType4(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_allergien(self):
        return self.allergien
    def set_allergien(self, allergien):
        self.allergien = allergien
    def has__content(self):
        if (
            self.allergien != "Keine Allergien bekannt"
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType4', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dataType4')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dataType4':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dataType4')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dataType4', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dataType4'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType4', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.allergien is not None:
            namespaceprefix_ = self.allergien_nsprefix_ + ':' if (UseCapturedNS_ and self.allergien_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sallergien>%s</%sallergien>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.allergien), input_name='allergien')), namespaceprefix_ , eol_))
        if self.allergien is None:
            namespaceprefix_ = self.allergien_nsprefix_ + ':' if (UseCapturedNS_ and self.allergien_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sallergien>Keine Allergien bekannt</%sallergien/>%s' % (namespaceprefix_,namespace_prefix, eol_))
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.allergien is not None:
            json_dict['allergien'] = self.allergien
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'allergien':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'allergien')
            value_ = self.gds_validate_string(value_, node, 'allergien')
            self.allergien = value_
            self.allergien_nsprefix_ = child_.prefix
# end class dataType4


class i_allergies_dataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, movableColumns: 'boolean' = True, data: List_['dataType5'] = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.movableColumns = movableColumns
        self.movableColumns_nsprefix_ = None
        if data is None:
            self.data = []
        else:
            self.data = data
        self.data_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, i_allergies_dataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if i_allergies_dataType.subclass:
            return i_allergies_dataType.subclass(*args_, **kwargs_)
        else:
            return i_allergies_dataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_movableColumns(self):
        return self.movableColumns
    def set_movableColumns(self, movableColumns):
        self.movableColumns = movableColumns
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def add_data(self, value):
        self.data.append(value)
    def insert_data_at(self, index, value):
        self.data.insert(index, value)
    def replace_data_at(self, index, value):
        self.data[index] = value
    def has__content(self):
        if (
            not self.movableColumns or
            self.data
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='i_allergies_dataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('i_allergies_dataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'i_allergies_dataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='i_allergies_dataType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='i_allergies_dataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='i_allergies_dataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='i_allergies_dataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.movableColumns is not None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>%s</%smovableColumns>%s' % (namespaceprefix_ , self.gds_format_boolean(self.movableColumns, input_name='movableColumns'), namespaceprefix_ , eol_))
        if self.movableColumns is None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>true</%smovableColumns/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        for data_ in self.data:
            namespaceprefix_ = self.data_nsprefix_ + ':' if (UseCapturedNS_ and self.data_nsprefix_) else ''
            data_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='data', pretty_print=pretty_print)
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.movableColumns is not None:
            json_dict['movableColumns'] = self.movableColumns
        child_list = []
        for child in self.data:
            child_dict = child.exportJson(json_dict, 'data', True)
            if child_dict:
                child_list.append(child_dict)
        if child_list:
            json_dict['data'] = child_list
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'movableColumns':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'movableColumns')
            ival_ = self.gds_validate_boolean(ival_, node, 'movableColumns')
            self.movableColumns = ival_
            self.movableColumns_nsprefix_ = child_.prefix
        elif nodeName_ == 'data':
            obj_ = dataType5.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.data.append(obj_)
            obj_.original_tagname_ = 'data'
# end class i_allergies_dataType


class dataType5(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, allergien: 'string' = 'Keine Allergien bekannt', aktivitaet: 'string' = None, code: 'string' = None, codesystem: 'string' = None, codesystem_type: 'string' = None, marked: 'string' = None, marked2: 'string' = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.allergien = allergien
        self.allergien_nsprefix_ = None
        self.aktivitaet = aktivitaet
        self.aktivitaet_nsprefix_ = None
        self.code = code
        self.code_nsprefix_ = None
        self.codesystem = codesystem
        self.codesystem_nsprefix_ = None
        self.codesystem_type = codesystem_type
        self.codesystem_type_nsprefix_ = None
        self.marked = marked
        self.marked_nsprefix_ = None
        self.marked2 = marked2
        self.marked2_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dataType5)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dataType5.subclass:
            return dataType5.subclass(*args_, **kwargs_)
        else:
            return dataType5(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_allergien(self):
        return self.allergien
    def set_allergien(self, allergien):
        self.allergien = allergien
    def get_aktivitaet(self):
        return self.aktivitaet
    def set_aktivitaet(self, aktivitaet):
        self.aktivitaet = aktivitaet
    def get_code(self):
        return self.code
    def set_code(self, code):
        self.code = code
    def get_codesystem(self):
        return self.codesystem
    def set_codesystem(self, codesystem):
        self.codesystem = codesystem
    def get_codesystem_type(self):
        return self.codesystem_type
    def set_codesystem_type(self, codesystem_type):
        self.codesystem_type = codesystem_type
    def get_marked(self):
        return self.marked
    def set_marked(self, marked):
        self.marked = marked
    def get_marked2(self):
        return self.marked2
    def set_marked2(self, marked2):
        self.marked2 = marked2
    def has__content(self):
        if (
            self.allergien != "Keine Allergien bekannt" or
            self.aktivitaet is not None or
            self.code is not None or
            self.codesystem is not None or
            self.codesystem_type is not None or
            self.marked is not None or
            self.marked2 is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType5', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dataType5')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dataType5':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dataType5')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dataType5', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dataType5'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType5', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.allergien is not None:
            namespaceprefix_ = self.allergien_nsprefix_ + ':' if (UseCapturedNS_ and self.allergien_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sallergien>%s</%sallergien>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.allergien), input_name='allergien')), namespaceprefix_ , eol_))
        if self.allergien is None:
            namespaceprefix_ = self.allergien_nsprefix_ + ':' if (UseCapturedNS_ and self.allergien_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sallergien>Keine Allergien bekannt</%sallergien/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.aktivitaet is not None:
            namespaceprefix_ = self.aktivitaet_nsprefix_ + ':' if (UseCapturedNS_ and self.aktivitaet_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%saktivitaet>%s</%saktivitaet>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.aktivitaet), input_name='aktivitaet')), namespaceprefix_ , eol_))
        if self.code is not None:
            namespaceprefix_ = self.code_nsprefix_ + ':' if (UseCapturedNS_ and self.code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scode>%s</%scode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.code), input_name='code')), namespaceprefix_ , eol_))
        if self.codesystem is not None:
            namespaceprefix_ = self.codesystem_nsprefix_ + ':' if (UseCapturedNS_ and self.codesystem_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodesystem>%s</%scodesystem>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codesystem), input_name='codesystem')), namespaceprefix_ , eol_))
        if self.codesystem_type is not None:
            namespaceprefix_ = self.codesystem_type_nsprefix_ + ':' if (UseCapturedNS_ and self.codesystem_type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodesystem_type>%s</%scodesystem_type>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codesystem_type), input_name='codesystem_type')), namespaceprefix_ , eol_))
        if self.marked is not None:
            namespaceprefix_ = self.marked_nsprefix_ + ':' if (UseCapturedNS_ and self.marked_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smarked>%s</%smarked>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.marked), input_name='marked')), namespaceprefix_ , eol_))
        if self.marked2 is not None:
            namespaceprefix_ = self.marked2_nsprefix_ + ':' if (UseCapturedNS_ and self.marked2_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smarked2>%s</%smarked2>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.marked2), input_name='marked2')), namespaceprefix_ , eol_))
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.allergien is not None:
            json_dict['allergien'] = self.allergien
        if self.aktivitaet is not None:
            json_dict['aktivitaet'] = self.aktivitaet
        if self.code is not None:
            json_dict['code'] = self.code
        if self.codesystem is not None:
            json_dict['codesystem'] = self.codesystem
        if self.codesystem_type is not None:
            json_dict['codesystem_type'] = self.codesystem_type
        if self.marked is not None:
            json_dict['marked'] = self.marked
        if self.marked2 is not None:
            json_dict['marked2'] = self.marked2
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'allergien':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'allergien')
            value_ = self.gds_validate_string(value_, node, 'allergien')
            self.allergien = value_
            self.allergien_nsprefix_ = child_.prefix
        elif nodeName_ == 'aktivitaet':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'aktivitaet')
            value_ = self.gds_validate_string(value_, node, 'aktivitaet')
            self.aktivitaet = value_
            self.aktivitaet_nsprefix_ = child_.prefix
        elif nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
        elif nodeName_ == 'codesystem':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codesystem')
            value_ = self.gds_validate_string(value_, node, 'codesystem')
            self.codesystem = value_
            self.codesystem_nsprefix_ = child_.prefix
        elif nodeName_ == 'codesystem_type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codesystem_type')
            value_ = self.gds_validate_string(value_, node, 'codesystem_type')
            self.codesystem_type = value_
            self.codesystem_type_nsprefix_ = child_.prefix
        elif nodeName_ == 'marked':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'marked')
            value_ = self.gds_validate_string(value_, node, 'marked')
            self.marked = value_
            self.marked_nsprefix_ = child_.prefix
        elif nodeName_ == 'marked2':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'marked2')
            value_ = self.gds_validate_string(value_, node, 'marked2')
            self.marked2 = value_
            self.marked2_nsprefix_ = child_.prefix
# end class dataType5


class v_current_problems_dataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, movableColumns: 'boolean' = False, data: List_['dataType6'] = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.movableColumns = movableColumns
        self.movableColumns_nsprefix_ = None
        if data is None:
            self.data = []
        else:
            self.data = data
        self.data_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, v_current_problems_dataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if v_current_problems_dataType.subclass:
            return v_current_problems_dataType.subclass(*args_, **kwargs_)
        else:
            return v_current_problems_dataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_movableColumns(self):
        return self.movableColumns
    def set_movableColumns(self, movableColumns):
        self.movableColumns = movableColumns
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def add_data(self, value):
        self.data.append(value)
    def insert_data_at(self, index, value):
        self.data.insert(index, value)
    def replace_data_at(self, index, value):
        self.data[index] = value
    def has__content(self):
        if (
            self.movableColumns or
            self.data
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='v_current_problems_dataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('v_current_problems_dataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'v_current_problems_dataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='v_current_problems_dataType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='v_current_problems_dataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='v_current_problems_dataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='v_current_problems_dataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.movableColumns is not None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>%s</%smovableColumns>%s' % (namespaceprefix_ , self.gds_format_boolean(self.movableColumns, input_name='movableColumns'), namespaceprefix_ , eol_))
        if self.movableColumns is None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>false</%smovableColumns/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        for data_ in self.data:
            namespaceprefix_ = self.data_nsprefix_ + ':' if (UseCapturedNS_ and self.data_nsprefix_) else ''
            data_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='data', pretty_print=pretty_print)
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.movableColumns is not None:
            json_dict['movableColumns'] = self.movableColumns
        child_list = []
        for child in self.data:
            child_dict = child.exportJson(json_dict, 'data', True)
            if child_dict:
                child_list.append(child_dict)
        if child_list:
            json_dict['data'] = child_list
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'movableColumns':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'movableColumns')
            ival_ = self.gds_validate_boolean(ival_, node, 'movableColumns')
            self.movableColumns = ival_
            self.movableColumns_nsprefix_ = child_.prefix
        elif nodeName_ == 'data':
            obj_ = dataType6.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.data.append(obj_)
            obj_.original_tagname_ = 'data'
# end class v_current_problems_dataType


class dataType6(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, diagnose: 'string' = 'Keine aktuellen Diagnosen bekannt', erklaerung: List_['erklaerungType'] = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.diagnose = diagnose
        self.diagnose_nsprefix_ = None
        if erklaerung is None:
            self.erklaerung = []
        else:
            self.erklaerung = erklaerung
        self.erklaerung_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dataType6)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dataType6.subclass:
            return dataType6.subclass(*args_, **kwargs_)
        else:
            return dataType6(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_diagnose(self):
        return self.diagnose
    def set_diagnose(self, diagnose):
        self.diagnose = diagnose
    def get_erklaerung(self):
        return self.erklaerung
    def set_erklaerung(self, erklaerung):
        self.erklaerung = erklaerung
    def add_erklaerung(self, value):
        self.erklaerung.append(value)
    def insert_erklaerung_at(self, index, value):
        self.erklaerung.insert(index, value)
    def replace_erklaerung_at(self, index, value):
        self.erklaerung[index] = value
    def has__content(self):
        if (
            self.diagnose != "Keine aktuellen Diagnosen bekannt" or
            self.erklaerung
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType6', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dataType6')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dataType6':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dataType6')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dataType6', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dataType6'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType6', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.diagnose is not None:
            namespaceprefix_ = self.diagnose_nsprefix_ + ':' if (UseCapturedNS_ and self.diagnose_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdiagnose>%s</%sdiagnose>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.diagnose), input_name='diagnose')), namespaceprefix_ , eol_))
        if self.diagnose is None:
            namespaceprefix_ = self.diagnose_nsprefix_ + ':' if (UseCapturedNS_ and self.diagnose_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdiagnose>Keine aktuellen Diagnosen bekannt</%sdiagnose/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        for erklaerung_ in self.erklaerung:
            namespaceprefix_ = self.erklaerung_nsprefix_ + ':' if (UseCapturedNS_ and self.erklaerung_nsprefix_) else ''
            erklaerung_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='erklaerung', pretty_print=pretty_print)
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.diagnose is not None:
            json_dict['diagnose'] = self.diagnose
        child_list = []
        for child in self.erklaerung:
            child_dict = child.exportJson(json_dict, 'erklaerung', True)
            if child_dict:
                child_list.append(child_dict)
        if child_list:
            json_dict['erklaerung'] = child_list
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'diagnose':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'diagnose')
            value_ = self.gds_validate_string(value_, node, 'diagnose')
            self.diagnose = value_
            self.diagnose_nsprefix_ = child_.prefix
        elif nodeName_ == 'erklaerung':
            obj_ = erklaerungType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.erklaerung.append(obj_)
            obj_.original_tagname_ = 'erklaerung'
# end class dataType6


class erklaerungType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, url: 'string' = None, label: 'string' = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.url = url
        self.url_nsprefix_ = None
        self.label = label
        self.label_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, erklaerungType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if erklaerungType.subclass:
            return erklaerungType.subclass(*args_, **kwargs_)
        else:
            return erklaerungType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_url(self):
        return self.url
    def set_url(self, url):
        self.url = url
    def get_label(self):
        return self.label
    def set_label(self, label):
        self.label = label
    def has__content(self):
        if (
            self.url is not None or
            self.label is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='erklaerungType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('erklaerungType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'erklaerungType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='erklaerungType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='erklaerungType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='erklaerungType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='erklaerungType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.url is not None:
            namespaceprefix_ = self.url_nsprefix_ + ':' if (UseCapturedNS_ and self.url_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%surl>%s</%surl>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.url), input_name='url')), namespaceprefix_ , eol_))
        if self.label is not None:
            namespaceprefix_ = self.label_nsprefix_ + ':' if (UseCapturedNS_ and self.label_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slabel>%s</%slabel>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.label), input_name='label')), namespaceprefix_ , eol_))
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.url is not None:
            json_dict['url'] = self.url
        if self.label is not None:
            json_dict['label'] = self.label
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'url':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'url')
            value_ = self.gds_validate_string(value_, node, 'url')
            self.url = value_
            self.url_nsprefix_ = child_.prefix
        elif nodeName_ == 'label':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'label')
            value_ = self.gds_validate_string(value_, node, 'label')
            self.label = value_
            self.label_nsprefix_ = child_.prefix
# end class erklaerungType


class i_current_problems_dataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, movableColumns: 'boolean' = True, data: List_['dataType7'] = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.movableColumns = movableColumns
        self.movableColumns_nsprefix_ = None
        if data is None:
            self.data = []
        else:
            self.data = data
        self.data_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, i_current_problems_dataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if i_current_problems_dataType.subclass:
            return i_current_problems_dataType.subclass(*args_, **kwargs_)
        else:
            return i_current_problems_dataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_movableColumns(self):
        return self.movableColumns
    def set_movableColumns(self, movableColumns):
        self.movableColumns = movableColumns
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def add_data(self, value):
        self.data.append(value)
    def insert_data_at(self, index, value):
        self.data.insert(index, value)
    def replace_data_at(self, index, value):
        self.data[index] = value
    def has__content(self):
        if (
            not self.movableColumns or
            self.data
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='i_current_problems_dataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('i_current_problems_dataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'i_current_problems_dataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='i_current_problems_dataType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='i_current_problems_dataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='i_current_problems_dataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='i_current_problems_dataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.movableColumns is not None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>%s</%smovableColumns>%s' % (namespaceprefix_ , self.gds_format_boolean(self.movableColumns, input_name='movableColumns'), namespaceprefix_ , eol_))
        if self.movableColumns is None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>true</%smovableColumns/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        for data_ in self.data:
            namespaceprefix_ = self.data_nsprefix_ + ':' if (UseCapturedNS_ and self.data_nsprefix_) else ''
            data_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='data', pretty_print=pretty_print)
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.movableColumns is not None:
            json_dict['movableColumns'] = self.movableColumns
        child_list = []
        for child in self.data:
            child_dict = child.exportJson(json_dict, 'data', True)
            if child_dict:
                child_list.append(child_dict)
        if child_list:
            json_dict['data'] = child_list
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'movableColumns':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'movableColumns')
            ival_ = self.gds_validate_boolean(ival_, node, 'movableColumns')
            self.movableColumns = ival_
            self.movableColumns_nsprefix_ = child_.prefix
        elif nodeName_ == 'data':
            obj_ = dataType7.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.data.append(obj_)
            obj_.original_tagname_ = 'data'
# end class i_current_problems_dataType


class dataType7(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, diagnose: 'string' = 'Keine aktuellen Diagnosen bekannt', code: 'string' = None, codesystem: 'anyURI' = None, status: 'string' = None, verifizierung: 'string' = None, codesystem_type: 'string' = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.diagnose = diagnose
        self.diagnose_nsprefix_ = None
        self.code = code
        self.code_nsprefix_ = None
        self.codesystem = codesystem
        self.codesystem_nsprefix_ = None
        self.status = status
        self.status_nsprefix_ = None
        self.verifizierung = verifizierung
        self.verifizierung_nsprefix_ = None
        self.codesystem_type = codesystem_type
        self.codesystem_type_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dataType7)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dataType7.subclass:
            return dataType7.subclass(*args_, **kwargs_)
        else:
            return dataType7(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_diagnose(self):
        return self.diagnose
    def set_diagnose(self, diagnose):
        self.diagnose = diagnose
    def get_code(self):
        return self.code
    def set_code(self, code):
        self.code = code
    def get_codesystem(self):
        return self.codesystem
    def set_codesystem(self, codesystem):
        self.codesystem = codesystem
    def get_status(self):
        return self.status
    def set_status(self, status):
        self.status = status
    def get_verifizierung(self):
        return self.verifizierung
    def set_verifizierung(self, verifizierung):
        self.verifizierung = verifizierung
    def get_codesystem_type(self):
        return self.codesystem_type
    def set_codesystem_type(self, codesystem_type):
        self.codesystem_type = codesystem_type
    def has__content(self):
        if (
            self.diagnose != "Keine aktuellen Diagnosen bekannt" or
            self.code is not None or
            self.codesystem is not None or
            self.status is not None or
            self.verifizierung is not None or
            self.codesystem_type is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType7', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dataType7')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dataType7':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dataType7')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dataType7', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dataType7'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType7', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.diagnose is not None:
            namespaceprefix_ = self.diagnose_nsprefix_ + ':' if (UseCapturedNS_ and self.diagnose_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdiagnose>%s</%sdiagnose>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.diagnose), input_name='diagnose')), namespaceprefix_ , eol_))
        if self.diagnose is None:
            namespaceprefix_ = self.diagnose_nsprefix_ + ':' if (UseCapturedNS_ and self.diagnose_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdiagnose>Keine aktuellen Diagnosen bekannt</%sdiagnose/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.code is not None:
            namespaceprefix_ = self.code_nsprefix_ + ':' if (UseCapturedNS_ and self.code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scode>%s</%scode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.code), input_name='code')), namespaceprefix_ , eol_))
        if self.codesystem is not None:
            namespaceprefix_ = self.codesystem_nsprefix_ + ':' if (UseCapturedNS_ and self.codesystem_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodesystem>%s</%scodesystem>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codesystem), input_name='codesystem')), namespaceprefix_ , eol_))
        if self.status is not None:
            namespaceprefix_ = self.status_nsprefix_ + ':' if (UseCapturedNS_ and self.status_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstatus>%s</%sstatus>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.status), input_name='status')), namespaceprefix_ , eol_))
        if self.verifizierung is not None:
            namespaceprefix_ = self.verifizierung_nsprefix_ + ':' if (UseCapturedNS_ and self.verifizierung_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sverifizierung>%s</%sverifizierung>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.verifizierung), input_name='verifizierung')), namespaceprefix_ , eol_))
        if self.codesystem_type is not None:
            namespaceprefix_ = self.codesystem_type_nsprefix_ + ':' if (UseCapturedNS_ and self.codesystem_type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodesystem_type>%s</%scodesystem_type>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codesystem_type), input_name='codesystem_type')), namespaceprefix_ , eol_))
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.diagnose is not None:
            json_dict['diagnose'] = self.diagnose
        if self.code is not None:
            json_dict['code'] = self.code
        if self.codesystem is not None:
            json_dict['codesystem'] = self.codesystem
        if self.status is not None:
            json_dict['status'] = self.status
        if self.verifizierung is not None:
            json_dict['verifizierung'] = self.verifizierung
        if self.codesystem_type is not None:
            json_dict['codesystem_type'] = self.codesystem_type
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'diagnose':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'diagnose')
            value_ = self.gds_validate_string(value_, node, 'diagnose')
            self.diagnose = value_
            self.diagnose_nsprefix_ = child_.prefix
        elif nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
        elif nodeName_ == 'codesystem':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codesystem')
            value_ = self.gds_validate_string(value_, node, 'codesystem')
            self.codesystem = value_
            self.codesystem_nsprefix_ = child_.prefix
        elif nodeName_ == 'status':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'status')
            value_ = self.gds_validate_string(value_, node, 'status')
            self.status = value_
            self.status_nsprefix_ = child_.prefix
        elif nodeName_ == 'verifizierung':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'verifizierung')
            value_ = self.gds_validate_string(value_, node, 'verifizierung')
            self.verifizierung = value_
            self.verifizierung_nsprefix_ = child_.prefix
        elif nodeName_ == 'codesystem_type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codesystem_type')
            value_ = self.gds_validate_string(value_, node, 'codesystem_type')
            self.codesystem_type = value_
            self.codesystem_type_nsprefix_ = child_.prefix
# end class dataType7


class v_past_problems_dataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, movableColumns: 'boolean' = False, data: List_['dataType8'] = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.movableColumns = movableColumns
        self.movableColumns_nsprefix_ = None
        if data is None:
            self.data = []
        else:
            self.data = data
        self.data_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, v_past_problems_dataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if v_past_problems_dataType.subclass:
            return v_past_problems_dataType.subclass(*args_, **kwargs_)
        else:
            return v_past_problems_dataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_movableColumns(self):
        return self.movableColumns
    def set_movableColumns(self, movableColumns):
        self.movableColumns = movableColumns
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def add_data(self, value):
        self.data.append(value)
    def insert_data_at(self, index, value):
        self.data.insert(index, value)
    def replace_data_at(self, index, value):
        self.data[index] = value
    def has__content(self):
        if (
            self.movableColumns or
            self.data
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='v_past_problems_dataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('v_past_problems_dataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'v_past_problems_dataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='v_past_problems_dataType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='v_past_problems_dataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='v_past_problems_dataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='v_past_problems_dataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.movableColumns is not None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>%s</%smovableColumns>%s' % (namespaceprefix_ , self.gds_format_boolean(self.movableColumns, input_name='movableColumns'), namespaceprefix_ , eol_))
        if self.movableColumns is None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>false</%smovableColumns/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        for data_ in self.data:
            namespaceprefix_ = self.data_nsprefix_ + ':' if (UseCapturedNS_ and self.data_nsprefix_) else ''
            data_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='data', pretty_print=pretty_print)
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.movableColumns is not None:
            json_dict['movableColumns'] = self.movableColumns
        child_list = []
        for child in self.data:
            child_dict = child.exportJson(json_dict, 'data', True)
            if child_dict:
                child_list.append(child_dict)
        if child_list:
            json_dict['data'] = child_list
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'movableColumns':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'movableColumns')
            ival_ = self.gds_validate_boolean(ival_, node, 'movableColumns')
            self.movableColumns = ival_
            self.movableColumns_nsprefix_ = child_.prefix
        elif nodeName_ == 'data':
            obj_ = dataType8.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.data.append(obj_)
            obj_.original_tagname_ = 'data'
# end class v_past_problems_dataType


class dataType8(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, diagnose: 'string' = 'Keine vergangenen Diagnosen bekannt', erklaerung: List_['erklaerungType9'] = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.diagnose = diagnose
        self.diagnose_nsprefix_ = None
        if erklaerung is None:
            self.erklaerung = []
        else:
            self.erklaerung = erklaerung
        self.erklaerung_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dataType8)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dataType8.subclass:
            return dataType8.subclass(*args_, **kwargs_)
        else:
            return dataType8(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_diagnose(self):
        return self.diagnose
    def set_diagnose(self, diagnose):
        self.diagnose = diagnose
    def get_erklaerung(self):
        return self.erklaerung
    def set_erklaerung(self, erklaerung):
        self.erklaerung = erklaerung
    def add_erklaerung(self, value):
        self.erklaerung.append(value)
    def insert_erklaerung_at(self, index, value):
        self.erklaerung.insert(index, value)
    def replace_erklaerung_at(self, index, value):
        self.erklaerung[index] = value
    def has__content(self):
        if (
            self.diagnose != "Keine vergangenen Diagnosen bekannt" or
            self.erklaerung
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType8', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dataType8')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dataType8':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dataType8')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dataType8', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dataType8'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType8', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.diagnose is not None:
            namespaceprefix_ = self.diagnose_nsprefix_ + ':' if (UseCapturedNS_ and self.diagnose_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdiagnose>%s</%sdiagnose>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.diagnose), input_name='diagnose')), namespaceprefix_ , eol_))
        if self.diagnose is None:
            namespaceprefix_ = self.diagnose_nsprefix_ + ':' if (UseCapturedNS_ and self.diagnose_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdiagnose>Keine vergangenen Diagnosen bekannt</%sdiagnose/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        for erklaerung_ in self.erklaerung:
            namespaceprefix_ = self.erklaerung_nsprefix_ + ':' if (UseCapturedNS_ and self.erklaerung_nsprefix_) else ''
            erklaerung_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='erklaerung', pretty_print=pretty_print)
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.diagnose is not None:
            json_dict['diagnose'] = self.diagnose
        child_list = []
        for child in self.erklaerung:
            child_dict = child.exportJson(json_dict, 'erklaerung', True)
            if child_dict:
                child_list.append(child_dict)
        if child_list:
            json_dict['erklaerung'] = child_list
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'diagnose':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'diagnose')
            value_ = self.gds_validate_string(value_, node, 'diagnose')
            self.diagnose = value_
            self.diagnose_nsprefix_ = child_.prefix
        elif nodeName_ == 'erklaerung':
            obj_ = erklaerungType9.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.erklaerung.append(obj_)
            obj_.original_tagname_ = 'erklaerung'
# end class dataType8


class erklaerungType9(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, url: 'string' = None, label: 'string' = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.url = url
        self.url_nsprefix_ = None
        self.label = label
        self.label_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, erklaerungType9)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if erklaerungType9.subclass:
            return erklaerungType9.subclass(*args_, **kwargs_)
        else:
            return erklaerungType9(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_url(self):
        return self.url
    def set_url(self, url):
        self.url = url
    def get_label(self):
        return self.label
    def set_label(self, label):
        self.label = label
    def has__content(self):
        if (
            self.url is not None or
            self.label is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='erklaerungType9', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('erklaerungType9')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'erklaerungType9':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='erklaerungType9')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='erklaerungType9', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='erklaerungType9'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='erklaerungType9', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.url is not None:
            namespaceprefix_ = self.url_nsprefix_ + ':' if (UseCapturedNS_ and self.url_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%surl>%s</%surl>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.url), input_name='url')), namespaceprefix_ , eol_))
        if self.label is not None:
            namespaceprefix_ = self.label_nsprefix_ + ':' if (UseCapturedNS_ and self.label_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slabel>%s</%slabel>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.label), input_name='label')), namespaceprefix_ , eol_))
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.url is not None:
            json_dict['url'] = self.url
        if self.label is not None:
            json_dict['label'] = self.label
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'url':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'url')
            value_ = self.gds_validate_string(value_, node, 'url')
            self.url = value_
            self.url_nsprefix_ = child_.prefix
        elif nodeName_ == 'label':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'label')
            value_ = self.gds_validate_string(value_, node, 'label')
            self.label = value_
            self.label_nsprefix_ = child_.prefix
# end class erklaerungType9


class i_past_problems_dataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, movableColumns: 'boolean' = True, data: List_['dataType10'] = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.movableColumns = movableColumns
        self.movableColumns_nsprefix_ = None
        if data is None:
            self.data = []
        else:
            self.data = data
        self.data_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, i_past_problems_dataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if i_past_problems_dataType.subclass:
            return i_past_problems_dataType.subclass(*args_, **kwargs_)
        else:
            return i_past_problems_dataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_movableColumns(self):
        return self.movableColumns
    def set_movableColumns(self, movableColumns):
        self.movableColumns = movableColumns
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def add_data(self, value):
        self.data.append(value)
    def insert_data_at(self, index, value):
        self.data.insert(index, value)
    def replace_data_at(self, index, value):
        self.data[index] = value
    def has__content(self):
        if (
            not self.movableColumns or
            self.data
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='i_past_problems_dataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('i_past_problems_dataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'i_past_problems_dataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='i_past_problems_dataType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='i_past_problems_dataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='i_past_problems_dataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='i_past_problems_dataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.movableColumns is not None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>%s</%smovableColumns>%s' % (namespaceprefix_ , self.gds_format_boolean(self.movableColumns, input_name='movableColumns'), namespaceprefix_ , eol_))
        if self.movableColumns is None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>true</%smovableColumns/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        for data_ in self.data:
            namespaceprefix_ = self.data_nsprefix_ + ':' if (UseCapturedNS_ and self.data_nsprefix_) else ''
            data_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='data', pretty_print=pretty_print)
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.movableColumns is not None:
            json_dict['movableColumns'] = self.movableColumns
        child_list = []
        for child in self.data:
            child_dict = child.exportJson(json_dict, 'data', True)
            if child_dict:
                child_list.append(child_dict)
        if child_list:
            json_dict['data'] = child_list
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'movableColumns':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'movableColumns')
            ival_ = self.gds_validate_boolean(ival_, node, 'movableColumns')
            self.movableColumns = ival_
            self.movableColumns_nsprefix_ = child_.prefix
        elif nodeName_ == 'data':
            obj_ = dataType10.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.data.append(obj_)
            obj_.original_tagname_ = 'data'
# end class i_past_problems_dataType


class dataType10(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, diagnose: 'string' = 'Keine vergangenen Diagnosen bekannt', code: 'string' = None, codesystem: 'anyURI' = None, status: 'string' = None, verifizierung: 'string' = None, codesystem_type: 'string' = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.diagnose = diagnose
        self.diagnose_nsprefix_ = None
        self.code = code
        self.code_nsprefix_ = None
        self.codesystem = codesystem
        self.codesystem_nsprefix_ = None
        self.status = status
        self.status_nsprefix_ = None
        self.verifizierung = verifizierung
        self.verifizierung_nsprefix_ = None
        self.codesystem_type = codesystem_type
        self.codesystem_type_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dataType10)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dataType10.subclass:
            return dataType10.subclass(*args_, **kwargs_)
        else:
            return dataType10(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_diagnose(self):
        return self.diagnose
    def set_diagnose(self, diagnose):
        self.diagnose = diagnose
    def get_code(self):
        return self.code
    def set_code(self, code):
        self.code = code
    def get_codesystem(self):
        return self.codesystem
    def set_codesystem(self, codesystem):
        self.codesystem = codesystem
    def get_status(self):
        return self.status
    def set_status(self, status):
        self.status = status
    def get_verifizierung(self):
        return self.verifizierung
    def set_verifizierung(self, verifizierung):
        self.verifizierung = verifizierung
    def get_codesystem_type(self):
        return self.codesystem_type
    def set_codesystem_type(self, codesystem_type):
        self.codesystem_type = codesystem_type
    def has__content(self):
        if (
            self.diagnose != "Keine vergangenen Diagnosen bekannt" or
            self.code is not None or
            self.codesystem is not None or
            self.status is not None or
            self.verifizierung is not None or
            self.codesystem_type is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType10', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dataType10')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dataType10':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dataType10')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dataType10', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dataType10'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType10', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.diagnose is not None:
            namespaceprefix_ = self.diagnose_nsprefix_ + ':' if (UseCapturedNS_ and self.diagnose_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdiagnose>%s</%sdiagnose>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.diagnose), input_name='diagnose')), namespaceprefix_ , eol_))
        if self.diagnose is None:
            namespaceprefix_ = self.diagnose_nsprefix_ + ':' if (UseCapturedNS_ and self.diagnose_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdiagnose>Keine vergangenen Diagnosen bekannt</%sdiagnose/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.code is not None:
            namespaceprefix_ = self.code_nsprefix_ + ':' if (UseCapturedNS_ and self.code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scode>%s</%scode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.code), input_name='code')), namespaceprefix_ , eol_))
        if self.codesystem is not None:
            namespaceprefix_ = self.codesystem_nsprefix_ + ':' if (UseCapturedNS_ and self.codesystem_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodesystem>%s</%scodesystem>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codesystem), input_name='codesystem')), namespaceprefix_ , eol_))
        if self.status is not None:
            namespaceprefix_ = self.status_nsprefix_ + ':' if (UseCapturedNS_ and self.status_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstatus>%s</%sstatus>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.status), input_name='status')), namespaceprefix_ , eol_))
        if self.verifizierung is not None:
            namespaceprefix_ = self.verifizierung_nsprefix_ + ':' if (UseCapturedNS_ and self.verifizierung_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sverifizierung>%s</%sverifizierung>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.verifizierung), input_name='verifizierung')), namespaceprefix_ , eol_))
        if self.codesystem_type is not None:
            namespaceprefix_ = self.codesystem_type_nsprefix_ + ':' if (UseCapturedNS_ and self.codesystem_type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodesystem_type>%s</%scodesystem_type>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codesystem_type), input_name='codesystem_type')), namespaceprefix_ , eol_))
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.diagnose is not None:
            json_dict['diagnose'] = self.diagnose
        if self.code is not None:
            json_dict['code'] = self.code
        if self.codesystem is not None:
            json_dict['codesystem'] = self.codesystem
        if self.status is not None:
            json_dict['status'] = self.status
        if self.verifizierung is not None:
            json_dict['verifizierung'] = self.verifizierung
        if self.codesystem_type is not None:
            json_dict['codesystem_type'] = self.codesystem_type
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'diagnose':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'diagnose')
            value_ = self.gds_validate_string(value_, node, 'diagnose')
            self.diagnose = value_
            self.diagnose_nsprefix_ = child_.prefix
        elif nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
        elif nodeName_ == 'codesystem':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codesystem')
            value_ = self.gds_validate_string(value_, node, 'codesystem')
            self.codesystem = value_
            self.codesystem_nsprefix_ = child_.prefix
        elif nodeName_ == 'status':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'status')
            value_ = self.gds_validate_string(value_, node, 'status')
            self.status = value_
            self.status_nsprefix_ = child_.prefix
        elif nodeName_ == 'verifizierung':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'verifizierung')
            value_ = self.gds_validate_string(value_, node, 'verifizierung')
            self.verifizierung = value_
            self.verifizierung_nsprefix_ = child_.prefix
        elif nodeName_ == 'codesystem_type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codesystem_type')
            value_ = self.gds_validate_string(value_, node, 'codesystem_type')
            self.codesystem_type = value_
            self.codesystem_type_nsprefix_ = child_.prefix
# end class dataType10


class v_family_problems_dataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, movableColumns: 'boolean' = False, data: List_['dataType11'] = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.movableColumns = movableColumns
        self.movableColumns_nsprefix_ = None
        if data is None:
            self.data = []
        else:
            self.data = data
        self.data_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, v_family_problems_dataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if v_family_problems_dataType.subclass:
            return v_family_problems_dataType.subclass(*args_, **kwargs_)
        else:
            return v_family_problems_dataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_movableColumns(self):
        return self.movableColumns
    def set_movableColumns(self, movableColumns):
        self.movableColumns = movableColumns
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def add_data(self, value):
        self.data.append(value)
    def insert_data_at(self, index, value):
        self.data.insert(index, value)
    def replace_data_at(self, index, value):
        self.data[index] = value
    def has__content(self):
        if (
            self.movableColumns or
            self.data
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='v_family_problems_dataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('v_family_problems_dataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'v_family_problems_dataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='v_family_problems_dataType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='v_family_problems_dataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='v_family_problems_dataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='v_family_problems_dataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.movableColumns is not None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>%s</%smovableColumns>%s' % (namespaceprefix_ , self.gds_format_boolean(self.movableColumns, input_name='movableColumns'), namespaceprefix_ , eol_))
        if self.movableColumns is None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>false</%smovableColumns/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        for data_ in self.data:
            namespaceprefix_ = self.data_nsprefix_ + ':' if (UseCapturedNS_ and self.data_nsprefix_) else ''
            data_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='data', pretty_print=pretty_print)
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.movableColumns is not None:
            json_dict['movableColumns'] = self.movableColumns
        child_list = []
        for child in self.data:
            child_dict = child.exportJson(json_dict, 'data', True)
            if child_dict:
                child_list.append(child_dict)
        if child_list:
            json_dict['data'] = child_list
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'movableColumns':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'movableColumns')
            ival_ = self.gds_validate_boolean(ival_, node, 'movableColumns')
            self.movableColumns = ival_
            self.movableColumns_nsprefix_ = child_.prefix
        elif nodeName_ == 'data':
            obj_ = dataType11.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.data.append(obj_)
            obj_.original_tagname_ = 'data'
# end class v_family_problems_dataType


class dataType11(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, diagnose: 'string' = 'Keine Familienanamnese bekannt', erklaerung: List_['erklaerungType12'] = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.diagnose = diagnose
        self.diagnose_nsprefix_ = None
        if erklaerung is None:
            self.erklaerung = []
        else:
            self.erklaerung = erklaerung
        self.erklaerung_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dataType11)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dataType11.subclass:
            return dataType11.subclass(*args_, **kwargs_)
        else:
            return dataType11(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_diagnose(self):
        return self.diagnose
    def set_diagnose(self, diagnose):
        self.diagnose = diagnose
    def get_erklaerung(self):
        return self.erklaerung
    def set_erklaerung(self, erklaerung):
        self.erklaerung = erklaerung
    def add_erklaerung(self, value):
        self.erklaerung.append(value)
    def insert_erklaerung_at(self, index, value):
        self.erklaerung.insert(index, value)
    def replace_erklaerung_at(self, index, value):
        self.erklaerung[index] = value
    def has__content(self):
        if (
            self.diagnose != "Keine Familienanamnese bekannt" or
            self.erklaerung
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType11', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dataType11')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dataType11':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dataType11')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dataType11', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dataType11'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType11', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.diagnose is not None:
            namespaceprefix_ = self.diagnose_nsprefix_ + ':' if (UseCapturedNS_ and self.diagnose_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdiagnose>%s</%sdiagnose>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.diagnose), input_name='diagnose')), namespaceprefix_ , eol_))
        if self.diagnose is None:
            namespaceprefix_ = self.diagnose_nsprefix_ + ':' if (UseCapturedNS_ and self.diagnose_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdiagnose>Keine Familienanamnese bekannt</%sdiagnose/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        for erklaerung_ in self.erklaerung:
            namespaceprefix_ = self.erklaerung_nsprefix_ + ':' if (UseCapturedNS_ and self.erklaerung_nsprefix_) else ''
            erklaerung_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='erklaerung', pretty_print=pretty_print)
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.diagnose is not None:
            json_dict['diagnose'] = self.diagnose
        child_list = []
        for child in self.erklaerung:
            child_dict = child.exportJson(json_dict, 'erklaerung', True)
            if child_dict:
                child_list.append(child_dict)
        if child_list:
            json_dict['erklaerung'] = child_list
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'diagnose':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'diagnose')
            value_ = self.gds_validate_string(value_, node, 'diagnose')
            self.diagnose = value_
            self.diagnose_nsprefix_ = child_.prefix
        elif nodeName_ == 'erklaerung':
            obj_ = erklaerungType12.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.erklaerung.append(obj_)
            obj_.original_tagname_ = 'erklaerung'
# end class dataType11


class erklaerungType12(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, url: 'string' = None, label: 'string' = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.url = url
        self.url_nsprefix_ = None
        self.label = label
        self.label_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, erklaerungType12)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if erklaerungType12.subclass:
            return erklaerungType12.subclass(*args_, **kwargs_)
        else:
            return erklaerungType12(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_url(self):
        return self.url
    def set_url(self, url):
        self.url = url
    def get_label(self):
        return self.label
    def set_label(self, label):
        self.label = label
    def has__content(self):
        if (
            self.url is not None or
            self.label is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='erklaerungType12', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('erklaerungType12')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'erklaerungType12':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='erklaerungType12')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='erklaerungType12', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='erklaerungType12'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='erklaerungType12', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.url is not None:
            namespaceprefix_ = self.url_nsprefix_ + ':' if (UseCapturedNS_ and self.url_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%surl>%s</%surl>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.url), input_name='url')), namespaceprefix_ , eol_))
        if self.label is not None:
            namespaceprefix_ = self.label_nsprefix_ + ':' if (UseCapturedNS_ and self.label_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slabel>%s</%slabel>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.label), input_name='label')), namespaceprefix_ , eol_))
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.url is not None:
            json_dict['url'] = self.url
        if self.label is not None:
            json_dict['label'] = self.label
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'url':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'url')
            value_ = self.gds_validate_string(value_, node, 'url')
            self.url = value_
            self.url_nsprefix_ = child_.prefix
        elif nodeName_ == 'label':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'label')
            value_ = self.gds_validate_string(value_, node, 'label')
            self.label = value_
            self.label_nsprefix_ = child_.prefix
# end class erklaerungType12


class i_family_problems_dataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, movableColumns: 'boolean' = True, data: List_['dataType13'] = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.movableColumns = movableColumns
        self.movableColumns_nsprefix_ = None
        if data is None:
            self.data = []
        else:
            self.data = data
        self.data_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, i_family_problems_dataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if i_family_problems_dataType.subclass:
            return i_family_problems_dataType.subclass(*args_, **kwargs_)
        else:
            return i_family_problems_dataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_movableColumns(self):
        return self.movableColumns
    def set_movableColumns(self, movableColumns):
        self.movableColumns = movableColumns
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def add_data(self, value):
        self.data.append(value)
    def insert_data_at(self, index, value):
        self.data.insert(index, value)
    def replace_data_at(self, index, value):
        self.data[index] = value
    def has__content(self):
        if (
            not self.movableColumns or
            self.data
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='i_family_problems_dataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('i_family_problems_dataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'i_family_problems_dataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='i_family_problems_dataType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='i_family_problems_dataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='i_family_problems_dataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='i_family_problems_dataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.movableColumns is not None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>%s</%smovableColumns>%s' % (namespaceprefix_ , self.gds_format_boolean(self.movableColumns, input_name='movableColumns'), namespaceprefix_ , eol_))
        if self.movableColumns is None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>true</%smovableColumns/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        for data_ in self.data:
            namespaceprefix_ = self.data_nsprefix_ + ':' if (UseCapturedNS_ and self.data_nsprefix_) else ''
            data_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='data', pretty_print=pretty_print)
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.movableColumns is not None:
            json_dict['movableColumns'] = self.movableColumns
        child_list = []
        for child in self.data:
            child_dict = child.exportJson(json_dict, 'data', True)
            if child_dict:
                child_list.append(child_dict)
        if child_list:
            json_dict['data'] = child_list
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'movableColumns':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'movableColumns')
            ival_ = self.gds_validate_boolean(ival_, node, 'movableColumns')
            self.movableColumns = ival_
            self.movableColumns_nsprefix_ = child_.prefix
        elif nodeName_ == 'data':
            obj_ = dataType13.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.data.append(obj_)
            obj_.original_tagname_ = 'data'
# end class i_family_problems_dataType


class dataType13(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, diagnose: 'string' = 'Keine Familienanamnese bekannt', code: 'string' = None, codesystem: 'anyURI' = None, status: 'string' = None, verifizierung: 'string' = None, codesystem_type: 'string' = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.diagnose = diagnose
        self.diagnose_nsprefix_ = None
        self.code = code
        self.code_nsprefix_ = None
        self.codesystem = codesystem
        self.codesystem_nsprefix_ = None
        self.status = status
        self.status_nsprefix_ = None
        self.verifizierung = verifizierung
        self.verifizierung_nsprefix_ = None
        self.codesystem_type = codesystem_type
        self.codesystem_type_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dataType13)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dataType13.subclass:
            return dataType13.subclass(*args_, **kwargs_)
        else:
            return dataType13(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_diagnose(self):
        return self.diagnose
    def set_diagnose(self, diagnose):
        self.diagnose = diagnose
    def get_code(self):
        return self.code
    def set_code(self, code):
        self.code = code
    def get_codesystem(self):
        return self.codesystem
    def set_codesystem(self, codesystem):
        self.codesystem = codesystem
    def get_status(self):
        return self.status
    def set_status(self, status):
        self.status = status
    def get_verifizierung(self):
        return self.verifizierung
    def set_verifizierung(self, verifizierung):
        self.verifizierung = verifizierung
    def get_codesystem_type(self):
        return self.codesystem_type
    def set_codesystem_type(self, codesystem_type):
        self.codesystem_type = codesystem_type
    def has__content(self):
        if (
            self.diagnose != "Keine Familienanamnese bekannt" or
            self.code is not None or
            self.codesystem is not None or
            self.status is not None or
            self.verifizierung is not None or
            self.codesystem_type is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType13', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dataType13')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dataType13':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dataType13')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dataType13', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dataType13'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType13', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.diagnose is not None:
            namespaceprefix_ = self.diagnose_nsprefix_ + ':' if (UseCapturedNS_ and self.diagnose_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdiagnose>%s</%sdiagnose>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.diagnose), input_name='diagnose')), namespaceprefix_ , eol_))
        if self.diagnose is None:
            namespaceprefix_ = self.diagnose_nsprefix_ + ':' if (UseCapturedNS_ and self.diagnose_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdiagnose>Keine Familienanamnese bekannt</%sdiagnose/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.code is not None:
            namespaceprefix_ = self.code_nsprefix_ + ':' if (UseCapturedNS_ and self.code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scode>%s</%scode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.code), input_name='code')), namespaceprefix_ , eol_))
        if self.codesystem is not None:
            namespaceprefix_ = self.codesystem_nsprefix_ + ':' if (UseCapturedNS_ and self.codesystem_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodesystem>%s</%scodesystem>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codesystem), input_name='codesystem')), namespaceprefix_ , eol_))
        if self.status is not None:
            namespaceprefix_ = self.status_nsprefix_ + ':' if (UseCapturedNS_ and self.status_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstatus>%s</%sstatus>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.status), input_name='status')), namespaceprefix_ , eol_))
        if self.verifizierung is not None:
            namespaceprefix_ = self.verifizierung_nsprefix_ + ':' if (UseCapturedNS_ and self.verifizierung_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sverifizierung>%s</%sverifizierung>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.verifizierung), input_name='verifizierung')), namespaceprefix_ , eol_))
        if self.codesystem_type is not None:
            namespaceprefix_ = self.codesystem_type_nsprefix_ + ':' if (UseCapturedNS_ and self.codesystem_type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodesystem_type>%s</%scodesystem_type>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codesystem_type), input_name='codesystem_type')), namespaceprefix_ , eol_))
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.diagnose is not None:
            json_dict['diagnose'] = self.diagnose
        if self.code is not None:
            json_dict['code'] = self.code
        if self.codesystem is not None:
            json_dict['codesystem'] = self.codesystem
        if self.status is not None:
            json_dict['status'] = self.status
        if self.verifizierung is not None:
            json_dict['verifizierung'] = self.verifizierung
        if self.codesystem_type is not None:
            json_dict['codesystem_type'] = self.codesystem_type
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'diagnose':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'diagnose')
            value_ = self.gds_validate_string(value_, node, 'diagnose')
            self.diagnose = value_
            self.diagnose_nsprefix_ = child_.prefix
        elif nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
        elif nodeName_ == 'codesystem':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codesystem')
            value_ = self.gds_validate_string(value_, node, 'codesystem')
            self.codesystem = value_
            self.codesystem_nsprefix_ = child_.prefix
        elif nodeName_ == 'status':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'status')
            value_ = self.gds_validate_string(value_, node, 'status')
            self.status = value_
            self.status_nsprefix_ = child_.prefix
        elif nodeName_ == 'verifizierung':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'verifizierung')
            value_ = self.gds_validate_string(value_, node, 'verifizierung')
            self.verifizierung = value_
            self.verifizierung_nsprefix_ = child_.prefix
        elif nodeName_ == 'codesystem_type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codesystem_type')
            value_ = self.gds_validate_string(value_, node, 'codesystem_type')
            self.codesystem_type = value_
            self.codesystem_type_nsprefix_ = child_.prefix
# end class dataType13


class v_procedures_dataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, movableColumns: 'boolean' = False, data: List_['dataType14'] = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.movableColumns = movableColumns
        self.movableColumns_nsprefix_ = None
        if data is None:
            self.data = []
        else:
            self.data = data
        self.data_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, v_procedures_dataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if v_procedures_dataType.subclass:
            return v_procedures_dataType.subclass(*args_, **kwargs_)
        else:
            return v_procedures_dataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_movableColumns(self):
        return self.movableColumns
    def set_movableColumns(self, movableColumns):
        self.movableColumns = movableColumns
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def add_data(self, value):
        self.data.append(value)
    def insert_data_at(self, index, value):
        self.data.insert(index, value)
    def replace_data_at(self, index, value):
        self.data[index] = value
    def has__content(self):
        if (
            self.movableColumns or
            self.data
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='v_procedures_dataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('v_procedures_dataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'v_procedures_dataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='v_procedures_dataType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='v_procedures_dataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='v_procedures_dataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='v_procedures_dataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.movableColumns is not None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>%s</%smovableColumns>%s' % (namespaceprefix_ , self.gds_format_boolean(self.movableColumns, input_name='movableColumns'), namespaceprefix_ , eol_))
        if self.movableColumns is None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>false</%smovableColumns/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        for data_ in self.data:
            namespaceprefix_ = self.data_nsprefix_ + ':' if (UseCapturedNS_ and self.data_nsprefix_) else ''
            data_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='data', pretty_print=pretty_print)
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.movableColumns is not None:
            json_dict['movableColumns'] = self.movableColumns
        child_list = []
        for child in self.data:
            child_dict = child.exportJson(json_dict, 'data', True)
            if child_dict:
                child_list.append(child_dict)
        if child_list:
            json_dict['data'] = child_list
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'movableColumns':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'movableColumns')
            ival_ = self.gds_validate_boolean(ival_, node, 'movableColumns')
            self.movableColumns = ival_
            self.movableColumns_nsprefix_ = child_.prefix
        elif nodeName_ == 'data':
            obj_ = dataType14.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.data.append(obj_)
            obj_.original_tagname_ = 'data'
# end class v_procedures_dataType


class dataType14(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, zeitpunkt: 'string' = None, operation: 'string' = 'Keine Operationen bekannt', erklaerung: List_['erklaerungType15'] = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.zeitpunkt = zeitpunkt
        self.zeitpunkt_nsprefix_ = None
        self.operation = operation
        self.operation_nsprefix_ = None
        if erklaerung is None:
            self.erklaerung = []
        else:
            self.erklaerung = erklaerung
        self.erklaerung_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dataType14)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dataType14.subclass:
            return dataType14.subclass(*args_, **kwargs_)
        else:
            return dataType14(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_zeitpunkt(self):
        return self.zeitpunkt
    def set_zeitpunkt(self, zeitpunkt):
        self.zeitpunkt = zeitpunkt
    def get_operation(self):
        return self.operation
    def set_operation(self, operation):
        self.operation = operation
    def get_erklaerung(self):
        return self.erklaerung
    def set_erklaerung(self, erklaerung):
        self.erklaerung = erklaerung
    def add_erklaerung(self, value):
        self.erklaerung.append(value)
    def insert_erklaerung_at(self, index, value):
        self.erklaerung.insert(index, value)
    def replace_erklaerung_at(self, index, value):
        self.erklaerung[index] = value
    def has__content(self):
        if (
            self.zeitpunkt is not None or
            self.operation != "Keine Operationen bekannt" or
            self.erklaerung
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType14', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dataType14')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dataType14':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dataType14')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dataType14', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dataType14'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType14', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.zeitpunkt is not None:
            namespaceprefix_ = self.zeitpunkt_nsprefix_ + ':' if (UseCapturedNS_ and self.zeitpunkt_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%szeitpunkt>%s</%szeitpunkt>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.zeitpunkt), input_name='zeitpunkt')), namespaceprefix_ , eol_))
        if self.operation is not None:
            namespaceprefix_ = self.operation_nsprefix_ + ':' if (UseCapturedNS_ and self.operation_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soperation>%s</%soperation>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.operation), input_name='operation')), namespaceprefix_ , eol_))
        if self.operation is None:
            namespaceprefix_ = self.operation_nsprefix_ + ':' if (UseCapturedNS_ and self.operation_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soperation>Keine Operationen bekannt</%soperation/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        for erklaerung_ in self.erklaerung:
            namespaceprefix_ = self.erklaerung_nsprefix_ + ':' if (UseCapturedNS_ and self.erklaerung_nsprefix_) else ''
            erklaerung_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='erklaerung', pretty_print=pretty_print)
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.zeitpunkt is not None:
            json_dict['zeitpunkt'] = self.zeitpunkt
        if self.operation is not None:
            json_dict['operation'] = self.operation
        child_list = []
        for child in self.erklaerung:
            child_dict = child.exportJson(json_dict, 'erklaerung', True)
            if child_dict:
                child_list.append(child_dict)
        if child_list:
            json_dict['erklaerung'] = child_list
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'zeitpunkt':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'zeitpunkt')
            value_ = self.gds_validate_string(value_, node, 'zeitpunkt')
            self.zeitpunkt = value_
            self.zeitpunkt_nsprefix_ = child_.prefix
        elif nodeName_ == 'operation':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'operation')
            value_ = self.gds_validate_string(value_, node, 'operation')
            self.operation = value_
            self.operation_nsprefix_ = child_.prefix
        elif nodeName_ == 'erklaerung':
            obj_ = erklaerungType15.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.erklaerung.append(obj_)
            obj_.original_tagname_ = 'erklaerung'
# end class dataType14


class erklaerungType15(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, url: 'string' = None, label: 'string' = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.url = url
        self.url_nsprefix_ = None
        self.label = label
        self.label_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, erklaerungType15)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if erklaerungType15.subclass:
            return erklaerungType15.subclass(*args_, **kwargs_)
        else:
            return erklaerungType15(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_url(self):
        return self.url
    def set_url(self, url):
        self.url = url
    def get_label(self):
        return self.label
    def set_label(self, label):
        self.label = label
    def has__content(self):
        if (
            self.url is not None or
            self.label is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='erklaerungType15', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('erklaerungType15')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'erklaerungType15':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='erklaerungType15')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='erklaerungType15', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='erklaerungType15'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='erklaerungType15', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.url is not None:
            namespaceprefix_ = self.url_nsprefix_ + ':' if (UseCapturedNS_ and self.url_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%surl>%s</%surl>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.url), input_name='url')), namespaceprefix_ , eol_))
        if self.label is not None:
            namespaceprefix_ = self.label_nsprefix_ + ':' if (UseCapturedNS_ and self.label_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slabel>%s</%slabel>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.label), input_name='label')), namespaceprefix_ , eol_))
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.url is not None:
            json_dict['url'] = self.url
        if self.label is not None:
            json_dict['label'] = self.label
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'url':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'url')
            value_ = self.gds_validate_string(value_, node, 'url')
            self.url = value_
            self.url_nsprefix_ = child_.prefix
        elif nodeName_ == 'label':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'label')
            value_ = self.gds_validate_string(value_, node, 'label')
            self.label = value_
            self.label_nsprefix_ = child_.prefix
# end class erklaerungType15


class i_procedures_dataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, movableColumns: 'boolean' = True, data: List_['dataType16'] = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.movableColumns = movableColumns
        self.movableColumns_nsprefix_ = None
        if data is None:
            self.data = []
        else:
            self.data = data
        self.data_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, i_procedures_dataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if i_procedures_dataType.subclass:
            return i_procedures_dataType.subclass(*args_, **kwargs_)
        else:
            return i_procedures_dataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_movableColumns(self):
        return self.movableColumns
    def set_movableColumns(self, movableColumns):
        self.movableColumns = movableColumns
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def add_data(self, value):
        self.data.append(value)
    def insert_data_at(self, index, value):
        self.data.insert(index, value)
    def replace_data_at(self, index, value):
        self.data[index] = value
    def has__content(self):
        if (
            not self.movableColumns or
            self.data
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='i_procedures_dataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('i_procedures_dataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'i_procedures_dataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='i_procedures_dataType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='i_procedures_dataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='i_procedures_dataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='i_procedures_dataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.movableColumns is not None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>%s</%smovableColumns>%s' % (namespaceprefix_ , self.gds_format_boolean(self.movableColumns, input_name='movableColumns'), namespaceprefix_ , eol_))
        if self.movableColumns is None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>true</%smovableColumns/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        for data_ in self.data:
            namespaceprefix_ = self.data_nsprefix_ + ':' if (UseCapturedNS_ and self.data_nsprefix_) else ''
            data_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='data', pretty_print=pretty_print)
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.movableColumns is not None:
            json_dict['movableColumns'] = self.movableColumns
        child_list = []
        for child in self.data:
            child_dict = child.exportJson(json_dict, 'data', True)
            if child_dict:
                child_list.append(child_dict)
        if child_list:
            json_dict['data'] = child_list
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'movableColumns':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'movableColumns')
            ival_ = self.gds_validate_boolean(ival_, node, 'movableColumns')
            self.movableColumns = ival_
            self.movableColumns_nsprefix_ = child_.prefix
        elif nodeName_ == 'data':
            obj_ = dataType16.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.data.append(obj_)
            obj_.original_tagname_ = 'data'
# end class i_procedures_dataType


class dataType16(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, zeitpunkt: 'string' = None, operation: 'string' = 'Keine Operationen bekannt', code: 'string' = None, codesystem: 'anyURI' = None, status: 'string' = None, codesystem_type: 'string' = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.zeitpunkt = zeitpunkt
        self.zeitpunkt_nsprefix_ = None
        self.operation = operation
        self.operation_nsprefix_ = None
        self.code = code
        self.code_nsprefix_ = None
        self.codesystem = codesystem
        self.codesystem_nsprefix_ = None
        self.status = status
        self.status_nsprefix_ = None
        self.codesystem_type = codesystem_type
        self.codesystem_type_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dataType16)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dataType16.subclass:
            return dataType16.subclass(*args_, **kwargs_)
        else:
            return dataType16(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_zeitpunkt(self):
        return self.zeitpunkt
    def set_zeitpunkt(self, zeitpunkt):
        self.zeitpunkt = zeitpunkt
    def get_operation(self):
        return self.operation
    def set_operation(self, operation):
        self.operation = operation
    def get_code(self):
        return self.code
    def set_code(self, code):
        self.code = code
    def get_codesystem(self):
        return self.codesystem
    def set_codesystem(self, codesystem):
        self.codesystem = codesystem
    def get_status(self):
        return self.status
    def set_status(self, status):
        self.status = status
    def get_codesystem_type(self):
        return self.codesystem_type
    def set_codesystem_type(self, codesystem_type):
        self.codesystem_type = codesystem_type
    def has__content(self):
        if (
            self.zeitpunkt is not None or
            self.operation != "Keine Operationen bekannt" or
            self.code is not None or
            self.codesystem is not None or
            self.status is not None or
            self.codesystem_type is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType16', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dataType16')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dataType16':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dataType16')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dataType16', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dataType16'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType16', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.zeitpunkt is not None:
            namespaceprefix_ = self.zeitpunkt_nsprefix_ + ':' if (UseCapturedNS_ and self.zeitpunkt_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%szeitpunkt>%s</%szeitpunkt>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.zeitpunkt), input_name='zeitpunkt')), namespaceprefix_ , eol_))
        if self.operation is not None:
            namespaceprefix_ = self.operation_nsprefix_ + ':' if (UseCapturedNS_ and self.operation_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soperation>%s</%soperation>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.operation), input_name='operation')), namespaceprefix_ , eol_))
        if self.operation is None:
            namespaceprefix_ = self.operation_nsprefix_ + ':' if (UseCapturedNS_ and self.operation_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soperation>Keine Operationen bekannt</%soperation/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.code is not None:
            namespaceprefix_ = self.code_nsprefix_ + ':' if (UseCapturedNS_ and self.code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scode>%s</%scode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.code), input_name='code')), namespaceprefix_ , eol_))
        if self.codesystem is not None:
            namespaceprefix_ = self.codesystem_nsprefix_ + ':' if (UseCapturedNS_ and self.codesystem_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodesystem>%s</%scodesystem>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codesystem), input_name='codesystem')), namespaceprefix_ , eol_))
        if self.status is not None:
            namespaceprefix_ = self.status_nsprefix_ + ':' if (UseCapturedNS_ and self.status_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstatus>%s</%sstatus>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.status), input_name='status')), namespaceprefix_ , eol_))
        if self.codesystem_type is not None:
            namespaceprefix_ = self.codesystem_type_nsprefix_ + ':' if (UseCapturedNS_ and self.codesystem_type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodesystem_type>%s</%scodesystem_type>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codesystem_type), input_name='codesystem_type')), namespaceprefix_ , eol_))
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.zeitpunkt is not None:
            json_dict['zeitpunkt'] = self.zeitpunkt
        if self.operation is not None:
            json_dict['operation'] = self.operation
        if self.code is not None:
            json_dict['code'] = self.code
        if self.codesystem is not None:
            json_dict['codesystem'] = self.codesystem
        if self.status is not None:
            json_dict['status'] = self.status
        if self.codesystem_type is not None:
            json_dict['codesystem_type'] = self.codesystem_type
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'zeitpunkt':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'zeitpunkt')
            value_ = self.gds_validate_string(value_, node, 'zeitpunkt')
            self.zeitpunkt = value_
            self.zeitpunkt_nsprefix_ = child_.prefix
        elif nodeName_ == 'operation':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'operation')
            value_ = self.gds_validate_string(value_, node, 'operation')
            self.operation = value_
            self.operation_nsprefix_ = child_.prefix
        elif nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
        elif nodeName_ == 'codesystem':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codesystem')
            value_ = self.gds_validate_string(value_, node, 'codesystem')
            self.codesystem = value_
            self.codesystem_nsprefix_ = child_.prefix
        elif nodeName_ == 'status':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'status')
            value_ = self.gds_validate_string(value_, node, 'status')
            self.status = value_
            self.status_nsprefix_ = child_.prefix
        elif nodeName_ == 'codesystem_type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codesystem_type')
            value_ = self.gds_validate_string(value_, node, 'codesystem_type')
            self.codesystem_type = value_
            self.codesystem_type_nsprefix_ = child_.prefix
# end class dataType16


class v_results_dataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, movableColumns: 'boolean' = False, data: List_['dataType17'] = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.movableColumns = movableColumns
        self.movableColumns_nsprefix_ = None
        if data is None:
            self.data = []
        else:
            self.data = data
        self.data_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, v_results_dataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if v_results_dataType.subclass:
            return v_results_dataType.subclass(*args_, **kwargs_)
        else:
            return v_results_dataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_movableColumns(self):
        return self.movableColumns
    def set_movableColumns(self, movableColumns):
        self.movableColumns = movableColumns
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def add_data(self, value):
        self.data.append(value)
    def insert_data_at(self, index, value):
        self.data.insert(index, value)
    def replace_data_at(self, index, value):
        self.data[index] = value
    def has__content(self):
        if (
            self.movableColumns or
            self.data
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='v_results_dataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('v_results_dataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'v_results_dataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='v_results_dataType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='v_results_dataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='v_results_dataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='v_results_dataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.movableColumns is not None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>%s</%smovableColumns>%s' % (namespaceprefix_ , self.gds_format_boolean(self.movableColumns, input_name='movableColumns'), namespaceprefix_ , eol_))
        if self.movableColumns is None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>false</%smovableColumns/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        for data_ in self.data:
            namespaceprefix_ = self.data_nsprefix_ + ':' if (UseCapturedNS_ and self.data_nsprefix_) else ''
            data_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='data', pretty_print=pretty_print)
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.movableColumns is not None:
            json_dict['movableColumns'] = self.movableColumns
        child_list = []
        for child in self.data:
            child_dict = child.exportJson(json_dict, 'data', True)
            if child_dict:
                child_list.append(child_dict)
        if child_list:
            json_dict['data'] = child_list
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'movableColumns':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'movableColumns')
            ival_ = self.gds_validate_boolean(ival_, node, 'movableColumns')
            self.movableColumns = ival_
            self.movableColumns_nsprefix_ = child_.prefix
        elif nodeName_ == 'data':
            obj_ = dataType17.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.data.append(obj_)
            obj_.original_tagname_ = 'data'
# end class v_results_dataType


class dataType17(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, zeitpunkt: 'string' = None, test: 'string' = 'Keine Tests bekannt', ergebnis: 'string' = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.zeitpunkt = zeitpunkt
        self.zeitpunkt_nsprefix_ = None
        self.test = test
        self.test_nsprefix_ = None
        self.ergebnis = ergebnis
        self.ergebnis_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dataType17)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dataType17.subclass:
            return dataType17.subclass(*args_, **kwargs_)
        else:
            return dataType17(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_zeitpunkt(self):
        return self.zeitpunkt
    def set_zeitpunkt(self, zeitpunkt):
        self.zeitpunkt = zeitpunkt
    def get_test(self):
        return self.test
    def set_test(self, test):
        self.test = test
    def get_ergebnis(self):
        return self.ergebnis
    def set_ergebnis(self, ergebnis):
        self.ergebnis = ergebnis
    def has__content(self):
        if (
            self.zeitpunkt is not None or
            self.test != "Keine Tests bekannt" or
            self.ergebnis is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType17', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dataType17')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dataType17':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dataType17')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dataType17', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dataType17'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType17', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.zeitpunkt is not None:
            namespaceprefix_ = self.zeitpunkt_nsprefix_ + ':' if (UseCapturedNS_ and self.zeitpunkt_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%szeitpunkt>%s</%szeitpunkt>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.zeitpunkt), input_name='zeitpunkt')), namespaceprefix_ , eol_))
        if self.test is not None:
            namespaceprefix_ = self.test_nsprefix_ + ':' if (UseCapturedNS_ and self.test_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stest>%s</%stest>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.test), input_name='test')), namespaceprefix_ , eol_))
        if self.test is None:
            namespaceprefix_ = self.test_nsprefix_ + ':' if (UseCapturedNS_ and self.test_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stest>Keine Tests bekannt</%stest/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.ergebnis is not None:
            namespaceprefix_ = self.ergebnis_nsprefix_ + ':' if (UseCapturedNS_ and self.ergebnis_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sergebnis>%s</%sergebnis>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ergebnis), input_name='ergebnis')), namespaceprefix_ , eol_))
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.zeitpunkt is not None:
            json_dict['zeitpunkt'] = self.zeitpunkt
        if self.test is not None:
            json_dict['test'] = self.test
        if self.ergebnis is not None:
            json_dict['ergebnis'] = self.ergebnis
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'zeitpunkt':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'zeitpunkt')
            value_ = self.gds_validate_string(value_, node, 'zeitpunkt')
            self.zeitpunkt = value_
            self.zeitpunkt_nsprefix_ = child_.prefix
        elif nodeName_ == 'test':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'test')
            value_ = self.gds_validate_string(value_, node, 'test')
            self.test = value_
            self.test_nsprefix_ = child_.prefix
        elif nodeName_ == 'ergebnis':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ergebnis')
            value_ = self.gds_validate_string(value_, node, 'ergebnis')
            self.ergebnis = value_
            self.ergebnis_nsprefix_ = child_.prefix
# end class dataType17


class i_results_dataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, movableColumns: 'boolean' = True, data: List_['dataType18'] = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.movableColumns = movableColumns
        self.movableColumns_nsprefix_ = None
        if data is None:
            self.data = []
        else:
            self.data = data
        self.data_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, i_results_dataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if i_results_dataType.subclass:
            return i_results_dataType.subclass(*args_, **kwargs_)
        else:
            return i_results_dataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_movableColumns(self):
        return self.movableColumns
    def set_movableColumns(self, movableColumns):
        self.movableColumns = movableColumns
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def add_data(self, value):
        self.data.append(value)
    def insert_data_at(self, index, value):
        self.data.insert(index, value)
    def replace_data_at(self, index, value):
        self.data[index] = value
    def has__content(self):
        if (
            not self.movableColumns or
            self.data
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='i_results_dataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('i_results_dataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'i_results_dataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='i_results_dataType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='i_results_dataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='i_results_dataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='i_results_dataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.movableColumns is not None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>%s</%smovableColumns>%s' % (namespaceprefix_ , self.gds_format_boolean(self.movableColumns, input_name='movableColumns'), namespaceprefix_ , eol_))
        if self.movableColumns is None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>true</%smovableColumns/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        for data_ in self.data:
            namespaceprefix_ = self.data_nsprefix_ + ':' if (UseCapturedNS_ and self.data_nsprefix_) else ''
            data_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='data', pretty_print=pretty_print)
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.movableColumns is not None:
            json_dict['movableColumns'] = self.movableColumns
        child_list = []
        for child in self.data:
            child_dict = child.exportJson(json_dict, 'data', True)
            if child_dict:
                child_list.append(child_dict)
        if child_list:
            json_dict['data'] = child_list
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'movableColumns':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'movableColumns')
            ival_ = self.gds_validate_boolean(ival_, node, 'movableColumns')
            self.movableColumns = ival_
            self.movableColumns_nsprefix_ = child_.prefix
        elif nodeName_ == 'data':
            obj_ = dataType18.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.data.append(obj_)
            obj_.original_tagname_ = 'data'
# end class i_results_dataType


class dataType18(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, zeitpunkt: 'string' = None, test: 'string' = 'Keine Tests bekannt', ergebnis: 'string' = None, codeTest: 'string' = None, codesystemTest: 'anyURI' = None, codeErgebnis: 'string' = None, codesystemErgebnis: 'string' = None, status: 'string' = None, codesystem_type_test: 'string' = None, codesystem_type_ergebnis: 'string' = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.zeitpunkt = zeitpunkt
        self.zeitpunkt_nsprefix_ = None
        self.test = test
        self.test_nsprefix_ = None
        self.ergebnis = ergebnis
        self.ergebnis_nsprefix_ = None
        self.codeTest = codeTest
        self.codeTest_nsprefix_ = None
        self.codesystemTest = codesystemTest
        self.codesystemTest_nsprefix_ = None
        self.codeErgebnis = codeErgebnis
        self.codeErgebnis_nsprefix_ = None
        self.codesystemErgebnis = codesystemErgebnis
        self.codesystemErgebnis_nsprefix_ = None
        self.status = status
        self.status_nsprefix_ = None
        self.codesystem_type_test = codesystem_type_test
        self.codesystem_type_test_nsprefix_ = None
        self.codesystem_type_ergebnis = codesystem_type_ergebnis
        self.codesystem_type_ergebnis_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dataType18)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dataType18.subclass:
            return dataType18.subclass(*args_, **kwargs_)
        else:
            return dataType18(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_zeitpunkt(self):
        return self.zeitpunkt
    def set_zeitpunkt(self, zeitpunkt):
        self.zeitpunkt = zeitpunkt
    def get_test(self):
        return self.test
    def set_test(self, test):
        self.test = test
    def get_ergebnis(self):
        return self.ergebnis
    def set_ergebnis(self, ergebnis):
        self.ergebnis = ergebnis
    def get_codeTest(self):
        return self.codeTest
    def set_codeTest(self, codeTest):
        self.codeTest = codeTest
    def get_codesystemTest(self):
        return self.codesystemTest
    def set_codesystemTest(self, codesystemTest):
        self.codesystemTest = codesystemTest
    def get_codeErgebnis(self):
        return self.codeErgebnis
    def set_codeErgebnis(self, codeErgebnis):
        self.codeErgebnis = codeErgebnis
    def get_codesystemErgebnis(self):
        return self.codesystemErgebnis
    def set_codesystemErgebnis(self, codesystemErgebnis):
        self.codesystemErgebnis = codesystemErgebnis
    def get_status(self):
        return self.status
    def set_status(self, status):
        self.status = status
    def get_codesystem_type_test(self):
        return self.codesystem_type_test
    def set_codesystem_type_test(self, codesystem_type_test):
        self.codesystem_type_test = codesystem_type_test
    def get_codesystem_type_ergebnis(self):
        return self.codesystem_type_ergebnis
    def set_codesystem_type_ergebnis(self, codesystem_type_ergebnis):
        self.codesystem_type_ergebnis = codesystem_type_ergebnis
    def has__content(self):
        if (
            self.zeitpunkt is not None or
            self.test != "Keine Tests bekannt" or
            self.ergebnis is not None or
            self.codeTest is not None or
            self.codesystemTest is not None or
            self.codeErgebnis is not None or
            self.codesystemErgebnis is not None or
            self.status is not None or
            self.codesystem_type_test is not None or
            self.codesystem_type_ergebnis is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType18', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dataType18')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dataType18':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dataType18')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dataType18', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dataType18'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType18', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.zeitpunkt is not None:
            namespaceprefix_ = self.zeitpunkt_nsprefix_ + ':' if (UseCapturedNS_ and self.zeitpunkt_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%szeitpunkt>%s</%szeitpunkt>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.zeitpunkt), input_name='zeitpunkt')), namespaceprefix_ , eol_))
        if self.test is not None:
            namespaceprefix_ = self.test_nsprefix_ + ':' if (UseCapturedNS_ and self.test_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stest>%s</%stest>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.test), input_name='test')), namespaceprefix_ , eol_))
        if self.test is None:
            namespaceprefix_ = self.test_nsprefix_ + ':' if (UseCapturedNS_ and self.test_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stest>Keine Tests bekannt</%stest/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.ergebnis is not None:
            namespaceprefix_ = self.ergebnis_nsprefix_ + ':' if (UseCapturedNS_ and self.ergebnis_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sergebnis>%s</%sergebnis>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ergebnis), input_name='ergebnis')), namespaceprefix_ , eol_))
        if self.codeTest is not None:
            namespaceprefix_ = self.codeTest_nsprefix_ + ':' if (UseCapturedNS_ and self.codeTest_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodeTest>%s</%scodeTest>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codeTest), input_name='codeTest')), namespaceprefix_ , eol_))
        if self.codesystemTest is not None:
            namespaceprefix_ = self.codesystemTest_nsprefix_ + ':' if (UseCapturedNS_ and self.codesystemTest_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodesystemTest>%s</%scodesystemTest>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codesystemTest), input_name='codesystemTest')), namespaceprefix_ , eol_))
        if self.codeErgebnis is not None:
            namespaceprefix_ = self.codeErgebnis_nsprefix_ + ':' if (UseCapturedNS_ and self.codeErgebnis_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodeErgebnis>%s</%scodeErgebnis>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codeErgebnis), input_name='codeErgebnis')), namespaceprefix_ , eol_))
        if self.codesystemErgebnis is not None:
            namespaceprefix_ = self.codesystemErgebnis_nsprefix_ + ':' if (UseCapturedNS_ and self.codesystemErgebnis_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodesystemErgebnis>%s</%scodesystemErgebnis>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codesystemErgebnis), input_name='codesystemErgebnis')), namespaceprefix_ , eol_))
        if self.status is not None:
            namespaceprefix_ = self.status_nsprefix_ + ':' if (UseCapturedNS_ and self.status_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstatus>%s</%sstatus>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.status), input_name='status')), namespaceprefix_ , eol_))
        if self.codesystem_type_test is not None:
            namespaceprefix_ = self.codesystem_type_test_nsprefix_ + ':' if (UseCapturedNS_ and self.codesystem_type_test_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodesystem_type_test>%s</%scodesystem_type_test>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codesystem_type_test), input_name='codesystem_type_test')), namespaceprefix_ , eol_))
        if self.codesystem_type_ergebnis is not None:
            namespaceprefix_ = self.codesystem_type_ergebnis_nsprefix_ + ':' if (UseCapturedNS_ and self.codesystem_type_ergebnis_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodesystem_type_ergebnis>%s</%scodesystem_type_ergebnis>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codesystem_type_ergebnis), input_name='codesystem_type_ergebnis')), namespaceprefix_ , eol_))
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.zeitpunkt is not None:
            json_dict['zeitpunkt'] = self.zeitpunkt
        if self.test is not None:
            json_dict['test'] = self.test
        if self.ergebnis is not None:
            json_dict['ergebnis'] = self.ergebnis
        if self.codeTest is not None:
            json_dict['codeTest'] = self.codeTest
        if self.codesystemTest is not None:
            json_dict['codesystemTest'] = self.codesystemTest
        if self.codeErgebnis is not None:
            json_dict['codeErgebnis'] = self.codeErgebnis
        if self.codesystemErgebnis is not None:
            json_dict['codesystemErgebnis'] = self.codesystemErgebnis
        if self.status is not None:
            json_dict['status'] = self.status
        if self.codesystem_type_test is not None:
            json_dict['codesystem_type_test'] = self.codesystem_type_test
        if self.codesystem_type_ergebnis is not None:
            json_dict['codesystem_type_ergebnis'] = self.codesystem_type_ergebnis
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'zeitpunkt':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'zeitpunkt')
            value_ = self.gds_validate_string(value_, node, 'zeitpunkt')
            self.zeitpunkt = value_
            self.zeitpunkt_nsprefix_ = child_.prefix
        elif nodeName_ == 'test':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'test')
            value_ = self.gds_validate_string(value_, node, 'test')
            self.test = value_
            self.test_nsprefix_ = child_.prefix
        elif nodeName_ == 'ergebnis':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ergebnis')
            value_ = self.gds_validate_string(value_, node, 'ergebnis')
            self.ergebnis = value_
            self.ergebnis_nsprefix_ = child_.prefix
        elif nodeName_ == 'codeTest':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codeTest')
            value_ = self.gds_validate_string(value_, node, 'codeTest')
            self.codeTest = value_
            self.codeTest_nsprefix_ = child_.prefix
        elif nodeName_ == 'codesystemTest':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codesystemTest')
            value_ = self.gds_validate_string(value_, node, 'codesystemTest')
            self.codesystemTest = value_
            self.codesystemTest_nsprefix_ = child_.prefix
        elif nodeName_ == 'codeErgebnis':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codeErgebnis')
            value_ = self.gds_validate_string(value_, node, 'codeErgebnis')
            self.codeErgebnis = value_
            self.codeErgebnis_nsprefix_ = child_.prefix
        elif nodeName_ == 'codesystemErgebnis':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codesystemErgebnis')
            value_ = self.gds_validate_string(value_, node, 'codesystemErgebnis')
            self.codesystemErgebnis = value_
            self.codesystemErgebnis_nsprefix_ = child_.prefix
        elif nodeName_ == 'status':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'status')
            value_ = self.gds_validate_string(value_, node, 'status')
            self.status = value_
            self.status_nsprefix_ = child_.prefix
        elif nodeName_ == 'codesystem_type_test':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codesystem_type_test')
            value_ = self.gds_validate_string(value_, node, 'codesystem_type_test')
            self.codesystem_type_test = value_
            self.codesystem_type_test_nsprefix_ = child_.prefix
        elif nodeName_ == 'codesystem_type_ergebnis':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codesystem_type_ergebnis')
            value_ = self.gds_validate_string(value_, node, 'codesystem_type_ergebnis')
            self.codesystem_type_ergebnis = value_
            self.codesystem_type_ergebnis_nsprefix_ = child_.prefix
# end class dataType18


class v_vitalsigns_dataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, movableColumns: 'boolean' = False, data: List_['dataType19'] = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.movableColumns = movableColumns
        self.movableColumns_nsprefix_ = None
        if data is None:
            self.data = []
        else:
            self.data = data
        self.data_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, v_vitalsigns_dataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if v_vitalsigns_dataType.subclass:
            return v_vitalsigns_dataType.subclass(*args_, **kwargs_)
        else:
            return v_vitalsigns_dataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_movableColumns(self):
        return self.movableColumns
    def set_movableColumns(self, movableColumns):
        self.movableColumns = movableColumns
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def add_data(self, value):
        self.data.append(value)
    def insert_data_at(self, index, value):
        self.data.insert(index, value)
    def replace_data_at(self, index, value):
        self.data[index] = value
    def has__content(self):
        if (
            self.movableColumns or
            self.data
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='v_vitalsigns_dataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('v_vitalsigns_dataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'v_vitalsigns_dataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='v_vitalsigns_dataType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='v_vitalsigns_dataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='v_vitalsigns_dataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='v_vitalsigns_dataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.movableColumns is not None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>%s</%smovableColumns>%s' % (namespaceprefix_ , self.gds_format_boolean(self.movableColumns, input_name='movableColumns'), namespaceprefix_ , eol_))
        if self.movableColumns is None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>false</%smovableColumns/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        for data_ in self.data:
            namespaceprefix_ = self.data_nsprefix_ + ':' if (UseCapturedNS_ and self.data_nsprefix_) else ''
            data_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='data', pretty_print=pretty_print)
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.movableColumns is not None:
            json_dict['movableColumns'] = self.movableColumns
        child_list = []
        for child in self.data:
            child_dict = child.exportJson(json_dict, 'data', True)
            if child_dict:
                child_list.append(child_dict)
        if child_list:
            json_dict['data'] = child_list
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'movableColumns':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'movableColumns')
            ival_ = self.gds_validate_boolean(ival_, node, 'movableColumns')
            self.movableColumns = ival_
            self.movableColumns_nsprefix_ = child_.prefix
        elif nodeName_ == 'data':
            obj_ = dataType19.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.data.append(obj_)
            obj_.original_tagname_ = 'data'
# end class v_vitalsigns_dataType


class dataType19(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, zeitpunkt: 'string' = None, gemessenerWert: 'string' = 'Keine gemessene Werte bekannt', ergebnis: 'string' = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.zeitpunkt = zeitpunkt
        self.zeitpunkt_nsprefix_ = None
        self.gemessenerWert = gemessenerWert
        self.gemessenerWert_nsprefix_ = None
        self.ergebnis = ergebnis
        self.ergebnis_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dataType19)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dataType19.subclass:
            return dataType19.subclass(*args_, **kwargs_)
        else:
            return dataType19(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_zeitpunkt(self):
        return self.zeitpunkt
    def set_zeitpunkt(self, zeitpunkt):
        self.zeitpunkt = zeitpunkt
    def get_gemessenerWert(self):
        return self.gemessenerWert
    def set_gemessenerWert(self, gemessenerWert):
        self.gemessenerWert = gemessenerWert
    def get_ergebnis(self):
        return self.ergebnis
    def set_ergebnis(self, ergebnis):
        self.ergebnis = ergebnis
    def has__content(self):
        if (
            self.zeitpunkt is not None or
            self.gemessenerWert != "Keine gemessene Werte bekannt" or
            self.ergebnis is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType19', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dataType19')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dataType19':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dataType19')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dataType19', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dataType19'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType19', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.zeitpunkt is not None:
            namespaceprefix_ = self.zeitpunkt_nsprefix_ + ':' if (UseCapturedNS_ and self.zeitpunkt_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%szeitpunkt>%s</%szeitpunkt>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.zeitpunkt), input_name='zeitpunkt')), namespaceprefix_ , eol_))
        if self.gemessenerWert is not None:
            namespaceprefix_ = self.gemessenerWert_nsprefix_ + ':' if (UseCapturedNS_ and self.gemessenerWert_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sgemessenerWert>%s</%sgemessenerWert>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.gemessenerWert), input_name='gemessenerWert')), namespaceprefix_ , eol_))
        if self.gemessenerWert is None:
            namespaceprefix_ = self.gemessenerWert_nsprefix_ + ':' if (UseCapturedNS_ and self.gemessenerWert_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sgemessenerWert>Keine gemessene Werte bekannt</%sgemessenerWert/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.ergebnis is not None:
            namespaceprefix_ = self.ergebnis_nsprefix_ + ':' if (UseCapturedNS_ and self.ergebnis_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sergebnis>%s</%sergebnis>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ergebnis), input_name='ergebnis')), namespaceprefix_ , eol_))
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.zeitpunkt is not None:
            json_dict['zeitpunkt'] = self.zeitpunkt
        if self.gemessenerWert is not None:
            json_dict['gemessenerWert'] = self.gemessenerWert
        if self.ergebnis is not None:
            json_dict['ergebnis'] = self.ergebnis
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'zeitpunkt':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'zeitpunkt')
            value_ = self.gds_validate_string(value_, node, 'zeitpunkt')
            self.zeitpunkt = value_
            self.zeitpunkt_nsprefix_ = child_.prefix
        elif nodeName_ == 'gemessenerWert':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'gemessenerWert')
            value_ = self.gds_validate_string(value_, node, 'gemessenerWert')
            self.gemessenerWert = value_
            self.gemessenerWert_nsprefix_ = child_.prefix
        elif nodeName_ == 'ergebnis':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ergebnis')
            value_ = self.gds_validate_string(value_, node, 'ergebnis')
            self.ergebnis = value_
            self.ergebnis_nsprefix_ = child_.prefix
# end class dataType19


class i_vitalsigns_dataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, movableColumns: 'boolean' = True, data: List_['dataType20'] = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.movableColumns = movableColumns
        self.movableColumns_nsprefix_ = None
        if data is None:
            self.data = []
        else:
            self.data = data
        self.data_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, i_vitalsigns_dataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if i_vitalsigns_dataType.subclass:
            return i_vitalsigns_dataType.subclass(*args_, **kwargs_)
        else:
            return i_vitalsigns_dataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_movableColumns(self):
        return self.movableColumns
    def set_movableColumns(self, movableColumns):
        self.movableColumns = movableColumns
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def add_data(self, value):
        self.data.append(value)
    def insert_data_at(self, index, value):
        self.data.insert(index, value)
    def replace_data_at(self, index, value):
        self.data[index] = value
    def has__content(self):
        if (
            not self.movableColumns or
            self.data
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='i_vitalsigns_dataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('i_vitalsigns_dataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'i_vitalsigns_dataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='i_vitalsigns_dataType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='i_vitalsigns_dataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='i_vitalsigns_dataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='i_vitalsigns_dataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.movableColumns is not None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>%s</%smovableColumns>%s' % (namespaceprefix_ , self.gds_format_boolean(self.movableColumns, input_name='movableColumns'), namespaceprefix_ , eol_))
        if self.movableColumns is None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>true</%smovableColumns/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        for data_ in self.data:
            namespaceprefix_ = self.data_nsprefix_ + ':' if (UseCapturedNS_ and self.data_nsprefix_) else ''
            data_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='data', pretty_print=pretty_print)
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.movableColumns is not None:
            json_dict['movableColumns'] = self.movableColumns
        child_list = []
        for child in self.data:
            child_dict = child.exportJson(json_dict, 'data', True)
            if child_dict:
                child_list.append(child_dict)
        if child_list:
            json_dict['data'] = child_list
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'movableColumns':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'movableColumns')
            ival_ = self.gds_validate_boolean(ival_, node, 'movableColumns')
            self.movableColumns = ival_
            self.movableColumns_nsprefix_ = child_.prefix
        elif nodeName_ == 'data':
            obj_ = dataType20.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.data.append(obj_)
            obj_.original_tagname_ = 'data'
# end class i_vitalsigns_dataType


class dataType20(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, zeitpunkt: 'string' = None, gemessenerWert: 'string' = 'Keine gemessene Werte bekannt', ergebnis: 'string' = None, codeWert: 'string' = None, codesystemWert: 'string' = None, codeErgebnis: 'string' = None, codesystemErgebnis: 'string' = None, status: 'string' = None, codesystem_type_wert: 'string' = None, codesystem_type_ergebnis: 'string' = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.zeitpunkt = zeitpunkt
        self.zeitpunkt_nsprefix_ = None
        self.gemessenerWert = gemessenerWert
        self.gemessenerWert_nsprefix_ = None
        self.ergebnis = ergebnis
        self.ergebnis_nsprefix_ = None
        self.codeWert = codeWert
        self.codeWert_nsprefix_ = None
        self.codesystemWert = codesystemWert
        self.codesystemWert_nsprefix_ = None
        self.codeErgebnis = codeErgebnis
        self.codeErgebnis_nsprefix_ = None
        self.codesystemErgebnis = codesystemErgebnis
        self.codesystemErgebnis_nsprefix_ = None
        self.status = status
        self.status_nsprefix_ = None
        self.codesystem_type_wert = codesystem_type_wert
        self.codesystem_type_wert_nsprefix_ = None
        self.codesystem_type_ergebnis = codesystem_type_ergebnis
        self.codesystem_type_ergebnis_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dataType20)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dataType20.subclass:
            return dataType20.subclass(*args_, **kwargs_)
        else:
            return dataType20(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_zeitpunkt(self):
        return self.zeitpunkt
    def set_zeitpunkt(self, zeitpunkt):
        self.zeitpunkt = zeitpunkt
    def get_gemessenerWert(self):
        return self.gemessenerWert
    def set_gemessenerWert(self, gemessenerWert):
        self.gemessenerWert = gemessenerWert
    def get_ergebnis(self):
        return self.ergebnis
    def set_ergebnis(self, ergebnis):
        self.ergebnis = ergebnis
    def get_codeWert(self):
        return self.codeWert
    def set_codeWert(self, codeWert):
        self.codeWert = codeWert
    def get_codesystemWert(self):
        return self.codesystemWert
    def set_codesystemWert(self, codesystemWert):
        self.codesystemWert = codesystemWert
    def get_codeErgebnis(self):
        return self.codeErgebnis
    def set_codeErgebnis(self, codeErgebnis):
        self.codeErgebnis = codeErgebnis
    def get_codesystemErgebnis(self):
        return self.codesystemErgebnis
    def set_codesystemErgebnis(self, codesystemErgebnis):
        self.codesystemErgebnis = codesystemErgebnis
    def get_status(self):
        return self.status
    def set_status(self, status):
        self.status = status
    def get_codesystem_type_wert(self):
        return self.codesystem_type_wert
    def set_codesystem_type_wert(self, codesystem_type_wert):
        self.codesystem_type_wert = codesystem_type_wert
    def get_codesystem_type_ergebnis(self):
        return self.codesystem_type_ergebnis
    def set_codesystem_type_ergebnis(self, codesystem_type_ergebnis):
        self.codesystem_type_ergebnis = codesystem_type_ergebnis
    def has__content(self):
        if (
            self.zeitpunkt is not None or
            self.gemessenerWert != "Keine gemessene Werte bekannt" or
            self.ergebnis is not None or
            self.codeWert is not None or
            self.codesystemWert is not None or
            self.codeErgebnis is not None or
            self.codesystemErgebnis is not None or
            self.status is not None or
            self.codesystem_type_wert is not None or
            self.codesystem_type_ergebnis is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType20', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dataType20')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dataType20':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dataType20')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dataType20', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dataType20'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType20', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.zeitpunkt is not None:
            namespaceprefix_ = self.zeitpunkt_nsprefix_ + ':' if (UseCapturedNS_ and self.zeitpunkt_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%szeitpunkt>%s</%szeitpunkt>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.zeitpunkt), input_name='zeitpunkt')), namespaceprefix_ , eol_))
        if self.gemessenerWert is not None:
            namespaceprefix_ = self.gemessenerWert_nsprefix_ + ':' if (UseCapturedNS_ and self.gemessenerWert_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sgemessenerWert>%s</%sgemessenerWert>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.gemessenerWert), input_name='gemessenerWert')), namespaceprefix_ , eol_))
        if self.gemessenerWert is None:
            namespaceprefix_ = self.gemessenerWert_nsprefix_ + ':' if (UseCapturedNS_ and self.gemessenerWert_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sgemessenerWert>Keine gemessene Werte bekannt</%sgemessenerWert/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.ergebnis is not None:
            namespaceprefix_ = self.ergebnis_nsprefix_ + ':' if (UseCapturedNS_ and self.ergebnis_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sergebnis>%s</%sergebnis>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ergebnis), input_name='ergebnis')), namespaceprefix_ , eol_))
        if self.codeWert is not None:
            namespaceprefix_ = self.codeWert_nsprefix_ + ':' if (UseCapturedNS_ and self.codeWert_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodeWert>%s</%scodeWert>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codeWert), input_name='codeWert')), namespaceprefix_ , eol_))
        if self.codesystemWert is not None:
            namespaceprefix_ = self.codesystemWert_nsprefix_ + ':' if (UseCapturedNS_ and self.codesystemWert_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodesystemWert>%s</%scodesystemWert>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codesystemWert), input_name='codesystemWert')), namespaceprefix_ , eol_))
        if self.codeErgebnis is not None:
            namespaceprefix_ = self.codeErgebnis_nsprefix_ + ':' if (UseCapturedNS_ and self.codeErgebnis_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodeErgebnis>%s</%scodeErgebnis>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codeErgebnis), input_name='codeErgebnis')), namespaceprefix_ , eol_))
        if self.codesystemErgebnis is not None:
            namespaceprefix_ = self.codesystemErgebnis_nsprefix_ + ':' if (UseCapturedNS_ and self.codesystemErgebnis_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodesystemErgebnis>%s</%scodesystemErgebnis>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codesystemErgebnis), input_name='codesystemErgebnis')), namespaceprefix_ , eol_))
        if self.status is not None:
            namespaceprefix_ = self.status_nsprefix_ + ':' if (UseCapturedNS_ and self.status_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstatus>%s</%sstatus>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.status), input_name='status')), namespaceprefix_ , eol_))
        if self.codesystem_type_wert is not None:
            namespaceprefix_ = self.codesystem_type_wert_nsprefix_ + ':' if (UseCapturedNS_ and self.codesystem_type_wert_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodesystem_type_wert>%s</%scodesystem_type_wert>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codesystem_type_wert), input_name='codesystem_type_wert')), namespaceprefix_ , eol_))
        if self.codesystem_type_ergebnis is not None:
            namespaceprefix_ = self.codesystem_type_ergebnis_nsprefix_ + ':' if (UseCapturedNS_ and self.codesystem_type_ergebnis_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodesystem_type_ergebnis>%s</%scodesystem_type_ergebnis>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codesystem_type_ergebnis), input_name='codesystem_type_ergebnis')), namespaceprefix_ , eol_))
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.zeitpunkt is not None:
            json_dict['zeitpunkt'] = self.zeitpunkt
        if self.gemessenerWert is not None:
            json_dict['gemessenerWert'] = self.gemessenerWert
        if self.ergebnis is not None:
            json_dict['ergebnis'] = self.ergebnis
        if self.codeWert is not None:
            json_dict['codeWert'] = self.codeWert
        if self.codesystemWert is not None:
            json_dict['codesystemWert'] = self.codesystemWert
        if self.codeErgebnis is not None:
            json_dict['codeErgebnis'] = self.codeErgebnis
        if self.codesystemErgebnis is not None:
            json_dict['codesystemErgebnis'] = self.codesystemErgebnis
        if self.status is not None:
            json_dict['status'] = self.status
        if self.codesystem_type_wert is not None:
            json_dict['codesystem_type_wert'] = self.codesystem_type_wert
        if self.codesystem_type_ergebnis is not None:
            json_dict['codesystem_type_ergebnis'] = self.codesystem_type_ergebnis
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'zeitpunkt':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'zeitpunkt')
            value_ = self.gds_validate_string(value_, node, 'zeitpunkt')
            self.zeitpunkt = value_
            self.zeitpunkt_nsprefix_ = child_.prefix
        elif nodeName_ == 'gemessenerWert':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'gemessenerWert')
            value_ = self.gds_validate_string(value_, node, 'gemessenerWert')
            self.gemessenerWert = value_
            self.gemessenerWert_nsprefix_ = child_.prefix
        elif nodeName_ == 'ergebnis':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ergebnis')
            value_ = self.gds_validate_string(value_, node, 'ergebnis')
            self.ergebnis = value_
            self.ergebnis_nsprefix_ = child_.prefix
        elif nodeName_ == 'codeWert':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codeWert')
            value_ = self.gds_validate_string(value_, node, 'codeWert')
            self.codeWert = value_
            self.codeWert_nsprefix_ = child_.prefix
        elif nodeName_ == 'codesystemWert':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codesystemWert')
            value_ = self.gds_validate_string(value_, node, 'codesystemWert')
            self.codesystemWert = value_
            self.codesystemWert_nsprefix_ = child_.prefix
        elif nodeName_ == 'codeErgebnis':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codeErgebnis')
            value_ = self.gds_validate_string(value_, node, 'codeErgebnis')
            self.codeErgebnis = value_
            self.codeErgebnis_nsprefix_ = child_.prefix
        elif nodeName_ == 'codesystemErgebnis':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codesystemErgebnis')
            value_ = self.gds_validate_string(value_, node, 'codesystemErgebnis')
            self.codesystemErgebnis = value_
            self.codesystemErgebnis_nsprefix_ = child_.prefix
        elif nodeName_ == 'status':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'status')
            value_ = self.gds_validate_string(value_, node, 'status')
            self.status = value_
            self.status_nsprefix_ = child_.prefix
        elif nodeName_ == 'codesystem_type_wert':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codesystem_type_wert')
            value_ = self.gds_validate_string(value_, node, 'codesystem_type_wert')
            self.codesystem_type_wert = value_
            self.codesystem_type_wert_nsprefix_ = child_.prefix
        elif nodeName_ == 'codesystem_type_ergebnis':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codesystem_type_ergebnis')
            value_ = self.gds_validate_string(value_, node, 'codesystem_type_ergebnis')
            self.codesystem_type_ergebnis = value_
            self.codesystem_type_ergebnis_nsprefix_ = child_.prefix
# end class dataType20


class v_socialhistory_dataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, movableColumns: 'boolean' = False, data: List_['dataType21'] = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.movableColumns = movableColumns
        self.movableColumns_nsprefix_ = None
        if data is None:
            self.data = []
        else:
            self.data = data
        self.data_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, v_socialhistory_dataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if v_socialhistory_dataType.subclass:
            return v_socialhistory_dataType.subclass(*args_, **kwargs_)
        else:
            return v_socialhistory_dataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_movableColumns(self):
        return self.movableColumns
    def set_movableColumns(self, movableColumns):
        self.movableColumns = movableColumns
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def add_data(self, value):
        self.data.append(value)
    def insert_data_at(self, index, value):
        self.data.insert(index, value)
    def replace_data_at(self, index, value):
        self.data[index] = value
    def has__content(self):
        if (
            self.movableColumns or
            self.data
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='v_socialhistory_dataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('v_socialhistory_dataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'v_socialhistory_dataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='v_socialhistory_dataType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='v_socialhistory_dataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='v_socialhistory_dataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='v_socialhistory_dataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.movableColumns is not None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>%s</%smovableColumns>%s' % (namespaceprefix_ , self.gds_format_boolean(self.movableColumns, input_name='movableColumns'), namespaceprefix_ , eol_))
        if self.movableColumns is None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>false</%smovableColumns/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        for data_ in self.data:
            namespaceprefix_ = self.data_nsprefix_ + ':' if (UseCapturedNS_ and self.data_nsprefix_) else ''
            data_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='data', pretty_print=pretty_print)
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.movableColumns is not None:
            json_dict['movableColumns'] = self.movableColumns
        child_list = []
        for child in self.data:
            child_dict = child.exportJson(json_dict, 'data', True)
            if child_dict:
                child_list.append(child_dict)
        if child_list:
            json_dict['data'] = child_list
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'movableColumns':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'movableColumns')
            ival_ = self.gds_validate_boolean(ival_, node, 'movableColumns')
            self.movableColumns = ival_
            self.movableColumns_nsprefix_ = child_.prefix
        elif nodeName_ == 'data':
            obj_ = dataType21.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.data.append(obj_)
            obj_.original_tagname_ = 'data'
# end class v_socialhistory_dataType


class dataType21(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ereignis: 'string' = 'Keine Ergebnisse bekannt', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ereignis = ereignis
        self.ereignis_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dataType21)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dataType21.subclass:
            return dataType21.subclass(*args_, **kwargs_)
        else:
            return dataType21(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ereignis(self):
        return self.ereignis
    def set_ereignis(self, ereignis):
        self.ereignis = ereignis
    def has__content(self):
        if (
            self.ereignis != "Keine Ergebnisse bekannt"
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType21', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dataType21')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dataType21':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dataType21')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dataType21', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dataType21'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType21', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ereignis is not None:
            namespaceprefix_ = self.ereignis_nsprefix_ + ':' if (UseCapturedNS_ and self.ereignis_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sereignis>%s</%sereignis>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ereignis), input_name='ereignis')), namespaceprefix_ , eol_))
        if self.ereignis is None:
            namespaceprefix_ = self.ereignis_nsprefix_ + ':' if (UseCapturedNS_ and self.ereignis_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sereignis>Keine Ergebnisse bekannt</%sereignis/>%s' % (namespaceprefix_,namespace_prefix, eol_))
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.ereignis is not None:
            json_dict['ereignis'] = self.ereignis
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ereignis':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ereignis')
            value_ = self.gds_validate_string(value_, node, 'ereignis')
            self.ereignis = value_
            self.ereignis_nsprefix_ = child_.prefix
# end class dataType21


class i_socialhistory_dataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, movableColumns: 'boolean' = True, data: List_['dataType22'] = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.movableColumns = movableColumns
        self.movableColumns_nsprefix_ = None
        if data is None:
            self.data = []
        else:
            self.data = data
        self.data_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, i_socialhistory_dataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if i_socialhistory_dataType.subclass:
            return i_socialhistory_dataType.subclass(*args_, **kwargs_)
        else:
            return i_socialhistory_dataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_movableColumns(self):
        return self.movableColumns
    def set_movableColumns(self, movableColumns):
        self.movableColumns = movableColumns
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def add_data(self, value):
        self.data.append(value)
    def insert_data_at(self, index, value):
        self.data.insert(index, value)
    def replace_data_at(self, index, value):
        self.data[index] = value
    def has__content(self):
        if (
            not self.movableColumns or
            self.data
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='i_socialhistory_dataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('i_socialhistory_dataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'i_socialhistory_dataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='i_socialhistory_dataType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='i_socialhistory_dataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='i_socialhistory_dataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='i_socialhistory_dataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.movableColumns is not None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>%s</%smovableColumns>%s' % (namespaceprefix_ , self.gds_format_boolean(self.movableColumns, input_name='movableColumns'), namespaceprefix_ , eol_))
        if self.movableColumns is None:
            namespaceprefix_ = self.movableColumns_nsprefix_ + ':' if (UseCapturedNS_ and self.movableColumns_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smovableColumns>true</%smovableColumns/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        for data_ in self.data:
            namespaceprefix_ = self.data_nsprefix_ + ':' if (UseCapturedNS_ and self.data_nsprefix_) else ''
            data_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='data', pretty_print=pretty_print)
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.movableColumns is not None:
            json_dict['movableColumns'] = self.movableColumns
        child_list = []
        for child in self.data:
            child_dict = child.exportJson(json_dict, 'data', True)
            if child_dict:
                child_list.append(child_dict)
        if child_list:
            json_dict['data'] = child_list
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'movableColumns':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'movableColumns')
            ival_ = self.gds_validate_boolean(ival_, node, 'movableColumns')
            self.movableColumns = ival_
            self.movableColumns_nsprefix_ = child_.prefix
        elif nodeName_ == 'data':
            obj_ = dataType22.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.data.append(obj_)
            obj_.original_tagname_ = 'data'
# end class i_socialhistory_dataType


class dataType22(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, zeitpunkt: 'string' = None, ereignis: 'string' = 'Keine Ergebnisse bekannt', code: 'string' = None, codesystem: 'anyURI' = None, status: 'string' = None, codesystem_type: 'string' = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.zeitpunkt = zeitpunkt
        self.zeitpunkt_nsprefix_ = None
        self.ereignis = ereignis
        self.ereignis_nsprefix_ = None
        self.code = code
        self.code_nsprefix_ = None
        self.codesystem = codesystem
        self.codesystem_nsprefix_ = None
        self.status = status
        self.status_nsprefix_ = None
        self.codesystem_type = codesystem_type
        self.codesystem_type_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dataType22)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dataType22.subclass:
            return dataType22.subclass(*args_, **kwargs_)
        else:
            return dataType22(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_zeitpunkt(self):
        return self.zeitpunkt
    def set_zeitpunkt(self, zeitpunkt):
        self.zeitpunkt = zeitpunkt
    def get_ereignis(self):
        return self.ereignis
    def set_ereignis(self, ereignis):
        self.ereignis = ereignis
    def get_code(self):
        return self.code
    def set_code(self, code):
        self.code = code
    def get_codesystem(self):
        return self.codesystem
    def set_codesystem(self, codesystem):
        self.codesystem = codesystem
    def get_status(self):
        return self.status
    def set_status(self, status):
        self.status = status
    def get_codesystem_type(self):
        return self.codesystem_type
    def set_codesystem_type(self, codesystem_type):
        self.codesystem_type = codesystem_type
    def has__content(self):
        if (
            self.zeitpunkt is not None or
            self.ereignis != "Keine Ergebnisse bekannt" or
            self.code is not None or
            self.codesystem is not None or
            self.status is not None or
            self.codesystem_type is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType22', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dataType22')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dataType22':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dataType22')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dataType22', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dataType22'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:hl7-at:vidi" ', name_='dataType22', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.zeitpunkt is not None:
            namespaceprefix_ = self.zeitpunkt_nsprefix_ + ':' if (UseCapturedNS_ and self.zeitpunkt_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%szeitpunkt>%s</%szeitpunkt>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.zeitpunkt), input_name='zeitpunkt')), namespaceprefix_ , eol_))
        if self.ereignis is not None:
            namespaceprefix_ = self.ereignis_nsprefix_ + ':' if (UseCapturedNS_ and self.ereignis_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sereignis>%s</%sereignis>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ereignis), input_name='ereignis')), namespaceprefix_ , eol_))
        if self.ereignis is None:
            namespaceprefix_ = self.ereignis_nsprefix_ + ':' if (UseCapturedNS_ and self.ereignis_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sereignis>Keine Ergebnisse bekannt</%sereignis/>%s' % (namespaceprefix_,namespace_prefix, eol_))
        if self.code is not None:
            namespaceprefix_ = self.code_nsprefix_ + ':' if (UseCapturedNS_ and self.code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scode>%s</%scode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.code), input_name='code')), namespaceprefix_ , eol_))
        if self.codesystem is not None:
            namespaceprefix_ = self.codesystem_nsprefix_ + ':' if (UseCapturedNS_ and self.codesystem_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodesystem>%s</%scodesystem>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codesystem), input_name='codesystem')), namespaceprefix_ , eol_))
        if self.status is not None:
            namespaceprefix_ = self.status_nsprefix_ + ':' if (UseCapturedNS_ and self.status_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstatus>%s</%sstatus>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.status), input_name='status')), namespaceprefix_ , eol_))
        if self.codesystem_type is not None:
            namespaceprefix_ = self.codesystem_type_nsprefix_ + ':' if (UseCapturedNS_ and self.codesystem_type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scodesystem_type>%s</%scodesystem_type>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.codesystem_type), input_name='codesystem_type')), namespaceprefix_ , eol_))
    def exportJson(self, parent_dict=None, key=None, is_list=False):
        json_dict = dict()
        self.exportJsonAttributes(json_dict)
        self.exportJsonChildren(json_dict)
        return self.exportJsonResult(json_dict, parent_dict, key, is_list)
    def exportJsonResult(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
        return json_dict
    def exportJsonAttributes(self, json_dict):
        pass
    def exportJsonChildren(self, json_dict):
        if self.zeitpunkt is not None:
            json_dict['zeitpunkt'] = self.zeitpunkt
        if self.ereignis is not None:
            json_dict['ereignis'] = self.ereignis
        if self.code is not None:
            json_dict['code'] = self.code
        if self.codesystem is not None:
            json_dict['codesystem'] = self.codesystem
        if self.status is not None:
            json_dict['status'] = self.status
        if self.codesystem_type is not None:
            json_dict['codesystem_type'] = self.codesystem_type
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        if SaveNodeDict:
            node_dict[node] = self 
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'zeitpunkt':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'zeitpunkt')
            value_ = self.gds_validate_string(value_, node, 'zeitpunkt')
            self.zeitpunkt = value_
            self.zeitpunkt_nsprefix_ = child_.prefix
        elif nodeName_ == 'ereignis':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ereignis')
            value_ = self.gds_validate_string(value_, node, 'ereignis')
            self.ereignis = value_
            self.ereignis_nsprefix_ = child_.prefix
        elif nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
        elif nodeName_ == 'codesystem':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codesystem')
            value_ = self.gds_validate_string(value_, node, 'codesystem')
            self.codesystem = value_
            self.codesystem_nsprefix_ = child_.prefix
        elif nodeName_ == 'status':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'status')
            value_ = self.gds_validate_string(value_, node, 'status')
            self.status = value_
            self.status_nsprefix_ = child_.prefix
        elif nodeName_ == 'codesystem_type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'codesystem_type')
            value_ = self.gds_validate_string(value_, node, 'codesystem_type')
            self.codesystem_type = value_
            self.codesystem_type_nsprefix_ = child_.prefix
# end class dataType22


#
# End data representation classes.
#


GDSClassesMapping = {
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    prefix_tag = TagNamePrefix + tag
    rootClass = GDSClassesMapping.get(prefix_tag)
    if rootClass is None:
        rootClass = globals().get(prefix_tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'vidi'
        rootClass = vidi
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_=namespacedefs,
            pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, reverse_mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'vidi'
        rootClass = vidi
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if mapping is None:
        mapping = {}
    if reverse_mapping is None:
        reverse_mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping,
        reverse_mapping_=reverse_mapping, nsmap_=nsmap)
    reverse_node_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(str(content))
        sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_node_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'vidi'
        rootClass = vidi
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'vidi'
        rootClass = vidi
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from vidi import *\n\n')
        sys.stdout.write('import vidi as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
}

#
# Mapping of namespaces to types defined in them
# and the file in which each is defined.
# simpleTypes are marked "ST" and complexTypes "CT".
NamespaceToDefMappings_ = {'urn:hl7-at:vidi': []}

__all__ = [
    "dataType",
    "dataType1",
    "dataType10",
    "dataType11",
    "dataType13",
    "dataType14",
    "dataType16",
    "dataType17",
    "dataType18",
    "dataType19",
    "dataType2",
    "dataType20",
    "dataType21",
    "dataType22",
    "dataType3",
    "dataType4",
    "dataType5",
    "dataType6",
    "dataType7",
    "dataType8",
    "erklaerungType",
    "erklaerungType12",
    "erklaerungType15",
    "erklaerungType9",
    "i_allergies_dataType",
    "i_current_medication_dataType",
    "i_current_problems_dataType",
    "i_family_problems_dataType",
    "i_past_medication_dataType",
    "i_past_problems_dataType",
    "i_procedures_dataType",
    "i_results_dataType",
    "i_socialhistory_dataType",
    "i_vitalsigns_dataType",
    "v_allergies_dataType",
    "v_current_medication_dataType",
    "v_current_problems_dataType",
    "v_family_problems_dataType",
    "v_past_medication_dataType",
    "v_past_problems_dataType",
    "v_procedures_dataType",
    "v_results_dataType",
    "v_socialhistory_dataType",
    "v_vitalsigns_dataType",
    "vidi"
]
