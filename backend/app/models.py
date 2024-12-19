from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    description = Column(Text)

    images = relationship("ProductImage", back_populates="product")

class ProductImage(Base):
    __tablename__ = "product_images"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"))
    image_path = Column(String, nullable=False)  # путь к файлу или URL

    product = relationship("Product", back_populates="images")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    role = Column(String)  # "admin" or "user"
