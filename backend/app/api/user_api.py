from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.user_schema import (
    UserCreate,
    UserLogin,
    UserResponse
)

from app.services.user_service import (
    create_user,
    login_user
)


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# =========================
# REGISTER
# =========================

@router.post(
    "/register",
    response_model=UserResponse
)
def register_user(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):

    user = create_user(
        db,
        user_data
    )

    if user is None:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return user


# =========================
# LOGIN
# =========================

@router.post(
    "/login",
    response_model=UserResponse
)
def login(
    user_data: UserLogin,
    db: Session = Depends(get_db)
):

    user = login_user(
        db,
        user_data.email,
        user_data.password
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return user