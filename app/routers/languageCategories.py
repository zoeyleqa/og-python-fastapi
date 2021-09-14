# Alternative to defining routes manually.

from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter
from app.database import get_db
from app.models import LanguageCategory
from app.schemas import LanguageCategoryRead, LanguageCategoryCreate

router = CRUDRouter(
    schema=LanguageCategoryRead,
    create_schema=LanguageCategoryCreate,
    db=get_db,
    db_model=LanguageCategory,
    prefix="languagecategories",
)
