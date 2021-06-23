from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from .. import schemas, database, oauth2
from ..repository import user

get_db = database.get_db

router = APIRouter(
    tags=['Users'],
    prefix="/api/v1/users"
)

@router.post('', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get("/me", status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_my_profile(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.show(current_user, db)