from sqlalchemy.orm import Session
from ApiUsuarios.models import User, Product

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def add_product_to_user(db: Session, user_id: int, product_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    product = db.query(Product).filter(Product.id == product_id).first()
    if user and product:
        user.products.append(product)
        db.commit()
        db.refresh(user)
        return user
    return None

def remove_product_from_user(db: Session, user_id: int, product_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    product = db.query(Product).filter(Product.id == product_id).first()
    if user and product:
        user.products.remove(product)
        db.commit()
        db.refresh(user)
        return user
    return None


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

