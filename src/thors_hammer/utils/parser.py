# Responsible for parsing data between types such as JSON, XML and Classes

# Design not fully fleshed out yet
import xml.etree.ElementTree as ET
from typing import get_type_hints, List, get_args, Union, Type

class Parser:
    @staticmethod
    def to_xml_from_class(obj: object) -> str:
        def serialize_value(parent, tag, value):
            if type(value).__name__ == "OCIType":
            # if isinstance(value, OCIType):
                child = ET.SubElement(parent, tag)
                data = Parser.to_dict_from_class(value)
                for k, v in data.items():
                    if v is not None:
                        ET.SubElement(child, k).text = str(v)
            else:
                ET.SubElement(parent, tag).text = str(value)

        root_tag = obj.__class__.__name__
        root = ET.Element(root_tag, xmlns=obj.namespace)

        type_hints = get_type_hints(obj.__class__)
        for attr, hint in type_hints.items():
            value = getattr(obj, attr, None)
            if value is None:
                continue

            args = get_args(hint)
            if args:
                origin = getattr(hint, '__origin__', None)
                if origin in (list, List):
                    for item in value:
                        serialize_value(root, attr, item)
                    continue

            serialize_value(root, attr, value)

        return ET.tostring(root, encoding="utf-8", xml_declaration=False).decode("utf-8")

    @staticmethod
    def to_xml_from_dict(data: dict, cls: Type) -> str:
        obj = Parser.to_class_from_dict(data, cls)
        return Parser.to_xml_from_class(obj)

    @staticmethod
    def to_dict_from_class(obj: object) -> dict:
        result = {}
        type_hints = get_type_hints(obj.__class__)
        for attr, hint in type_hints.items():
            value = getattr(obj, attr, None)
            if value is None:
                continue

            args = get_args(hint)
            origin = getattr(hint, '__origin__', None)
            if origin in (list, List):
                result[attr] = []
                for item in value:
                    result[attr].append(Parser.to_dict_from_class(item) if type(value).__name__ == "OCIType" else item)
            elif type(value).__name__ == "OCIType":
                result[attr] = Parser.to_dict_from_class(value)
            else:
                result[attr] = value
        return result

    @staticmethod
    def to_dict_from_xml(xml: Union[str, ET.Element]) -> dict:
        if isinstance(xml, str):
            xml = ET.fromstring(xml)

        result = {}
        for child in xml:
            # Handle nested elements
            if len(child):
                result[child.tag] = Parser.to_dict_from_xml(child)
            else:
                result[child.tag] = child.text
        return result

    @staticmethod
    def to_class_from_dict(data: dict, cls: Type) -> object:
        type_hints = get_type_hints(cls)
        init_args = {}

        for key, hint in type_hints.items():
            if key not in data:
                continue

            value = data[key]
            args = get_args(hint)
            origin = getattr(hint, '__origin__', None)

            if origin in (list, List):
                subtype = args[0]
                init_args[key] = [Parser.to_class_from_dict(v, subtype) if isinstance(v, dict) else v for v in value]
            elif isinstance(value, dict) and hint.__name__ == "OCIType":
                init_args[key] = Parser.to_class_from_dict(value, hint)
            else:
                init_args[key] = value

        return cls(**init_args)

    @staticmethod
    def to_class_from_xml(xml: Union[str, ET.Element], cls: Type) -> object:
        return Parser.to_class_from_dict(Parser.to_dict_from_xml(xml), cls)
