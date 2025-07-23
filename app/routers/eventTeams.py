from fastapi import HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schema, db

router = APIRouter()

def get_db():
    database = db.SessionLocal()
    try:
        yield database
    finally:
        database.close()


@router.get("/eventTeam/{event_id}", response_model=schema.EventTeam , tags=["EventTeam"])
def get_teamEvent_by_event_id(event_id: int, db: Session = Depends(get_db)):
    event_teams = crud.get_eventTeam_by_event_id(db, event_id)
    if not event_teams:
        raise HTTPException(status_code=404, detail="Event team not found")
    else:
        event_team_record = schema.EventTeam(
        event_id=event_teams[0].event_id,
        team1_id=event_teams[0].team_id,
        team2_id=event_teams[1].team_id
        )
            
    return event_team_record

@router.post("/eventTeam", response_model= list[schema.EventTeam], tags=["EventTeam"])
def create_event_teams(event_team: schema.EventTeamCreate, db: Session = Depends(get_db)):
    event_teams = crud.get_eventTeam_by_event_id(db, event_team.event_id)
    if event_teams:
        raise HTTPException(status_code=400, detail="Event has been saved before")
    event_team = crud.create_eventTeam(db, event_team)
    if event_team is None:
        raise HTTPException(status_code=404, detail="Event or team not found")
    return event_team