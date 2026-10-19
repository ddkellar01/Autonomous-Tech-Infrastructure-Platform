from sqlalchemy import Column, Integer, String, DateTime, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class ScoutLog(Base):
    __tablename__ = "scout_logs"

    id = Column(Integer, primary_key=True, index=True)
    org_name = Column(String, index=True)
    repo_count = Column(Integer)
    report_data = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

engine = create_engine("sqlite:///./autonomous_engine.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
