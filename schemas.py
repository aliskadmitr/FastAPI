from typing import Optional

from pydantic import BaseModel, ConfigDict


class STaskAdd(BaseModel):
    time: int
    emotion: Optional[str] = None


class STask(STaskAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class STaskId(BaseModel):
    id: int
    advice: str
