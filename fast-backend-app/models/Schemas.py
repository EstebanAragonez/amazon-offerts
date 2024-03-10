from typing import Optional
from pydantic import BaseModel, HttpUrl
from datetime import date

class DataLoadLog(BaseModel):
    id:Optional[int]
    date:Optional[date]

class ProductDealCreate(BaseModel):
    title: str
    price: Optional[int]
    total_rating: Optional[int]
    img: HttpUrl
    discount: Optional[int]
    url: HttpUrl

class ProductDeal(BaseModel):
    id: int
    title: str
    price: Optional[int]
    total_rating: Optional[int]
    img: HttpUrl
    discount: Optional[int]
    url: HttpUrl
    date: Optional[str]

    class Config:
        orm_mode = True