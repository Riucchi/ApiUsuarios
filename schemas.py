from pydantic import BaseModel
from . import models
from typing import List, Any

class ProductBase(BaseModel):
    id: int
    name: str
    brand: str
    stock: int
    price: int
    product: Any = None


    class config:
        orm_mode = True
        arbitrary_types_allowed = True
    
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if isinstance(v, models.Product):
            return {
                "id": v.id,
                "name": v.name,
                "brand": v.brand,
                "stock": v.stock,
                "price": v.price,
            }
        return v



class UserBase(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    hotmail: str
    products: List[ProductBase] = []

    class Config:
        form_attributes = True
        orm_mode = True

    