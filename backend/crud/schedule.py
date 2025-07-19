from sqlalchemy.orm import Session
from backend.models.schedule import Schedule
from backend.schemas.schedule import ScheduleCreate

def create_schedule(db:Session, schedule :ScheduleCreate):
    db_schedule= Schedule(
        title=schedule.title,
        start_time=schedule.start_time,
        end_time=schedule.end_time,
        schedule_type=schedule.schedule_type,
        priority=schedule.priority,
        repeat=schedule.repeat
    )
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule
