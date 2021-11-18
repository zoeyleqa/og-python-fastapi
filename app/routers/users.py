from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter
from fastapi import APIRouter, Depends, status, HTTPException
from app.database import get_session, get_db
from app.models import User
from app.schemas import UserRead, UserCreate
from app import oauth2
from app.services import users
from sqlmodel import Session
from app.hashing import Hash
from typing import List

# router = APIRouter(
#     prefix="/users",
#     tags=["Users"],
#     # lock it down!
#     # dependencies=[Depends(oauth2.get_current_user)],
#     responses={},
# )

router = CRUDRouter(
    schema=UserRead,
    create_schema=UserCreate,
    db=get_db,
    db_model=User,
    prefix="users"
)


@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create(
    *,
    session: Session = Depends(get_session),
    # current_user: User = Depends(oauth2.get_current_user),
    args: UserCreate,
):
    return users.create(args, session)


@router.get("", response_model=List[UserRead], status_code=status.HTTP_200_OK)
def get_all(*, session: Session = Depends(get_session)):
    all_users = users.show_all(session)

    if not all_users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No user is found",
        )

    return all_users


