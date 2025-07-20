from sqlalchemy.orm import Session
from . import models, schema

def get_events(db: Session):
    return db.query(models.Event).all()

def get_event_by_id(db: Session, event_id: int):
    return db.query(models.Event).filter(models.Event.id == event_id).first()

def create_event(db: Session, event: schema.EventCreate):
    db_event = models.Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

#---------------------------------------------

def get_teams(db: Session):
    return db.query(models.Team).all()

def get_team_by_id(db: Session, team_id: int):
    team =db.query(models.Team).filter(models.Team.id == team_id)
    if team is None:
        return team 
    else:
        return team.first()
    
def create_team(db: Session, team: schema.TeamCreate):
    db_team = models.Team(**team.dict())
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

def update_team(db: Session, team_id: int, team: schema.TeamUpdate):
    db_team = get_team_by_id(db, team_id)
    if db_team: #if it is not None 
        db_team.name = team.name
        db.commit()
        db.refresh(db_team)
    return db_team

def delete_team(db: Session, team_id: int):
    db_team = get_team_by_id(db, team_id)
    if db_team:
        db.delete(db_team)
        db.commit()
    return db_team

#---------------------------------------------


def create_sport(db: Session, sport: schema.SportCreate):
    db_sport = models.Sport(**sport.dict())
    db.add(db_sport)
    db.commit()
    db.refresh(db_sport)
    return db_sport

def get_sports(db: Session):
    return db.query(models.Sport).all()

def get_sport_by_id(db: Session, sport_id: int):
    sport =db.query(models.Sport).filter(models.Sport.id == sport_id)
    if sport is None:
        return sport 
    else:
        return sport.first()
    
def update_sport(db: Session, sport_id: int, sport: schema.SportUpdate):
    db_sport = get_sport_by_id(db, sport_id)
    if db_sport: #if it is not None 
        db_sport.name = sport.name
        db.commit()
        db.refresh(db_sport)
    return db_sport

def delete_sport(db: Session, sport_id: int):
    db_sport = get_sport_by_id(db, sport_id)
    if db_sport:
        db.delete(db_sport)
        db.commit()
    return db_sport