from typing import List

from pydantic import parse_obj_as
from sqlalchemy import select

from database import new_session, TaskOrm
from prediction.pred import get_recommendation

from schemas import STask, STaskAdd


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
    async def find_all(cls, task_model=None) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            # task_models = result.
            # task_schemas = [STask.model_validate(task.scalar()) for task in task_models]
            model = STask.model_validate(result.scalar())
            recommendation = get_recommendation(model.__dict__)
            return [model]
