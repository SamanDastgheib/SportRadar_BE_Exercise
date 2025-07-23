from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import eventTeams, events, sports, teams


app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(events.router)
app.include_router(teams.router)
app.include_router(sports.router)
app.include_router(eventTeams.router)
