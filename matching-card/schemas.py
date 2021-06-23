from typing import Optional
from pydantic import BaseModel, validator
        
class Login(BaseModel):
    username: str
    password:str
    
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    
class User(BaseModel):
    username:str
    email:str
    password:str
    
class ShowUser(BaseModel):
    username:str
    email:str
    
    class Config():
        orm_mode = True
        
class Game(BaseModel):
    id:int
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