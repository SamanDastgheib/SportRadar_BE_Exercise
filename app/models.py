from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey, Table
from sqlalchemy.orm import relationship
from .db import Base

class Sport(Base):
    __tablename__ = "sport"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)

class Team(Base):
    __tablename__ = "team"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)

class Event(Base):
    __tablename__ = "event"
    id = Column(Integer, primary_key=True, index=True)
    event_date = Column(Date, nullable=False)
    event_time = Column(Time, nullable=False)
    sport_id = Column(Integer, ForeignKey("sport.id"))

class EventTeam(Base):
    __tablename__ = "event_team"
    event_id = Column(Integer, ForeignKey("event.id"), primary_key=True)
    team_id = Column(Integer, ForeignKey("team.id"), primary_key=True)
