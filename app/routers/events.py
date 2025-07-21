from datetime import datetime
from app import validationUtils
from fastapi import HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schema, db
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

router = APIRouter()

def get_db():
    database = db.SessionLocal()
    try:
        yield database
    finally:
        database.close()

@router.get("/eventResults/{event_id}", response_model=schema.EventResult)
def read_formated_events_by_id(event_id: int, database: Session = Depends(get_db)):
    events = crud.get_eventResutlsWithId(database, event_id)
    logger.info(f"Events found: {events}")
    result = validationUtils.merge_eventResults(events)
    if len(result) != 1 :
        raise HTTPException(status_code=404, detail="Event not found")

    return result[0]

@router.get("/eventResults", response_model=list[schema.EventResult])
def read_formated_events(database: Session = Depends(get_db)):
    events = crud.get_eventResutls(database)
    
    return validationUtils.merge_eventResults(events)

@router.get("/events", response_model=list[schema.Event])
def read_events(database: Session = Depends(get_db)):
    return crud.get_events(database)

@router.get("/events/{event_id}", response_model=schema.Event)
def read_event(event_id: int, database: Session = Depends(get_db)):
    return crud.get_event_by_id(database, event_id)

@router.post("/events", response_model=schema.Event)
def create_event(event: schema.EventCreate, database: Session = Depends(get_db)):
    event = crud.create_event(database, event)
    if event is None:
        raise HTTPException(status_code=404, detail="Sport not found")
    return event





