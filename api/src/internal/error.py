from pydantic import BaseModel

class ErrorDetails(BaseModel):
    error: str
    status_code: int