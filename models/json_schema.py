from pydantic import BaseModel, ValidationError
from typing import List

class GeneratedJSON(BaseModel):
    description: str
    keyRequirements: List[str]

