from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    hotmail: str

    class Config:
        form_attributes = True
