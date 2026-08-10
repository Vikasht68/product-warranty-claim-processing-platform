from pydantic import BaseModel
from datetime import datetime


class ClaimCreate(BaseModel):
    product_id: int
    user_id: int
    issue: str


class ClaimResponse(BaseModel):
    id: int
    product_id: int
    user_id: int
    issue: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True