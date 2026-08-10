from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.claim_schema import ClaimCreate, ClaimResponse
from app.services.claim_service import (
    create_claim,
    get_user_claims,
    get_claim,
    update_claim_status,
    delete_claim
)

router = APIRouter(
    prefix="/claims",
    tags=["Claims"]
)


# CREATE CLAIM
@router.post("/", response_model=ClaimResponse)
def add_claim(
    claim_data: ClaimCreate,
    db: Session = Depends(get_db)
):
    return create_claim(db, claim_data)


# READ ALL CLAIMS FOR USER
@router.get("/user/{user_id}", response_model=list[ClaimResponse])
def get_claims(
    user_id: int,
    db: Session = Depends(get_db)
):
    return get_user_claims(db, user_id)


# READ SINGLE CLAIM
@router.get("/{claim_id}", response_model=ClaimResponse)
def get_single_claim(
    claim_id: int,
    db: Session = Depends(get_db)
):
    claim = get_claim(db, claim_id)

    if claim is None:
        raise HTTPException(
            status_code=404,
            detail="Claim not found"
        )

    return claim


# UPDATE CLAIM STATUS
@router.put("/{claim_id}", response_model=ClaimResponse)
def edit_claim(
    claim_id: int,
    status: str,
    db: Session = Depends(get_db)
):
    claim = update_claim_status(
        db,
        claim_id,
        status
    )

    if claim is None:
        raise HTTPException(
            status_code=404,
            detail="Claim not found"
        )

    return claim


# DELETE CLAIM
@router.delete("/{claim_id}")
def remove_claim(
    claim_id: int,
    db: Session = Depends(get_db)
):
    claim = delete_claim(db, claim_id)

    if claim is None:
        raise HTTPException(
            status_code=404,
            detail="Claim not found"
        )

    return {
        "message": "Claim deleted successfully"
    }