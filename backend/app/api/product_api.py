from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.product_schema import ProductCreate, ProductResponse

from app.services.product_service import (
    create_product,
    get_user_products,
    get_product,
    update_product,
    delete_product
)


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("/", response_model=ProductResponse)
def add_product(
    product_data: ProductCreate,
    db: Session = Depends(get_db)
):
    product = create_product(db, product_data)

    if product is None:
        raise HTTPException(
            status_code=400,
            detail="Serial number already exists"
        )

    return product


@router.get(
    "/user/{user_id}",
    response_model=list[ProductResponse]
)
def get_products(
    user_id: int,
    db: Session = Depends(get_db)
):
    return get_user_products(db, user_id)


@router.get(
    "/{product_id}",
    response_model=ProductResponse
)
def get_single_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = get_product(db, product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


@router.put(
    "/{product_id}",
    response_model=ProductResponse
)
def edit_product(
    product_id: int,
    product_data: ProductCreate,
    db: Session = Depends(get_db)
):
    product = update_product(
        db,
        product_id,
        product_data
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    if product == "duplicate":
        raise HTTPException(
            status_code=400,
            detail="Serial number already exists"
        )

    return product


@router.delete("/{product_id}")
def remove_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = delete_product(db, product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {
        "message": "Product deleted successfully",
        "product_id": product_id
    }