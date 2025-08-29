from db import Base
from sqlalchemy import Column, String, BigInteger, DateTime, func

class Player(Base):
    __tablename__ = "player"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
