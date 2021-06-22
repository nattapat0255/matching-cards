from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas
from ..hashing import Hash
import random

DECK_LIST = [1,1,2,2,3,3,4,4,5,5,6,6]
  
def create(current_user: schemas.User, db: Session):
    game_room = db.query(models.Game).filter_by(player_name = current_user.username, active = True).first()
    if game_room:
        game_room.active = False
        db.commit()
    db_game = models.Game(player_name=current_user.username)
    db.add(db_game)
    db.commit()
    cards = DECK_LIST
    random.shuffle(cards)
    for index, value in enumerate(cards):
        db_card = models.Card(value=value, game_id=db_game.id)
        db.add(db_card)
        db.commit()
    db.refresh(db_game)
    return db_game

def choose(request: schemas.CardSelect, db: Session):
    game_room = db.query(models.Game).filter_by(id = request.game_id, active = True).first()
    if not game_room:
        raise HTTPException(status_code=404, detail="Not Found Game Room")
    
    # Check card input
    position = request.selecting_card
    if position < 1 or position > 12:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Please select position between 1 to 12")
    
    # Get all cards
    cards = db.query(models.Card).filter_by(game_id = request.game_id).order_by(models.Card.id)
    selected_card = cards[position-1]
    value = selected_card.value
    
    if selected_card.shown and selected_card.correct:
        return game_is_continue(value, "This card is already matched", game_room)
        
    if selected_card.shown and not selected_card.correct:
        return game_is_continue(value, "You are selecting this card", game_room)
    
    game_room.clicks +=1
    shown_cards = list(filter(lambda card: card.shown and not card.correct, game_room.cards))
    if len(shown_cards) == 0:
        selected_card.shown = True
        db.commit()
        return game_is_continue(value, f"You got a card number {value}", game_room)
    else:
        shown_card = shown_cards[0]
        if shown_card.value == value:
            shown_card.correct = True
            selected_card.correct = True
            selected_card.shown = True
            db.commit()
            if len(list(filter(lambda card: card.correct, game_room.cards))) == 12:
                return game_over(db, game_room)
            return game_is_continue(value, "These cards are matching", game_room)
        else:
            shown_card.shown = False
            db.commit()
            return game_is_continue(value, "These cards doesn't match", game_room)
        
def game_is_continue(value, message, game_room):
    return {
        "card_number": value,
        "message": message,
        "clicks": game_room.clicks,
        "game_over": False
    }

def game_over(db, game_room):
    game_room.solved = True
    game_room.active = False
    db.commit()
    return {
        "message": "Game clear!",
        "clicks": game_room.clicks,
        "game_over": True
    }

def get_highscore(current_user: schemas.User, db: Session):
    game_room = db.query(models.Game).filter_by(player_name = current_user.username, solved= True).order_by(models.Game.clicks).first()
    return game_room

def get_worldrecord(db: Session):
    game_room = db.query(models.Game).filter_by(solved= True).order_by(models.Game.clicks).first()
    return game_room