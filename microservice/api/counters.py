from fastapi import APIRouter, HTTPException, Path
from .models import CounterIn, CounterUpdate
from api import db_manager


counters = APIRouter()

@counters.get('/api/pages/')
async def read_everything_counter():
    return db_manager.get_everything_counter()

@counters.get('/api/pages/{id}')
async def read_counter(id: str = Path(..., description='Search the page')):
    return db_manager.get_counter(page=id)

@counters.post('/api/pages/', status_code=201)
async def add_counter(payload: CounterIn):
    counter_id = db_manager.add_counter(
        payload.page, 
        payload.count_follow_requests, 
        payload.count_follower, 
    )
    response = {
        'id': counter_id,
        'page': payload.page,
        'counters': {
            'count_follower': payload.count_follower,
            'count_follow_requests': payload.count_follow_requests
        }
    }
    return response

@counters.put('/api/pages/{id}', status_code=201)
async def update_counter(id: str, payload: CounterUpdate):
    counter_id = db_manager.update_counter(
        id, 
        payload.count_follow_requests,
        payload.count_follower
    )
    response = {
        'id': counter_id,
        'counters': {
            'count_follower': payload.count_follower,
            'count_follow_requests': payload.count_follow_requests
        }
    }
    return response

@counters.delete('/api/pages/{id}')
async def delete_counter(id: str):
    movie = db_manager.delete_counter(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_manager.delete_counter(id)
