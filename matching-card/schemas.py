from typing import Optional
from pydantic import BaseModel, validator
        
class Login(BaseModel):
    username: str
    password:str
    
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
    
class User(BaseModel):
    name:str
    email:str
    password:str
    
class ShowUser(BaseModel):
    name:str
    email:str
    
    class Config():
        orm_mode = True
        
class Game(BaseModel):
    id:int
    player_name:str
    clicks:int
    
    class Config():
        orm_mode = True
    
class CardSelect(BaseModel):
    game_id: int
    selecting_card: int
    
class ShowCardSelect(BaseModel):
    game_id: int
    position: int
    shown: bool
    value: int
    
class ShowGameHighScore(BaseModel):
    clicks:int
    
    class Config():
        orm_mode = True