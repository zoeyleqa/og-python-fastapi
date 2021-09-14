from app.models import Attendee
from app.schemas import AttendeeCreate
from sqlmodel import Session


def create(entity: AttendeeCreate, session: Session):
    session.add(entity)
    session.commit()
    session.refresh(entity)
    return entity


def show(id: int, session: Session):
    entity = session.get(Attendee, id)
    return entity
