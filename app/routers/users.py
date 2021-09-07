from app.database import get_session
from app.models import User
from fastapi import APIRouter, Depends, status, HTTPException
from app import schemas, oauth2
from app.services import users
from sqlmodel import Session
from app.hashing import Hash

router = APIRouter(
  prefix="/users",
  tags=["Users"],
  # lock it down!
  # dependencies=[Depends(oauth2.get_current_user)],
  responses={}
)

@router.post('', response_model=schemas.UserRead, status_code=status.HTTP_201_CREATED)
def create(
  *, 
  session: Session = Depends(get_session), 
  # current_user: User = Depends(oauth2.get_current_user),
  args: schemas.UserCreate
):
  return users.create(args, session)

@router.get('/{id}', response_model=schemas.UserRead, status_code=status.HTTP_200_OK)
def show(*, session: Session = Depends(get_session), id: int):
  user = users.show(id, session)

  if not user:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, 
      detail=f"User with the id {id} is not available."
    )

  return user
