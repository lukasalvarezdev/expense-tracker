import datetime
import json
from typing import Union
from uuid import uuid4

import aiofiles
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


def get_tasks_from_db():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except Exception:
        return []


class Task(BaseModel):
    id: str | None = None
    name: str
    description: str | None = None
    created_at: str | None = None


@app.get("/tasks")
def get_all_tasks():
    return get_tasks_from_db()


@app.get("/tasks/{task_id}")
def get_task_by_id(task_id: int, q: Union[str, None] = None):
    return {"task_id": task_id, "q": q}


@app.post("/tasks")
async def create_task(task: Task):
    tasks = get_tasks_from_db()

    new_task = Task(
        id=str(uuid4()),  # Generate a new unique ID
        name=task.name,
        description=task.description,
        created_at=str(datetime.datetime.now()),
    )

    tasks.append(new_task.model_dump())

    await save_tasks_to_file(tasks)

    return new_task


@app.delete(
    "/tasks/{task_id}",
)
async def delete_task(
    task_id: str,
):
    tasks = get_tasks_from_db()

    task_exists = any(task["id"] == task_id for task in tasks)

    if not task_exists:
        raise HTTPException(status_code=404, detail="Task not found")

    filtered_tasks = list(filter(lambda task: task["id"] != task_id, tasks))

    await save_tasks_to_file(filtered_tasks)

    return filtered_tasks


@app.patch(
    "/tasks/{task_id}",
)
async def update_task(task_id: str, updated_task: Task):
    tasks = get_tasks_from_db()

    task_exists = any(task["id"] == task_id for task in tasks)

    if not task_exists:
        raise HTTPException(status_code=404, detail="Task not found")

    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks[i] = updated_task.model_copy(
                update={"id": task_id, "created_at": task["created_at"]}
            ).model_dump()

            await save_tasks_to_file(tasks)
            return tasks[i]


async def save_tasks_to_file(new_tasks):
    async with aiofiles.open("tasks.json", "w") as file:
        await file.write(json.dumps(new_tasks, indent=4))
