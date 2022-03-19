from fastapi import FastAPI
from api.counters import counters
from api.db import database

# metadata.create_all(engine)

app = FastAPI()

# @app.on_event("startup")
# async def startup():
#     await database

# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


app.include_router(counters)
