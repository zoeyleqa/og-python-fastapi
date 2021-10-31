# Alternative to defining routes manually.

from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter
from app.database import get_db
from app.models import Site
from app.schemas import SiteRead, SiteCreate

router = CRUDRouter(
    schema=SiteRead, 
    create_schema=SiteCreate, 
    db=get_db, 
    db_model=Site, 
    prefix="sites"
)
