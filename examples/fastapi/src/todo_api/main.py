from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List

from todo_api.database import engine, Base, get_db
from todo_api.models import TodoItem

# Create the tables
Base.metadata.create_engine(bind=engine)

app = FastAPI(title="Todo API")

# Pydantic schemas
class TodoBase(BaseModel):
    title: str
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoResponse(TodoBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True

@app.get("/todos", response_model=List[TodoResponse])
def read_todos(db: Session = Depends(get_db)):
    return db.query(TodoItem).all()

@app.post("/todos", response_model=TodoResponse)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = TodoItem(title=todo.title, completed=todo.completed)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.get("/")
def root():
    return {"message": "Welcome to the Todo API. Go to /docs for Swagger documentation."}
