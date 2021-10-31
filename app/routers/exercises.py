# Alternative to defining routes manually.

from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter
from app.database import get_db
from app.models import Exercise
from app.schemas import ExerciseRead, ExerciseCreate

router = CRUDRouter(
    schema=ExerciseRead, 
    create_schema=ExerciseCreate, 
    db=get_db, 
    db_model=Exercise, 
    prefix="exercises"
)
