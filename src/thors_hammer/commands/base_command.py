from typing import get_type_hints, Union, Optional
import xml.etree.ElementTree as ET

from thors_hammer.utils.parser import Parser

class OCIType:
    # Base class for Broadworks types
    namespace = "C"

    # Handles dataclass default initialisation
    def __init__(self, **kwargs):
        annotations = get_type_hints(self.__class__)
        for key, value in kwargs.items():
            if key not in annotations:
                raise ValueError(f"Unknown field: {key}")
            setattr(self, key, value)

        for key in annotations:
            if not hasattr(self, key):
                setattr(self, key, None)

    def to_dict(self) -> dict:
        return Parser.to_dict_from_class(self)

    def to_xml(self) -> str:
        return Parser.to_xml_from_class(self)

    @classmethod
    def from_dict(cls, data: dict) -> 'OCIType':
        return Parser.to_class_from_dict(data, cls)

    @classmethod
    def from_xml(cls, xml: Union[str, ET.Element]) -> 'OCIType':
        return Parser.to_class_from_xml(xml, cls)

class OCICommand(OCIType):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class OCITable:
    pass

class OCIRequest(OCICommand):
    pass

class OCIResponse(OCICommand):
    pass

class OCIDataResponse(OCIResponse):
    pass

class SuccessResponse(OCIResponse):
    pass

class ErrorResponse(OCIResponse):
    errorCode: Optional[int] = None
    summary: str
    summaryEnglish: str
    detail: Optional[str] = None
