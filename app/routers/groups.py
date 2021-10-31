# Alternative to defining routes manually.

from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter
from app.database import get_db
from app.models import Group
from app.schemas import GroupRead, GroupCreate

router = CRUDRouter(
    schema=GroupRead, 
    create_schema=GroupCreate, 
    db=get_db, 
    db_model=Group, 
    prefix="groups"
)
