import uvicorn

from fastapi import FastAPI , APIRouter
from fastapi.middleware.cors import CORSMiddleware

from api.router import api_router
from core.conf import settings
from database.database import Database

root_router = APIRouter()
app = FastAPI(title="Test")

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)

if __name__ == '__main__':
    
    try:
        print("Connecting to Database....")
        Database(settings.DSN)
        
        print("Running Uvicorn....")
        uvicorn.run(
            app="main:app",
            host="0.0.0.0",
            port=8081,
            reload="True",
        )
        
    except Exception as e:
        print(f"Can't Start API due to : {e}")
        