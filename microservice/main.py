from fastapi import FastAPI
from api.counters import counters
from api.db import database


app = FastAPI()

app.include_router(counters)
