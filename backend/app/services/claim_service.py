from sqlalchemy.orm import Session

from app.models.claim import Claim
from app.schemas.claim_schema import ClaimCreate


def create_claim(db: Session, claim_data: ClaimCreate):
    claim = Claim(
        product_id=claim_data.product_id,
        user_id=claim_data.user_id,
        issue=claim_data.issue,
        status="Pending"
    )

    db.add(claim)
    db.commit()
    db.refresh(claim)

    return claim


def get_user_claims(db: Session, user_id: int):
    return db.query(Claim).filter(
        Claim.user_id == user_id
    ).all()


def get_claim(db: Session, claim_id: int):
    return db.query(Claim).filter(
        Claim.id == claim_id
    ).first()


def update_claim_status(
    db: Session,
    claim_id: int,
    status: str
):
    claim = db.query(Claim).filter(
        Claim.id == claim_id
    ).first()

    if not claim:
        return None

    claim.status = status

    db.commit()
    db.refresh(claim)

    return claim


def delete_claim(db: Session, claim_id: int):
    claim = db.query(Claim).filter(
        Claim.id == claim_id
    ).first()

    if not claim:
        return None

    db.delete(claim)
    db.commit()

    return claim