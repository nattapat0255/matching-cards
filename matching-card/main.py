from fastapi import FastAPI
from .database import engine
from .routers import game, user, authentication
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(game.router)