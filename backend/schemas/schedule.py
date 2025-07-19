from pydantic import BaseModel

class ScheduleItemCreate(BaseModel):
    title: str
    description: str

class ScheduleItemResponse(ScheduleItemCreate):
    id: int

    class Config:
        orm_mode = True
