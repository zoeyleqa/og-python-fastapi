# Alternative to defining routes manually.

from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter
from app.database import get_db
from app.models import Role
from app.schemas import RoleRead, RoleCreate

router = CRUDRouter(
    schema=RoleRead, create_schema=RoleCreate, db=get_db, db_model=Role, prefix="roles"
)
