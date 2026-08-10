from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import Base, engine

from app.models.user import User
from app.models.product import Product
from app.models.claim import Claim

from app.api.user_api import router as user_router
from app.api.product_api import router as product_router
from app.api.claim_api import router as claim_router


# Create database tables
Base.metadata.create_all(bind=engine)


# Create FastAPI application
app = FastAPI(
    title="Product Warranty Claim Platform",
    description="Product Warranty Claim Management System",
    version="1.0.0"
)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# API Routers
app.include_router(user_router)
app.include_router(product_router)
app.include_router(claim_router)


# Health check
@app.get("/")
def home():
    return {
        "message": "Product Warranty Claim Platform is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }