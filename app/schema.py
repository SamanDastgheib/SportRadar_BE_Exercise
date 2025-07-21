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

class EventResult(BaseModel):
    id : int
    day : str
    date : date
    time : time
    sport : str
    team1 : str
    team2 : str
    class Config:
        orm_mode = True
    

#---------------------------------------------

class EventTeam(BaseModel):
    event_id: int
    team_id: int

class EventTeamCreate(BaseModel):
    event_id: int
    team1_id: int
    team2_id: int
    class Config:
        orm_mode = True


#---------------------------------------------



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

#---------------------------------------------

class SportBase(BaseModel):
    name: str

class SportCreate(SportBase):
    pass

class Sport(SportBase):
    id: int
    class Config:
        orm_mode = True

class SportUpdate(SportBase):
    pass

