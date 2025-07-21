from fastapi import FastAPI
from app.routers import eventTeams, events, sports, teams


app = FastAPI()
app.include_router(events.router)
app.include_router(teams.router)
app.include_router(sports.router)
app.include_router(eventTeams.router)
