from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base

class Inventory(Base):
    __tablename__ = "inventories"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    character_id = Column(Integer, ForeignKey("characters.id"))

    quantity = Column(Integer, default=1)
