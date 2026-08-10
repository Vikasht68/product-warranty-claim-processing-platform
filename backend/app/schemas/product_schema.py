from pydantic import BaseModel
from datetime import date


class ProductCreate(BaseModel):
    name: str
    brand: str
    serial_number: str
    purchase_date: date
    warranty_expiry: date
    user_id: int


class ProductResponse(BaseModel):
    id: int
    name: str
    brand: str
    serial_number: str
    purchase_date: date
    warranty_expiry: date
    user_id: int

    class Config:
        from_attributes = True