from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from database import (
    create_todo,
    read_all_todos,
    read_one_todo,
    remove_todo,
    update_todo,
)
from model import Todo

app = FastAPI()


origins = ["https://localhost:3000", "http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Ping": "Pong"}


@app.get("/api/todo")
async def get_todo():
    response = await read_all_todos()
    return response


@app.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_id(title):
    response = await read_one_todo(title)
    if response:
        return response
    else:
        raise HTTPException(404, f"There is no Todo item with this title: {title}.")


@app.post("/api/todo", response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo)
    if response:
        return response
    else:
        raise HTTPException(400, "Something went wrong")


@app.put("/api/todo/{title}", response_model=Todo)
async def put_todo(title: str, desc: str):
    response = await update_todo(title=title, description=desc)
    if response:
        return response
    else:
        raise HTTPException(500, f"There is no Todo item with this title: {title}.")


@app.delete("/api/todo/{title}")
async def delete_todo(title: str):
    clean_title = title.replace("%20", " ")
    response = await remove_todo(clean_title)
    if response:
        return "Successfully deleted todo item!"
    else:
        raise HTTPException(500, f"There is no Todo item with this title: {title}.")
