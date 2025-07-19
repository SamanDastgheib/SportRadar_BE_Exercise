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

@router.get("/events", response_model=list[schema.Event])
def read_events(database: Session = Depends(get_db)):
    return crud.get_events(database)

@router.get("/events/{event_id}", response_model=schema.Event)
def read_event(event_id: int, database: Session = Depends(get_db)):
    return crud.get_event_by_id(database, event_id)

@router.post("/events", response_model=schema.Event)
def create_event(event: schema.EventCreate, database: Session = Depends(get_db)):
    return crud.create_event(database, event)
