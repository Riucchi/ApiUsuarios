from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import User
from dependencies import get_db
from schemas import UserBase
from typing import List
from crud import get_user

app = FastAPI()

@app.get("/users", response_model=List[UserBase])
async def get_users(db: Session = Depends(get_db)):
    try:
        users = db.query(User).all()
        return users
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    


    
@app.get("/users/{user_id}", response_model=UserBase)
async def ver_usuario(user_id = int, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404,detail="Usuario inexistente")
    return user



@app.post("/users", response_model=UserBase)
async def create_user(user: UserBase, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.hotmail == user.hotmail).first()

    if db_user:
        raise HTTPException(status_code=400, detail="El Email ya esta registrado")
    
    new_user = User(**user.dict(exclude_unset=True))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.put("/users/{user_id}", response_model=UserBase)
async def editar_usuario(user_id : int, user: UserBase, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)

    if db_user is None:

        raise HTTPException(status_code=404, detail="Usuario inexistente.")
    
    user_data = user.dict(exclude_unset=True)

    for key, value in user_data.items():
        setattr(db_user, key, value)
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



@app.delete("/users/{user_id}")
async def delete_user(user: UserBase, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user.id).first()
    if not user:
        raise HTTPException(status_code=404,detail="usuario no encontrado")
    db.delete(user)
    db.commit()
    return {"mensaje": "Usuario Eliminado Exitosamente"}





