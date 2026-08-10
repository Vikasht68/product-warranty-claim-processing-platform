from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product_schema import ProductCreate


def create_product(db: Session, product_data: ProductCreate):
    existing_product = db.query(Product).filter(
        Product.serial_number == product_data.serial_number
    ).first()

    if existing_product:
        return None

    product = Product(
        name=product_data.name,
        brand=product_data.brand,
        serial_number=product_data.serial_number,
        purchase_date=product_data.purchase_date,
        warranty_expiry=product_data.warranty_expiry,
        user_id=product_data.user_id
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def get_user_products(db: Session, user_id: int):
    return db.query(Product).filter(
        Product.user_id == user_id
    ).all()


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(
        Product.id == product_id
    ).first()


def update_product(
    db: Session,
    product_id: int,
    product_data: ProductCreate
):
    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if product is None:
        return None

    existing_product = db.query(Product).filter(
        Product.serial_number == product_data.serial_number,
        Product.id != product_id
    ).first()

    if existing_product:
        return "duplicate"

    product.name = product_data.name
    product.brand = product_data.brand
    product.serial_number = product_data.serial_number
    product.purchase_date = product_data.purchase_date
    product.warranty_expiry = product_data.warranty_expiry
    product.user_id = product_data.user_id

    db.commit()
    db.refresh(product)

    return product


def delete_product(db: Session, product_id: int):
    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if product is None:
        return None

    db.delete(product)
    db.commit()

    return product