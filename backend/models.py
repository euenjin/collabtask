from enum import Enum        # To define enumerations 
from datetime import datetime    #To handle date and time
from pydantic import BaseModel    # To create data models
from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.sql.sqltypes import Integer  # To define database columns
from database import Base  # To use the base class for SQLAlchemy models

class ScheduleType(str, Enum):   #To define types of schedules
    OneTime = "one_time"  
    FIXED = "fixed"              
    FLEXIBLE = "flexible"

class PriorityLevel(str, Enum):    #To define priority levels
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
 
class ScheduleItem(BaseModel):      #To define a schedule item model
    title: str
    start_time: datetime
    end_time: datetime
    schedule_type: ScheduleType
    priority: PriorityLevel
    recurring: bool = False

class Schedule(Base):              #To define a database model for schedules
    __tablename__ = "schedules"  
    id = Column(Integer,primary_key=True, index=True)  
    title = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    event_type = Column(String, nullable=False)  # fixed, flexible, and one_time
    priority = Column(String, nullable=False)    # low, medium, high
    repeat = Column(Boolean, default=False)
