from pydantic import BaseModel

class SuccessMessage(BaseModel):
    success: bool

class DescriptiveSuccessMessage(BaseModel):
    success: bool
    message: str