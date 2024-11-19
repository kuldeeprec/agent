from pydantic import BaseModel

class BRDModel(BaseModel):
    title: str
    description: str
    requirements: list[str]
