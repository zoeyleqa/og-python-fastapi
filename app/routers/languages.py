# Alternative to defining routes manually.

from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter
from app.database import get_db
from app.models import Language
from app.schemas import LanguageRead, LanguageCreate

router = CRUDRouter(
  schema=LanguageRead,
  create_schema=LanguageCreate,
  db=get_db,
  db_model=Language,
  prefix="Languages"
)