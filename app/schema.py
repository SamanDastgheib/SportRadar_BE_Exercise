from pydantic import BaseModel
from datetime import date, time

class EventBase(BaseModel):
    event_date: date
    event_time: time
    sport_id: int

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int

    class Config:
        orm_mode = True

class TeamBase(BaseModel):
    name: str

class TeamCreate(TeamBase):
    pass

class Team(TeamBase):
    id: int
    class Config:
        orm_mode = True


class TeamUpdate(TeamBase):
    pass


