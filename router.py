from typing import Annotated

from fastapi import APIRouter, Depends

from prediction.pred import get_recommendation
from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
) -> STask:
    task_id = await TaskRepository.add_one(task)
    return STask(id=task_id, time=task.time, emotion=task.emotion)


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks
