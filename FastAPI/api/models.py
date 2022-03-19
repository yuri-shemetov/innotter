from pydantic import BaseModel
from typing import Optional


class CounterIn(BaseModel):
    page: str
    count_follower: int
    count_follow_requests: int


class CounterOut(CounterIn):
    id: int


class CounterUpdate(CounterIn):
    page: Optional[str] = None
    count_follower: Optional[int] = None
    count_follow_requests: Optional[int] = None