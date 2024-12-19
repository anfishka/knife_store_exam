from sqlalchemy.orm import Session
from app.models import Product
from typing import Tuple, List


def get_products_paginated(db: Session, page: int, page_size: int) -> Tuple[List[Product], int]:
    query = db.query(Product)
    total = query.count()
    products = query.offset((page-1)*page_size).limit(page_size).all()
    return products, total

def get_product_by_id(db: Session, product_id: int) -> Product:
    return db.query(Product).filter(Product.id == product_id).first()

def create_product(db: Session, data) -> Product:
    product = Product(
        name=data.name,
        price=data.price,
        description=data.description,
        images=["/static/images/knife1.jpg"]
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def update_product(db: Session, product_id: int, data) -> Product:
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        return None
    product.name = data.name
    product.price = data.price
    product.description = data.description
    db.commit()
    db.refresh(product)
    return product

def delete_product(db: Session, product_id: int) -> None:
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
