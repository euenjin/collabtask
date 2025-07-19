from fastapi import FastAPI
from backend.database import engine
from backend.schemas.schedule import ScheduleItem   
from backend.models.schedule import Schedule, Base
from backend.routers import user  # import user router

app = FastAPI()
app.include_router(user.router, prefix="/users", tags=["users"])


@app.get("/")
async def root():
    return {"message": "Hello, CollabTask!"}

@app.post("/schedule")
async def create_schedule_item(item: ScheduleItem):        #returns a created schedule item
    return { "recieved schedule": item}

Base.metadata.create_all(bind=engine)  # Ensure the database tables are created

