from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas
from ..hashing import Hash
  
def create(request: schemas.User, db: Session):
    user =  db.query(models.User).filter_by(username=request.username, email=request.email).first()
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
            detail=f"username or email is already used")
    new_user = models.User(username=request.username, email=request.email, password= Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(request: schemas.User, db: Session):
    user = db.query(models.User).filter_by(username = request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"This user is not available")
    return user