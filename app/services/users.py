from app.models import User
from app.schemas import UserCreate
from app.hashing import Hash
from sqlmodel import Session, select


def create(entity: UserCreate, session: Session):
    entity.password = Hash.encrypt(entity.password)
    session.add(entity)
    session.commit()
    session.refresh(entity)
    return entity


def show_all(session: Session):
    entities = session.exec(select(User)).all()
    return entities


def show(id: int, session: Session):
    entity = session.get(User, id)
    return entity
