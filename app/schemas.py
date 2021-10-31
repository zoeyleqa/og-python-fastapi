from typing import List, Optional
from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Column
from datetime import datetime


class UserCreate(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
    admin: bool = Field(default=False)


class UserRead(UserCreate):
    id: int
    last_sign_in: datetime


class AttendeeCreate(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    email: str
    street: str
    city: str
    state: str
    country_code: str
    status: str
    is_us_citizen: bool


class AttendeeRead(AttendeeCreate):
    id: int

    # Since we use this in a query, we need ORM model on. If this was a SQLModel
    # class Config():
    #   orm_mode = True


class RoleCreate(BaseModel):
    name: str
    description: str
    pay: float


class RoleRead(RoleCreate):
    id: int


class EventsOnSiteCreate(BaseModel):
    event_id: int
    site_id:  int


class EventsOnSiteRead(EventsOnSiteCreate):
    id: int

    class Config():
        orm_mode = True


class EventCreate(BaseModel):
    name: str
    open_at: datetime
    start_at: datetime
    end_at: datetime
    infil_suspend_at: datetime
    exfil_suspend_at: datetime
    po_suspend_at: datetime
    final_suspend_at: datetime
    allow_override_dates: bool


class EventRead(EventCreate):
    id: int
    # sites: List[EventsOnSiteCreate]

    class Config():
        orm_mode = True


class SiteCreate(BaseModel):
    name: str
    description: str
    country: str
    city: str
    state: str
    latitude: float
    latitude_min: float
    latitude_sec: float
    longitude: float
    longitude_min: float
    longitude_sec: float


class SiteRead(SiteCreate):
    id: int
    # events: List[EventsOnSiteCreate]

    class Config():
        orm_mode = True


class ExerciseCreate(BaseModel):
    name: str
    description: str
    background_color: str
    text_color: str
    GroupId: int


class ExerciseRead(ExerciseCreate):
    id: int

    class Config():
        orm_mode = True


class GroupCreate(BaseModel):
    name: str
    unit: str
    lead_one: str
    lead_two: str


class GroupRead(GroupCreate):
    id: int
    # exercises: List[ExerciseCreate]

    class Config():
        orm_mode = True


class LanguageCreate(BaseModel):
    name: str
    comment: Optional[str]


class LanguageRead(LanguageCreate):
    id: int


class LanguageCategoryCreate(BaseModel):
    name: str
    description: Optional[str]


class LanguageCategoryRead(LanguageCategoryCreate):
    id: int


class PermissionTagCreate(BaseModel):
    name: str
    description: str


class PermissionTagRead(PermissionTagCreate):
    id: int


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
