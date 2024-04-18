from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, foreign
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    age = Column(Integer, index=True)
    hotmail = Column(String, index=True)
    products = relationship("Product", back_populates="user", primaryjoin="User.id == foreign(Product.user_id)")

class Product(Base):
    __tablename__ = "Ropa"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    brand = Column(String, index=True)
    price = Column(Integer, index=True)
    stock = Column(Integer, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="products", primaryjoin="Product.user_id == User.id")