from sqlalchemy.orm import Session
from app.models.user import User


def create_user(db: Session, user_data):
    existing_user = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if existing_user:
        return None

    user = User(
        name=user_data.name,
        email=user_data.email,
        password=user_data.password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(
        User.email == email
    ).first()


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)

    if user is None:
        return None

    if user.password != password:
        return None

    return user


def login_user(db: Session, email: str, password: str):
    return authenticate_user(db, email, password)