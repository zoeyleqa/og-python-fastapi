from app.models import Role
from app.schemas import RoleCreate
from sqlmodel import Session


def create(entity: RoleCreate, session: Session):
    session.add(entity)
    session.commit()
    session.refresh(entity)
    return entity


def show(id: int, session: Session):
    entity = session.get(Role, id)
    return entity
