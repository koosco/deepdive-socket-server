from fastapi import FastAPI

from repository import models
from routers.api_router import router as api_router
from routers.websocket_router import router as websocket_router
from config.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(websocket_router)
app.include_router(api_router)