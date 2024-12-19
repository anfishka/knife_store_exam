from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from ..services.product_service import get_products_paginated, get_product_by_id

router = APIRouter()

@router.get("/")
def list_products(page: int = 1, db: Session = Depends(get_db)):
    products, total = get_products_paginated(db, page=page, page_size=12)
    return {"data": products, "total": total, "page": page}

@router.get("/{product_id}")
def product_detail(product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(404, detail="Product not found")
    return product
