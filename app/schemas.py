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
class RoleCreate(BaseModel):
  name: str
  description: str
  pay: float
class RoleRead(RoleCreate):
  id: int
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

class Login(BaseModel):
  username: str
  password: str
class Token(BaseModel):
  access_token: str
  token_type: str
class TokenData(BaseModel):
  username: Optional[str] = None