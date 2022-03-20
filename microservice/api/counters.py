from fastapi import Header, APIRouter, HTTPException, Path
from .models import CounterIn, CounterOut, CounterUpdate
from api import db_manager


counters = APIRouter()

@counters.get('/{page}')
async def read_counter(page: str = Path(..., description='Search the page')):
    return db_manager.get_counter(page=page)

@counters.post('/', status_code=201)
async def add_counter(payload: CounterIn):
    counter_id = db_manager.add_counter(
        payload.page, payload.count_follow_requests, payload.count_follower)
    response = {
        'id': counter_id,
        'page': payload.page,
        'counters': {
            'count_follower': payload.count_follower,
            'count_follow_requests': payload.count_follow_requests
        }
    }
    return response

@counters.put('/counters/{id}', status_code=201)
async def update_counter(id: str, payload: CounterUpdate):
    counter_id = db_manager.update_counter(
        id, payload.count_follow_requests, payload.count_follower)
    response = {
        'id': counter_id,
        'counters': {
            'count_follower': payload.count_follower,
            'count_follow_requests': payload.count_follow_requests
        }
    }
    return response

@counters.delete('/{id}')
async def delete_counter(id: str):
    movie = db_manager.delete_counter(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_manager.delete_counter(id)
