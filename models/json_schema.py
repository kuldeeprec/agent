from pydantic import BaseModel, ValidationError
from typing import List

from pydantic import BaseModel
from typing import List, Dict, Union, Optional

class DisplayConfiguration(BaseModel):
    defaultDisplayName: str
    isMainField: str
    isVisible: str

class OptionValue(BaseModel):
    value: str
    key: int

class ColumnConfiguration(BaseModel):
    name: str
    key: str
    dataType: str
    aggregates: Optional[bool] = None
    optionValues: Optional[List[OptionValue]] = None

class TableConfiguration(BaseModel):
    rows: List[Dict]
    columns: List[ColumnConfiguration]
    rowLimit: Optional[int] = None

class FrequencyConfiguration(BaseModel):
    discountPeriod: int
    discountPeriodInWords: str

class DiscountConfiguration(BaseModel):
    applicableDiscountWindow: Dict[str, str]
    frequencyConfiguration: Dict[str, FrequencyConfiguration]
    discountType: str
    defaultFrequency: str
    acceptedFrequencyList: List[str]

class Attribute(BaseModel):
    displayConfiguration: Optional[DisplayConfiguration]
    isBasicInfo: Optional[bool] = None
    attributeType: str
    dataType: str
    key: str
    value: Optional[Union[str, float, List[Dict]]] = None
    tableConfiguration: Optional[TableConfiguration] = None
    optionValues: Optional[List[OptionValue]] = None
    discountConfiguration: Optional[DiscountConfiguration] = None

class GeneratedJSON(BaseModel):
    description: str
    keyRequirements: List[str]
    SK: str
    UpdatedTime: int
    PK: str
    Definitions: Dict[str, List[Attribute]]


