from typing import List

from pydantic import parse_obj_as
from sqlalchemy import select

from database import new_session, TaskOrm
from prediction.pred import get_recommendation

from schemas import STask, STaskAdd, STaskId


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            # await session.flush()  # отправит изменения в базу
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls, task_model=None) -> list[STaskId]:
        async with new_session() as session:
            tasks = (await session.scalars(select(TaskOrm))).all()
            # task_models = result.
            # task_schemas = [STask.model_validate(task.scalar()) for task in task_models]
            result = []
            for task in tasks:
                recommendation = get_recommendation(task)
                result.append(STaskId(id=task.id, advice=recommendation))
            return result
