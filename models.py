from sqlalchemy import Column, Integer, String
from ApiUsuarios.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    age = Column(Integer, index=True)
    hotmail = Column(String, index=True)

