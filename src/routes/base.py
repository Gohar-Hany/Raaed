from fastapi import FastAPI , APIRouter , Depends
from helpers.config import get_settings , Settings


base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)

@base_router.get("/")
async def welcome(settings : Settings = Depends(get_settings)) :

    return {
        "APP_NAME"    : settings.APP_NAME,
        "APP_VERSION" : settings.APP_VERSION
    }