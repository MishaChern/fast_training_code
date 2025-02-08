from typing import Annotated
from fastapi import APIRouter
from fastapi.params import Depends
from tornado.process import task_id

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/task",
    tags=["Таски"],
)

@router.post("")
async def add_task(
        task: Annotated[STaskAdd,Depends()],
)-> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.get_all()
    return tasks