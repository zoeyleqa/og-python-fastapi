from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, users, attendees, roles, sites, events, exercises, groups, languages, languageCategories, permissionTags

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:1337",
    "http://localhost:6006",
    "http://127.0.0.1",
    "http://127.0.0.1:1337",
    "http://127.0.0.1:6006",
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
app.include_router(sites.router)
app.include_router(events.router)
app.include_router(exercises.router)
app.include_router(groups.router)
app.include_router(languages.router)
app.include_router(languageCategories.router)
app.include_router(permissionTags.router)

@app.on_event("startup")
def on_startup():
    # create table if not already existing
    # create_db_and_tables()
    print("FastAPI Service started...")
