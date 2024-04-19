import sys
sys.path.insert(0, 'E://ProyectoAPI')


from fastapi import  Depends, HTTPException, APIRouter
from ApiUsuarios.dependencies import get_db
from ApiUsuarios.models import Product
from ApiUsuarios.crud import get_product
from ApiUsuarios.schemas import ProductBase
from typing import List
from sqlalchemy.orm import Session


router = APIRouter()



@router.get("/products", response_model=List[ProductBase])
async def get_all_products(db: Session = Depends(get_db)):
    try:
        products = db.query(Product).all()
        return products
    except Exception as e:
        raise HTTPException(status_code=404,detail=str(e))
    


    
@router.get("/product/{product_id}", response_model=ProductBase)
async def ver_producto(product_id = int, db:Session = Depends(get_db)):
    user = db.query(Product).filter(Product.id == product_id).first()
    if user is None:
        raise HTTPException(status_code=404,detail="Producto Inexistente.")
    return user






@router.post("/product", response_model=ProductBase)
async def create_product(product: ProductBase, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == Product.id).first()

    if db_product:
        raise HTTPException(status_code=400, detail="El Producto ya Existe.")
    
    new_product = Product(**product.dict(exclude_unset=True))
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product







@router.put("/products/{product_id}", response_model=ProductBase)
async def edit_product(product_id : int, product: ProductBase, db: Session = Depends(get_db)):
    db_product = get_product(db, product_id=product_id)

    if db_product is None:

        raise HTTPException(status_code=404, detail="Producto inexistente.")
    
    product_data = product.dict(exclude_unset=True)

    for key, value in product_data.items():
        setattr(db_product, key, value)
    
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product



@router.delete("/product/{product_id}")
async def delete_user(product: ProductBase, db:Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product.id).first()
    if not product:
        raise HTTPException(status_code=404,detail="Producto no encontrado")
    db.delete(product)
    db.commit()
    return {"mensaje": "Producto Eliminado Exitosamente."}