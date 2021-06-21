from typing import Optional
from pydantic import BaseModel, validator

class Game(BaseModel):
    player_name: str
        
class CardSelect(BaseModel):
    game_id: int
    selecting_card: int
    
class User(BaseModel):
    name:str
    email:str
    password:str
    
class ShowUser(BaseModel):
    name:str
    email:str
    
    class Config():
        orm_mode = True
        
class Login(BaseModel):
    username: str
    password:str
    
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None