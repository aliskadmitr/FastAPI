import uvicorn
from fastapi import FastAPI


from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router


# context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")


if __name__ == "__main__":
    app = FastAPI(lifespan=lifespan)
    app.include_router(tasks_router)
    uvicorn.run(app, host="0.0.0.0", port=8000)
