from fastapi import FastAPI
from app.routers import events, sports, teams

app = FastAPI()
app.include_router(events.router)
app.include_router(teams.router)
app.include_router(sports.router)
