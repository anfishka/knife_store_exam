from pydantic import BaseModel, Field, conlist
from typing import List, Optional
from typing import Annotated

class ProductImageOut(BaseModel):
    id: int
    image_path: str

    class Config:
        orm_mode = True

class ProductOut(BaseModel):
    id: int
    name: str
    price: float
    description: str
    images: List[ProductImageOut]

    class Config:
        orm_mode = True

class ProductCreate(BaseModel):
    name: str
    price: float
    description: str
    images: Annotated[List[str], Field(default_factory=list, max_items=8)]

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    images: Optional[List[str]] = None

class LoginData(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
