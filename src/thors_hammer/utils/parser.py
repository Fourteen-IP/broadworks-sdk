# Responsible for parsing data between types such as JSON, XML and Classes

# Design not fully fleshed out yet
import asyncio
from concurrent.futures import ThreadPoolExecutor
import xml.etree.ElementTree as ET
from typing import get_type_hints, List, get_args, Union, Type


class Parser:
    """
    Base Class For OCI Object Parsing & Type Translation

    method table:

    - to_xml_from_class: Translates class object to xml
    - to_xml_from_dict: Translates dictionary object to xml
    - to_dict_from_class: Translates class object to dictionary
    - to_dict_from_xml: Translates xml into dictionary
    - to_class_from_dict: Translates dictionary object to class
    - to_class_from_xml: Translates xml to class
    """

    @staticmethod
    def to_xml_from_class(obj: object) -> str:
        def serialize_value(parent, tag, value):
            if type(value).__name__ == "OCIType":
                child = ET.SubElement(parent, tag)
                data = Parser.to_dict_from_class(value)
                for k, v in data.items():
                    if v is not None:
                        ET.SubElement(child, k).text = str(v)
            else:
                ET.SubElement(parent, tag).text = str(value)

        root = ET.Element(
            "command",
            attrib={
                "xmlns": "",
                "{http://www.w3.org/2001/XMLSchema-instance}type": obj.__class__.__name__,
            },
        )

        type_hints = get_type_hints(obj.__class__)
        for attr, hint in type_hints.items():
            value = getattr(obj, attr, None)
            if value is None:
                continue

            args = get_args(hint)
            if args:
                origin = getattr(hint, "__origin__", None)
                if origin in (list, List):
                    for item in value:
                        serialize_value(root, attr, item)
                    continue

            serialize_value(root, attr, value)

        return ET.tostring(root, encoding="utf-8", xml_declaration=False).decode(
            "utf-8"
        )

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
            origin = getattr(hint, "__origin__", None)
            if origin in (list, List):
                result[attr] = []
                for item in value:
                    result[attr].append(
                        Parser.to_dict_from_class(item)
                        if type(value).__name__ == "OCIType"
                        else item
                    )
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

        if xml.attrib:
            result["attributes"] = dict(xml.attrib)

        children = list(xml)
        if children:
            for child in children:
                child_dict = Parser.to_dict_from_xml(child)

                if child.tag in result:
                    if isinstance(result[child.tag], list):
                        result[child.tag].append(child_dict)
                    else:
                        result[child.tag] = [result[child.tag], child_dict]
                else:
                    result[child.tag] = child_dict
        else:
            text = xml.text.strip() if xml.text else ""
            if result:
                result["text"] = text
            else:
                result = text

        return result

    @staticmethod
    def to_class_from_dict(data: dict, cls: Type) -> object:
        type_hints = get_type_hints(cls)
        init_args = {}

        for key, hint in type_hints.items():
            if key not in data.get("command"):
                continue

            value = data.get("command")[key]
            args = get_args(hint)
            origin = getattr(hint, "__origin__", None)

            if origin in (list, List):
                subtype = args[0]
                init_args[key] = [
                    Parser.to_class_from_dict(v, subtype) if isinstance(v, dict) else v
                    for v in value
                ]
            elif isinstance(value, dict) and hint.__name__ == "OCIType":
                init_args[key] = Parser.to_class_from_dict(value, hint)
            else:
                init_args[key] = value

        return cls(**init_args)

    @staticmethod
    def to_class_from_xml(xml: Union[str, ET.Element], cls: Type) -> object:
        return Parser.to_class_from_dict(Parser.to_dict_from_xml(xml), cls)


class AsyncParser:
    """
    Base Class For Async OCI Object Parsing & Type Translation

    method table:

    - to_xml_from_class: Translates class object to xml
    - to_xml_from_dict: Translates dictionary object to xml
    - to_dict_from_class: Translates class object to dictionary
    - to_dict_from_xml: Translates xml into dictionary
    - to_class_from_dict: Translates dictionary object to class
    - to_class_from_xml: Translates xml to class
    """

    _executor = ThreadPoolExecutor(max_workers=4, thread_name_prefix="async_parser")

    @staticmethod
    def _get_loop():
        return asyncio.get_event_loop()

    @staticmethod
    async def to_xml_from_class(obj: object) -> str:
        return await AsyncParser._get_loop().run_in_executor(
            AsyncParser._executor, Parser.to_xml_from_class, obj
        )

    @staticmethod
    async def to_xml_from_dict(data: dict, cls: Type) -> str:
        return await AsyncParser._get_loop().run_in_executor(
            AsyncParser._executor, Parser.to_xml_from_dict, data, cls
        )

    @staticmethod
    async def to_dict_from_class(obj: object) -> dict:
        return await AsyncParser._get_loop().run_in_executor(
            AsyncParser._executor, Parser.to_dict_from_class, obj
        )

    @staticmethod
    async def to_dict_from_xml(xml: Union[str, ET.Element]) -> dict:
        return await AsyncParser._get_loop().run_in_executor(
            AsyncParser._executor, Parser.to_dict_from_xml, xml
        )

    @staticmethod
    async def to_class_from_dict(data: dict, cls: Type) -> object:
        return await AsyncParser._get_loop().run_in_executor(
            AsyncParser._executor, Parser.to_class_from_dict, data, cls
        )

    @staticmethod
    async def to_class_from_xml(xml: Union[str, ET.Element], cls: Type) -> object:
        return await AsyncParser._get_loop().run_in_executor(
            AsyncParser._executor, Parser.to_class_from_xml, xml, cls
        )
