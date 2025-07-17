from sqlalchemy import create_engine               # Connect engine to the database
from sqlalchemy.ext.declarative import declarative_base  # base class factory for ORM models
from sqlalchemy.orm import sessionmaker             # Connect ORM models to the database
from dotenv import load_dotenv                       # Load settings from .env file
import os                                            # Import OS module to access environment variables

load_dotenv()                                        # Load variables from .env file into environment

DATABASE_URL = os.getenv("DATABASE_URL")             # Get DB connection string from environment variable

engine = create_engine(DATABASE_URL)                 # Create a DB engine instance for managing connections

SessionLocal = sessionmaker(                         # Create a configured "Session" class
    autocommit=False,                                # Disable autocommit (manual commit control)
    autoflush=False,                                 # Disable autoflush (manual flush control)
    bind=engine                                     # Bind sessions to the engine (DB connection)
)

Base = declarative_base()                            # Create a base class for all ORM models to inherit from
