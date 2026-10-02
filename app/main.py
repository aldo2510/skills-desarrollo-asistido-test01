from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API", version="1.0.0")


class Task(BaseModel):
    id: int
    title: str
    completed: bool = False


class TaskCreate(BaseModel):
    title: str


tasks: list[Task] = [
    Task(id=1, title="Learn GitHub Copilot"),
    Task(id=2, title="Create an agentic workflow"),
]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    return tasks


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(payload: TaskCreate):
    new_id = max(task.id for task in tasks) + 1
    task = Task(id=new_id, title=payload.title)
    tasks.append(task)
    return task


@app.patch("/tasks/{task_id}", response_model=Task)
def complete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            return task
    raise HTTPException(status_code=404, detail="Task not found")
