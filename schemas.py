from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    surname: str
    age: int
    hotmail: str

    class Config:
        orm_mode = True
