import motor.motor_asyncio

from model import Todo

client = motor.motor_asyncio.AsyncIOMotorClient(
    "mongodb+srv://mongoDbUser:joHgyfnZPIVSUoNe@cluster0.kgulu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
)
database = client.TodoList
collection = database.todo


async def create_todo(todo):
    result = await collection.insert_one(todo.__dict__)
    if not result:
        return None
    return todo


async def read_one_todo(title: str):
    document = await collection.find_one({"title": title})
    return document


async def read_all_todos() -> list[Todo]:
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos


async def update_todo(title: str, description: str) -> Todo:
    await collection.update_one(
        {"title": title}, {"$set": {"description": description}}
    )
    document = await collection.find_one({"title": title})
    return document


async def remove_todo(title: str) -> bool:
    await collection.delete_one({"title": title})
    return True
