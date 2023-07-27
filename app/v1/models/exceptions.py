from pydantic import BaseModel


class ExceptionModel(BaseModel):
    error: str
