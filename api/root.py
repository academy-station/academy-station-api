from fastapi import APIRouter
from .paper import api_paper
from .user import api_user

api_root = APIRouter()
api_root.include_router(api_paper, prefix="/paper")
api_root.include_router(api_user, prefix="/user")
