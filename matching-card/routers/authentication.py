from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from .. import schemas, database, models, token
from ..hashing import Hash
get_db = database.get_db

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")
    
    access_token = token.create_access_token(data={"sub": user.name})
    return {"access_token": access_token, "token_type": "bearer"}