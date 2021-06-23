from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from .. import schemas, database, oauth2
from ..repository import game

get_db = database.get_db

router = APIRouter(
    tags=['Matching Card Game'],
    prefix="/api/v1/game")

@router.get('', status_code=status.HTTP_201_CREATED, response_model=schemas.Game)
def new_game(db: Session = Depends(get_db), 
             current_user: schemas.User = Depends(oauth2.get_current_user)):
    return game.create(current_user, db)

@router.post('/choose', status_code=status.HTTP_202_ACCEPTED)
def select_card(request: schemas.CardSelect, 
                db: Session = Depends(get_db), 
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    return game.choose(current_user, request, db)

@router.get('/highscore', status_code=status.HTTP_200_OK, response_model=schemas.ShowGameHighScore)
def get_word_record(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return game.get_worldrecord(db)

@router.get('/highscore/me', status_code=status.HTTP_200_OK, response_model=schemas.ShowGameHighScore)
def get_my_highscore(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return game.get_highscore(current_user, db)