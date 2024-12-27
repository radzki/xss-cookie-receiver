from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL (SQLite in this case)
DATABASE_URL = "sqlite:///./payloads.db"

# SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# SessionLocal for database operations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()

# Define the PayloadModel
class PayloadModel(Base):
    __tablename__ = "payloads"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(String, index=True)

# Create all tables in the database
Base.metadata.create_all(bind=engine)
