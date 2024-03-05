import sys
sys.path.insert(0, 'E://ProyectoAPI')

from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ApiUsuarios.models import User
from ApiUsuarios.dependencies import get_db
from ApiUsuarios.models import User
from ApiUsuarios.schemas import UserBase
from typing import List
from ApiUsuarios.crud import get_user

router = APIRouter()

@router.get("/users", response_model=List[UserBase])
async def get_users(db: Session = Depends(get_db)):
    try:
        users = db.query(User).all()
        return users
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    


    
@router.get("/users/{user_id}", response_model=UserBase)
async def ver_usuario(user_id = int, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404,detail="Usuario inexistente")
    return user



@router.post("/users", response_model=UserBase)
async def create_user(user: UserBase, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.hotmail == user.hotmail).first()

    if db_user:
        raise HTTPException(status_code=400, detail="El Email ya esta registrado")
    
    new_user = User(**user.dict(exclude_unset=True))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.put("/users/{user_id}", response_model=UserBase)
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



@router.delete("/users/{user_id}")
async def delete_user(user: UserBase, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user.id).first()
    if not user:
        raise HTTPException(status_code=404,detail="usuario no encontrado")
    db.delete(user)
    db.commit()
    return {"mensaje": "Usuario Eliminado Exitosamente"}





