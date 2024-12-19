from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from ..core.security import get_current_admin_user
from ..services.product_service import create_product, update_product, delete_product
from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float
    description: str
    images: list[str] = []

class ProductUpdate(BaseModel):
    name: str
    price: float
    description: str
    images: list[str] = []

router = APIRouter()

@router.post("/products")
def admin_create_product(product_data: ProductCreate,
                         db: Session = Depends(get_db),
                         current_user = Depends(get_current_admin_user)):
    return create_product(db, product_data)

@router.put("/products/{product_id}")
def admin_update_product(product_id: int, product_data: ProductUpdate,
                         db: Session = Depends(get_db),
                         current_user = Depends(get_current_admin_user)):
    return update_product(db, product_id, product_data)

@router.delete("/products/{product_id}")
def admin_delete_product(product_id: int,
                         db: Session = Depends(get_db),
                         current_user = Depends(get_current_admin_user)):
    delete_product(db, product_id)
    return {"detail": "Deleted"}
