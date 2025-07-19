from fastapi import FastAPI
from app.routers import events

app = FastAPI()
app.include_router(events.router)
