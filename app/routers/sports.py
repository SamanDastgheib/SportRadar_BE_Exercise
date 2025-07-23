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

@router.post("/sport" , tags=["sport"])
async def create_sport(sport: schema.SportCreate, db: Session = Depends(get_db)):
    if validationUtils.is_valid_name(sport.name) is False:
        raise HTTPException(status_code=400, detail="Sport name is required")
    sport = crud.create_sport(db, sport)
    if sport is None:
        raise HTTPException(status_code=404, detail="Sport not found")
    return sport

@router.get("/sports", tags=["sport"])
async def read_sports(db: Session = Depends(get_db)):
    sports = crud.get_sports(db)
    return sports

@router.get("/sport/{sport_id}", tags=["sport"])
async def read_sport(sport_id: int, db: Session = Depends(get_db)):
    sport = crud.get_sport(db, sport_id)
    if sport is None:
        raise HTTPException(status_code=404, detail="Sport not found")
    return sport        

@router.patch("/sport/{sport_id}", tags=["sport"])
async def update_sport(sport_id: int, sport: schema.SportUpdate, db: Session = Depends(get_db)):
    if validationUtils.is_valid_name(sport.name) is False:
        raise HTTPException(status_code=400, detail="Sport name is required")
    sport = crud.update_sport(db, sport_id, sport)
    if sport is None:
        raise HTTPException(status_code=404, detail="Sport not found")
    return sport

@router.delete("/sport/{sport_id}", tags=["sport"])
async def delete_sport(sport_id: int, db: Session = Depends(get_db)):
    sport = crud.delete_sport(db, sport_id)
    if sport is None:
        raise HTTPException(status_code=404, detail="Sport not found")
    return sport