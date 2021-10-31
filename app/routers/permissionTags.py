# Alternative to defining routes manually.

from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter
from app.database import get_db
from app.models import PermissionTag
from app.schemas import PermissionTagRead, PermissionTagCreate

router = CRUDRouter(
    schema=PermissionTagRead, 
    create_schema=PermissionTagCreate, 
    db=get_db, 
    db_model=PermissionTag, 
    prefix="permissiontags"
)
