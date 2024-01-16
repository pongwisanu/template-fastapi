from fastapi import APIRouter , Security

from core.conf import settings

from middleware.authen import get_api_key

from database.database import Database


router = APIRouter()

db = Database(settings.DSN)

@router.get("/")
def Index():
    return {"Hello": "World"}

@router.get("/get/{name}")
def GetSharepointDetail(name :str):
    return ""

@router.post("/gets")
def GetUserModel(api_key: str = Security(get_api_key)):
    return ""