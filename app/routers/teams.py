from fastapi import HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schema, db , validationUtils


router = APIRouter()

def get_db():
    database = db.SessionLocal()
    try:
        yield database
    finally:
        database.close()

@router.get("/teams",response_model=list[schema.Team])
def read_teams(database: Session = Depends(get_db)):
    return crud.get_teams(database)

@router.get("/teams/{team_id}",response_model=schema.Team)
def find_team_by_id(team_id: int, database: Session = Depends(get_db)):
    team = crud.get_team_by_id(database, team_id)
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

@router.post("/teams",response_model=schema.Team)
def create_team(team: schema.TeamCreate, database: Session = Depends(get_db)):
    if validationUtils.is_valid_name(team.name) is False:
        raise HTTPException(status_code=400, detail="Team name is required")
    return crud.create_team(database, team)

@router.patch("/teams/{team_id}",response_model=schema.Team)
def update_team(team_id: int, team: schema.TeamUpdate, database: Session = Depends(get_db)):
    if validationUtils.is_valid_name(team.name) is False:
        raise HTTPException(status_code=400, detail="Team name is required")
    updated_team = crud.update_team(database, team_id, team)
    if updated_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return updated_team

@router.delete("/teams/{team_id}",response_model=schema.Team)
def delete_team(team_id: int, database: Session = Depends(get_db)):
    delete_team = crud.delete_team(database, team_id)
    if delete_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return delete_team
