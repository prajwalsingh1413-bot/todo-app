from fastapi import APIRouter
from app.database import todo_collection
from app.schemas import Todo

router = APIRouter(prefix="/todos", tags=["Todos"])

@router.post("/")
def create_todo(todo: Todo):
    result = todo_collection.insert_one(todo.dict())
    return {"id": str(result.inserted_id)}

@router.get("/")
def get_todos():
    todos = []
    for t in todo_collection.find():
        t["_id"] = str(t["_id"])
        todos.append(t)
    return todos