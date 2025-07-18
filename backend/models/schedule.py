from sqlalchemy import Column, String, DateTime, Boolean, Integer
from database import Base

class Schedule(Base):
    __tablename__ = "schedules"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    schedule_type = Column(String, nullable=False)  # "one_time", "fixed", "flexible"
    priority = Column(String, nullable=False)       # "low", "medium", "high"
    repeat = Column(Boolean, default=False)