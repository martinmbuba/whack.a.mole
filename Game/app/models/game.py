from db import Base
from sqlalchemy import Column, JSON, BigInteger, DateTime, func, ForeignKey

class Game(Base):
    __tablename__ = "game"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    player_id = Column(BigInteger, ForeignKey("player.id"), nullable=False)
    board = Column(JSON, nullable=False)   
    created_at = Column(DateTime(timezone=True), server_default=func.now())
