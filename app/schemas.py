from typing import List, Optional
from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Column
from datetime import date, datetime


class RoleCreate(BaseModel):
    name: str
    description: str
    pay: float


class RoleRead(RoleCreate):
    id: int

    class Config():
        orm_mode = True


class EventsOnSiteCreate(BaseModel):
    event_id: int
    site_id:  int


class EventsOnSiteRead(EventsOnSiteCreate):
    id: int

    class Config():
        orm_mode = True


class GroupCreate(BaseModel):
    name: str
    unit: str
    lead_one: str
    lead_two: str


class ExerciseCreate(BaseModel):
    name: str
    description: Optional[str] = None
    background_color: str
    text_color: str
    group_id: int


class ExerciseNameRead(BaseModel):
    id: int
    name: str


class ExerciseIdRead(ExerciseCreate):
    id: int


class ExerciseRead(ExerciseCreate):
    id: int
    exercise_group: Optional[GroupCreate] = None
    # exercise_user: Optional[UserCreate] = None

    class Config():
        orm_mode = True


class GroupRead(GroupCreate):
    id: int
    group_exercises: List[ExerciseIdRead] = []

    class Config():
        orm_mode = True


class EventCreate(BaseModel):
    name: str
    open_at: date
    start_at: date
    end_at: date
    infil_suspend_at: date
    exfil_suspend_at: date
    po_suspend_at: date
    final_suspend_at: date
    allow_override_dates: bool
    SubGroupId: int
    event_exercise: Optional[ExerciseCreate] = None


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


class LanguageCreate(BaseModel):
    name: str
    comment: Optional[str]


class LanguageRead(LanguageCreate):
    id: int

    class Config():
        orm_mode = True


class LanguageCategoryCreate(BaseModel):
    name: str
    description: Optional[str]

    class Config():
        orm_mode = True


class LanguageCategoryRead(LanguageCategoryCreate):
    id: int


class AttendeeCreate(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    nick_name: str
    suffix: str
    sex: str
    email: str
    street: str
    city: str
    state: str
    country_code: str
    status: str
    is_us_citizen: bool


class AttendeeRead(AttendeeCreate):
    id: int
    langs: List[LanguageCreate] = []
    lang_cats: List[LanguageCategoryCreate] = []
    attendee_roles: List[RoleCreate] = []

    # Since we use this in a query, we need ORM model on. If this was a SQLModel
    class Config():
        orm_mode = True


class PermissionTagCreate(BaseModel):
    tag: str

    class Config():
        orm_mode = True


class PermissionTagRead(PermissionTagCreate):
    id: int


class UserTagPermLinkCreate(BaseModel):
    tag: str
    access_rights: str


class UserTagPermLinkRead(UserTagPermLinkCreate):
    id: int
    hr_id: int


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
    user_access_rights: List[UserTagPermLinkRead] = []
    user_exercises: List[ExerciseNameRead] = []

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
