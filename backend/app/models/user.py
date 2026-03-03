from sqlalchemy import Column, BigInteger, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(BigInteger, unique=True, index=True)
    username = Column(String)
    coins = Column(Integer, default=500)
    arena_rank = Column(String, default="Bronze")
    created_at = Column(DateTime, default=datetime.utcnow)
