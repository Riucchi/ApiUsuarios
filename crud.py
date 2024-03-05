from sqlalchemy.orm import Session
from ApiUsuarios.models import User

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()