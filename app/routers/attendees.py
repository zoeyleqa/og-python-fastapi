# Alternative to defining routes manually.

from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter
from app.database import get_db
from app.models import Attendee
from app.schemas import AttendeeRead, AttendeeCreate

router = CRUDRouter(
    schema=AttendeeRead, create_schema=AttendeeCreate, db=get_db, db_model=Attendee, prefix="attendees", paginate=250
)
