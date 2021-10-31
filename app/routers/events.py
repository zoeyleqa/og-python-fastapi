# Alternative to defining routes manually.

from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter
from app.database import get_db
from app.models import Event
from app.schemas import EventRead, EventCreate

router = CRUDRouter(
    schema=EventRead, 
    create_schema=EventCreate, 
    db=get_db, 
    db_model=Event, 
    prefix="events"
)
