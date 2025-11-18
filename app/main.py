from fastapi import FastAPI
from app.routes import users, task
from app.db.database import engine
from app.models import user_models


app = FastAPI(
    title="Taskflow",
    version="1.0"
)

app.include_router(users.router)
user_models.Base.metadata.create_all(bind=engine)