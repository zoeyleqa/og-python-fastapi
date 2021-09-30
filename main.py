from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, users, attendees, roles, languages, languageCategories

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:1337",
    "http://cop.oakgrovetech.com/",
    "https://cop.oakgrovetech.com/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(attendees.router)
app.include_router(roles.router)
app.include_router(languages.router)
app.include_router(languageCategories.router)


@app.on_event("startup")
def on_startup():
    # create table if not already existing
    # create_db_and_tables()
    print("FastAPI Service started...")
