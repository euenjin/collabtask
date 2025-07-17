from fastapi import FastAPI
from database import engine
from models import ScheduleItem   
from models import Base

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, CollabTask!"}

@app.post("/schedule")
async def create_schedule_item(item: ScheduleItem):        #returns a created schedule item
    return { "recieved schedule": item}

Base.metadata.create_all(bind=engine)  # Ensure the database tables are created

