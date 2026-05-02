from fastapi import FastAPI
from app.routes import todo

app = FastAPI()

app.include_router(todo.router)