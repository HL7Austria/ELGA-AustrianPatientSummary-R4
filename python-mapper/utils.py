import datetime
import inspect
import typing
import decimal
import io
import json
from html import escape as html_escape
from html.parser import HTMLParser

class dateString(str): # wrapper for strings that should be in iso datetime format
    pass

class dateStringV3(str): # wrapper for strings that should be in v3 datetime format
    pass

def _handle_tr(tr):
    html = ""
    attrs = ""
    if tr.ID:
        attrs += ' id="%s"' % tr.ID
    if tr.styleCode:
        attrs += f' class="{tr.styleCode}"'
    html += "<tr %s>" % attrs
    for th in tr.th:
        html += _handle_tdh(th, "th")
    for td in tr.td:
        html += _handle_tdh(td, "td")
    html += "</tr>"
    return html

def _handle_tdh(tdh, tag):
    html = ""
    attrs = ""
    if tdh.ID:
        attrs += ' id="%s"' % tdh.ID
    if tdh.styleCode:
        attrs += f' class="{tdh.styleCode}"'
    html += f"<{tag}%s>" % attrs
    html += _handle_content(tdh)
    html += f"</{tag}>"
    return html

def _handle_content(elem):
    html = ""
    for content in elem.content_:
        if content.category == 1:
            html += html_escape(content.value)
        elif content.category == 2:
            if content.name == "br":
                html += f'<br />'
            else:
                html += f"[[unhandled simple content {content.name}]]"
        elif content.category == 3:
            attrs = ""
            if getattr(content.value, "ID", None):
                attrs += ' id="%s"' % content.value.ID 
            if content.name == "table":
                html += "<table%s><thead>" % attrs
                for tr in content.value.thead.tr:
                    html += _handle_tr(tr)
                html += "</thead>"
                if content.value.tfoot:
                    html += "<tfoot>"
                    for tr in content.value.tfoot.tr:
                        html += _handle_tr(tr)
                    html += "</tfoot>"
                html += "<tbody>"
                for tr in content.value.tbody[0].tr:
                    html += _handle_tr(tr)
                html += "</tbody></table>"
            elif content.name == "content":
                if content.value.styleCode == "Italics":
                    attrs += ' class="italics"'
                elif content.value.styleCode:
                    attrs += f' class="{content.value.styleCode}"'
                html += "<span%s>" % attrs
                html += _handle_content(content.value)
                html += "</span>"
            elif content.name == "paragraph":
                if content.value.styleCode:
                    attrs += f' class="{content.value.styleCode}"'
                html += "<p%s>" % attrs
                html += _handle_content(content.value)
                html += "</p>"
            elif content.name == "sup":
                html += "<sup%s>" % attrs
                html += _handle_content(content.value)
                html += "</sup>"
            elif content.name == "footnote":
                html += '<span class="footnote"%s>' % attrs
                html += _handle_content(content.value)
                html += "</span>"
            elif content.name == "renderMultiMedia":
                html += f'<img src="{content.value.referencedObject}"%s />' % attrs
            elif content.name == "br":
                html += f'<br />'
            elif content.name == "caption":
                html += "<caption%s>" % attrs
                html += _handle_content(content.value)
                html += "</caption>"
            elif content.name == "list":
                if content.value.listType in [None, "unordered"]:
                    if content.value.styleCode:
                        attrs += f' style="list-style-type:{content.value.styleCode.lower()}"'
                    html += "<ul%s>" % attrs
                    for item in content.value.item:
                        html += "<li>"
                        html += _handle_content(item)
                        html += "</li>"
                    html += "</ul>"
                elif content.value.listType == "ordered":
                    styleCodeTrans = {"LittleRoman": "i", "BigRoman": "I", "LittleAlpha": "a", "BigAlpha": "A", "Arabic": "1"}
                    listType = styleCodeTrans.get(content.value.styleCode)
                    if listType:
                        attrs += f' type="{listType}"'
                    html += "<ol%s>" % attrs
                    for item in content.value.item:
                        html += "<li>"
                        html += _handle_content(item)
                        html += "</li>"
                    html += "</ol>"
            else:
                html += f"[[unhandled content {content.name}]]"
        else:
            html += f"[[unhandled category {content.category}]]"
    return html

def strucdoctext2html(module, strucdoctext):
    html = _handle_content(strucdoctext)
    div = module.Flow(content_=[module.MixedContainer(1, 0, "", html)])
    div.original_tagname_ = "div"
    div.valueOf_ = ""
    return div

def ed2html(module, ed):
    # TODO: improve
    div = module.Flow(content_=[module.MixedContainer(1, 0, "", f"<v3:reference>{ed.reference.value}</v3:reference>")])
    div.original_tagname_ = "div"
    div.valueOf_ = ""
    return div

def ed2markdown(module, ed):
    # TODO: improve
    return module.markdown(value=f"<v3:reference>{ed.reference.value}</v3:reference>")

def strucdoctext2markdown(module, strucdoctext):
    # TODO: implement properly

    class MLStripper(HTMLParser):
        def __init__(self):
            super().__init__()
            self.reset()
            self.strict = False
            self.convert_charrefs= True
            self.text = io.StringIO()
        def handle_data(self, d):
            self.text.write(d)
        def get_data(self):
            return self.text.getvalue()

    html = _handle_content(strucdoctext)
    s = MLStripper()
    s.feed(html)
    return module.markdown(value=s.get_data())


def builddiv(module, content):
    div = module.Flow(content_=[module.MixedContainer(1, 0, "", content)])
    div.original_tagname_ = "div"
    div.valueOf_ = ""
    return div

def exportJsonAttributesResource(self, json_dict):
    if self.__class__.__name__ == "PythonGenerator":
        json_dict["resourceType"] = self.__class__.__bases__[0].__name__
    else:
        json_dict["resourceType"] = self.__class__.__name__

def exportJsonResultResourceContainer(self, json_dict, parent_dict, key, is_list):
    if json_dict:
        return list(json_dict.values())[0]
    else:
        return None

def exportJsonResultNarrative(self, json_dict, parent_dict, key, is_list):
    divf = io.StringIO()
    if self.div:
        self.div.export(divf, 0)
        json_dict["div"] = divf.getvalue()
    return json_dict

def exportJsonAttributesDateDateTime(self, json_dict):
    if self.id is not None:
        json_dict['id'] = self.id
    if self.value is not None:
        json_dict['value'] = self.value if isinstance(self.value, str) else self.value.isoformat()

class number_str(float):
    def __init__(self, o):
        self.o = o
    def __repr__(self):
        return str(self.o)

def exportJsonResultElement(self, json_dict, parent_dict, key, is_list, sub_defs=[], attr_defs=[]):
    if sub_defs == ["value"]:
        value = json_dict.pop("value", None)
        if json_dict:
            key = "_" + key
            if is_list:
                if key not in parent_dict:
                    parent_dict[key] = []
                parent_dict[key].append(json_dict)
            else:
                parent_dict[key] = json_dict
        if self.__class__.__name__ == "decimal":
            return number_str(value)
        elif self.__class__.__name__ == "dateTime":
            if isinstance(value, datetime.datetime):
                return value.isoformat()
            else:
                return value
        elif self.__class__.__name__ == "date":
            if isinstance(value, datetime.datetime):
                return value.date().isoformat()
            elif isinstance(value, datetime.date):
                return value.isoformat()
            else:
                return value
        elif self.__class__.__name__ == "time":
            return value.isoformat("seconds")
        else:
            return value
    else:
        return json_dict

def parse_json_primitive(module, val, type_str):
    if type_str == "div":
        return module.parseString(val.replace("<div", "<div xmlns:v3='urn:hl7-org:v3'"), silence=True)
    elif not type_str.endswith("_primitive"):
        elem_clazz = getattr(module, type_str)
        ann_elem = inspect.get_annotations(elem_clazz.__init__)
        prim_type = ann_elem["value"]
    else:
        prim_type = type_str
    if prim_type == "instant_primitive":
        val = datetime.datetime.fromisoformat(val)
    if not type_str.endswith("_primitive"):
        return elem_clazz(value=val)
    else:
        return val

def parse_json(module, dct, class_name=None):
    if "resourceType" in dct:
        clazz = getattr(module, dct["resourceType"])
    else:
        clazz = getattr(module, class_name.replace(".", "_"))
    ann = inspect.get_annotations(clazz.__init__)
    clazz = clazz.subclass or clazz
    kwargs = {}
    sortedDict = dict(sorted(dct.items(), key=lambda item: item[0], reverse=True))
    for elem, val in sortedDict.items():
        if elem == "type":
            elem = "type_"
        elif elem == "class":
            elem = "class_"
        if elem != "resourceType":
            if isinstance(val, list):
                if elem.startswith("_"):
                    for idx, el in enumerate(val):
                        exts = []
                        for ext in el["extension"]:
                            exts.append(parse_json(module, ext, class_name="Extension"))
                        kwargs[elem[1:]][idx].extension = exts
                else:
                    type_str = typing.get_args(ann[elem])[0].__forward_arg__
                    lst = []
                    for el in val:
                        if isinstance(el, dict):
                            lst.append(parse_json(module, el, class_name=type_str))
                        else:
                            lst.append(parse_json_primitive(module, el, type_str))
                    kwargs[elem] = lst
            elif isinstance(val, dict):
                if elem.startswith("_"):
                    exts = []
                    for ext in val["extension"]:
                        exts.append(parse_json(module, ext, class_name="Extension"))
                    kwargs[elem[1:]].extension = exts
                else:
                    if ann[elem] == "ResourceContainer":
                        kkwargs = { val["resourceType"]: parse_json(module, val, class_name=ann[elem]) }
                        container = module.ResourceContainer(**kkwargs)
                        for val in kkwargs.values():
                            if hasattr(val, "parent_object_"):
                                val.parent_object_ = container
                        kwargs[elem] = container
                    else:
                        kwargs[elem] = parse_json(module, val, class_name=ann[elem])
            else:
                kwargs[elem] = parse_json_primitive(module, val, ann[elem])
    fhir_res = clazz(**kwargs)
    fhir_res.gds_elementtree_node_ = dct
    dct["@node"] = fhir_res
    for val in kwargs.values():
        if isinstance(val, list):
            for v in val:
                if hasattr(v, "parent_object_"):
                    v.parent_object_ = fhir_res
        elif hasattr(val, "parent_object_"):
            val.parent_object_ = fhir_res
    return fhir_res

def qty_from_str(module, qty_str):
    parts = qty_str.split(" ")
    value = parts[0]
    comparator = None
    if value.startswith("<=") or value.startswith(">="):
        comparator = value[:2]
        value = value[2:]
    elif value.startswith("<") or value.startswith(">"):
        comparator = value[:1]
        value = value[1:]
    unit = parts[1]
    qty = module.Quantity(value=module.decimal(value=value), unit=module.string(value=unit))
    if comparator:
        qty.comparator = module.code(value=comparator)
    return qty

def get_type(var_type, element, type_str=None):
    is_list = False
    if var_type:
        if element:
            if not type_str:
                try:
                    type_str = inspect.get_annotations(var_type.__init__)[element]
                except BaseException:
                    try:
                        type_str = inspect.get_annotations(var_type.__init__)[element + "_"]
                    except BaseException:
                        if element == "data":
                            type_str = "string"
                        else:
                            return None, is_list
            if not isinstance(type_str, str):
                is_list = True
                type_str = typing.get_args(type_str)[0].__forward_arg__

            module = get_module(var_type)
            if var_type.__name__ in ["TS"]:
                var_type = dateStringV3
            elif type_str in ["string", "token", "uid", "anyURI"]:
                var_type = getattr(module, "string", str)
            elif type_str == "boolean":
                var_type = getattr(module, "boolean", bool)
            elif type_str == "integer":
                var_type = getattr(module, "integer", int)
            elif type_str == "base64Binary":
                var_type = getattr(module, "base64Binary", str)
            elif type_str in ["st", "cs", "string_primitive", "code_primitive", "uri_primitive", "url_primitive", "uuid_primitive", "canonical_primitive", "oid_primitive", "SampledDataDataType_primitive", "id_primitive", "markdown_primitive", "base64Binary_primitive", "hl7_oid", "hl7_st", "NMTOKEN", "xs_string", "xs_NMTOKEN", "xs_NMTOKENS"]:
                var_type = str
            elif type_str in ["bool", "boolean_primitive"]:
                var_type = bool
            elif type_str in ["int", "integer_primitive", "unsignedInt_primitive", "positiveInt_primitive"]:
                var_type = int
            elif type_str == "time_primitive":
                var_type = datetime.time
            elif type_str == "instant_primitive":
                var_type = datetime.datetime
            elif type_str in ["dateTime_primitive", "date_primitive"]:
                var_type = dateString
            elif type_str in ["real", "decimal_primitive"]:
                var_type = decimal.Decimal
            elif type_str in ["EntityNamePartQualifier", "set_EntityNamePartQualifier", "ActMood", "ContextControl", "ActClass", "RoleClassAssociative"]:
                # TODO genDs check why this class is not generated
                var_type = getattr(module, "CS")
            elif type_str.startswith("set_"):
                var_type = getattr(module, type_str[4:]) # TODO genDS check why lists aka "set_*" are not generated
            elif type_str in getattr(module, "GDSClassesMapping", {}):
                var_type = getattr(module, "GDSClassesMapping")[type_str]
            else:
                try:
                    var_type = getattr(module, type_str.replace(".", "_"))
                except:
                    var_type = getattr(module, type_str.replace(".", "_").upper())
    return var_type, is_list

def get_module(var_type):
    mod_split = var_type.__module__.split(".")
    return getattr(__import__(".".join(mod_split[0:-1]), fromlist=[mod_split[-1]]), mod_split[-1])
