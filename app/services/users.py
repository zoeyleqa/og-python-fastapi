from app.models import User
from app.schemas import UserCreate
from app.hashing import Hash
from sqlmodel import Session


def create(entity: UserCreate, session: Session):
    entity.password = Hash.encrypt(entity.password)
    session.add(entity)
    session.commit()
    session.refresh(entity)
    return entity


def show(id: int, session: Session):
    entity = session.get(User, id)
    return entity
