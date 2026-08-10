from sqlalchemy import Column, Integer, String, Date

from app.database.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    brand = Column(
        String,
        nullable=False
    )

    serial_number = Column(
        String,
        unique=True,
        nullable=False
    )

    purchase_date = Column(
        Date,
        nullable=False
    )

    warranty_expiry = Column(
        Date,
        nullable=False
    )

    user_id = Column(
        Integer,
        nullable=False
    )