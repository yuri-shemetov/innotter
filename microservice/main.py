from fastapi import FastAPI
from api.counters import counters


app = FastAPI()

app.include_router(counters)
