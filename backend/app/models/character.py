from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)

    # Rarity types:
    # Common, Rare, Epic, Legendary, Celestial
    rarity = Column(String, nullable=False)

    # Celestial characters only 1 in whole database
    is_unique = Column(Boolean, default=False)
