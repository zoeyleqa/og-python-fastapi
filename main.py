from fastapi import FastAPI
from app.routers import auth, users, attendees, roles, languages, languageCategories

app = FastAPI()

@app.on_event("startup")
def on_startup():
  # create table if not already existing
  # create_db_and_tables()
  print("FastAPI Service started...")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(attendees.router)
app.include_router(roles.router)
app.include_router(languages.router)
app.include_router(languageCategories.router)
