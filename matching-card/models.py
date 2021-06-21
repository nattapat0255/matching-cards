from sqlalchemy import ForeignKey, Column, Boolean, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class Game(Base):
    __tablename__ = "games"
    
    id = Column(Integer, primary_key=True, index=True)
    player_name = Column(String)
    clicks = Column(Integer, index=True, default=0)
    active = Column(Boolean, default=True)
    solved = Column(Boolean, default=False)
    
    cards = relationship("Card")
    
class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    position = Column(Integer, index=True)
    value = Column(Integer, index=True)
    shown = Column(Boolean, default=False)
    correct = Column(Boolean, default=False)
    
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)