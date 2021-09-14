from typing import Optional, List
from sqlmodel import SQLModel, Field, Column, Relationship
from datetime import date

# TODO Relationship definitions

# Linker tables toward top, since they need to be defined first in order for base
# models to use them.
# class AttendeeRoleLink(SQLModel, table=True):
#   __tablename__ = "RS_People_Roles_Assiged"

#   id: Optional[int] = Field(primary_key=True, default=None)
#   role_id: Optional[int] = Field(
#     sa_column=Column("RoleId"), default=None, foreign_key="Roles.Id", primary_key=True,
#   )
#   attendee_id: Optional[int] = Field(
#     sa_column=Column("HumanResourceId"), default=None, foreign_key="RS_People.Id", primary_key=True
#   )
#   pay: float


# Base models below
class User(SQLModel, table=True):
    __tablename__ = "Users"

    id: Optional[int] = Field(sa_column=Column("User_ID", primary_key=True), default=None)
    username: str
    first_name: str = Field(sa_column=Column("FirstName"))
    last_name: str = Field(sa_column=Column("LastName"))
    email: str
    password: str
    admin: str
    activation_token: str = Field(sa_column=Column("ActivationToken"))
    last_activation_request: int = Field(sa_column=Column("LastActivationRequest"))
    lost_password_request: int = Field(sa_column=Column("LostPasswordRequest"), default=0)
    active: int
    group_id: int = Field(sa_column=Column("Group_ID"))
    sign_up_date: int = Field(sa_column=Column("SignUpDate"))
    last_sign_in: int = Field(sa_column=Column("LastSignIn"))
    last_selected_event: int = Field(sa_column=Column("LastSelectedEvent"), default=0)
    password_request: Optional[str] = Field(sa_column=Column("PasswordRequest"))


class Attendee(SQLModel, table=True):
    __tablename__ = "RS_People"

    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(sa_column=Column("FirstName"))
    last_name: str = Field(sa_column=Column("LastName"))
    middle_name: Optional[str] = Field(sa_column=Column("MiddleName"))
    nick_name: Optional[str] = Field(sa_column=Column("NickName"))
    suffix: Optional[str]
    sex: Optional[str]
    date_of_birth: Optional[date] = Field(sa_column=Column("DOB"))
    company: Optional[str]
    employee_id_number: Optional[str] = Field(sa_column=Column("EIN"))
    social_security_number: Optional[str] = Field(sa_column=Column("SocialSecID"))
    email: Optional[str]
    street: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country_code: Optional[str] = Field(sa_column=Column("CountryCode"))
    zip: Optional[str]
    phone_home: Optional[str] = Field(sa_column=Column("PhoneHome"))
    phone_cell: Optional[str] = Field(sa_column=Column("PhoneCell"))
    bkg_check_at: Optional[date] = Field(sa_column=Column("BkgCheckDate"))
    bkg_check: Optional[int] = Field(sa_column=Column("BkgCheck"))
    force_protection_date: Optional[date] = Field(sa_column=Column("ForceProtectionDate"))
    clear_type: Optional[str] = Field(sa_column=Column("ClearType"))
    clear_expire_at: Optional[date] = Field(sa_column=Column("ClearExp"))
    medical_expire_at: Optional[date] = Field(sa_column=Column("MedicalExp"))
    liability_expire_at: Optional[date] = Field(sa_column=Column("LiabExp"))
    physical_date: Optional[date] = Field(sa_column=Column("PhysicalDate"))
    status: Optional[str]

    emergency_one_first_name: Optional[str] = Field(sa_column=Column("EFirstNameA"))
    emergency_one_last_name: Optional[str] = Field(sa_column=Column("ELastNameA"))
    emergency_one_phone_home: Optional[str] = Field(sa_column=Column("EPhoneHomeA"))
    emergency_one_phone_cell: Optional[str] = Field(sa_column=Column("EphoneCellA"))
    emergency_one_street: Optional[str] = Field(sa_column=Column("EStreetA"))
    emergency_one_city: Optional[str] = Field(sa_column=Column("ECityA"))
    emergency_one_state: Optional[str] = Field(sa_column=Column("EStateA"))
    emergency_one_zip: Optional[str] = Field(sa_column=Column("EZipA"))

    emergency_two_first_name: Optional[str] = Field(sa_column=Column("EFirstNameB"))
    emergency_two_last_name: Optional[str] = Field(sa_column=Column("ELastNameB"))
    emergency_two_phone_home: Optional[str] = Field(sa_column=Column("EPhoneHomeB"))
    emergency_two_phone_cell: Optional[str] = Field(sa_column=Column("EphoneCellB"))
    emergency_two_street: Optional[str] = Field(sa_column=Column("EStreetB"))
    emergency_two_city: Optional[str] = Field(sa_column=Column("ECityB"))
    emergency_two_state: Optional[str] = Field(sa_column=Column("EStateB"))
    emergency_two_zip: Optional[str] = Field(sa_column=Column("EZipB"))

    allergies_one: Optional[str] = Field(sa_column=Column("AllergiesA"))
    allergies_two: Optional[str] = Field(sa_column=Column("AllergiesB"))
    allergies_three: Optional[str] = Field(sa_column=Column("AllergiesC"))

    comments: Optional[str]

    drug_test_at: Optional[date] = Field(sa_column=Column("DrugTest"))
    drug_test_status: Optional[str] = Field(sa_column=Column("DrugTestStatus"))

    birth_city_name: Optional[str] = Field(sa_column=Column("BirthCityName"))
    birth_country_code: Optional[str] = Field(sa_column=Column("BirthCountryCode"))

    us_passport_number: Optional[str] = Field(sa_column=Column("USAPassportNum"))
    us_alien_registration_number: Optional[str] = Field(
        sa_column=Column("USAAlienRegNum")
    )

    alternative_passport_number: Optional[str] = Field(sa_column=Column("AltPassportNum"))
    alternative_passport_country: Optional[str] = Field(
        sa_column=Column("AltPassportCountry")
    )

    is_us_citizen: Optional[int] = Field(sa_column=Column("IsUSACitizen"))
    country_of_citizenship: Optional[str] = Field(
        sa_column=Column("CountryOfCitizenship")
    )

    driver_license_number: Optional[str] = Field(sa_column=Column("DriverLicNum"))
    driver_license_state: Optional[str] = Field(sa_column=Column("DriverLicState"))

    # roles: List["Role"] = Relationship(back_populates="attendees", link_model=AttendeeRoleLink)


class Role(SQLModel, table=True):
    __tablename__ = "Roles"

    id: Optional[int] = Field(primary_key=True, default=None)
    name: str = Field(sa_column=Column("Role"))
    description: str
    pay: float

    # attendees: List["Attendee"] = Relationship(back_populates="roles", link_model=AttendeeRoleLink)


class Language(SQLModel, table=True):
    __tablename__ = "Languages"

    id: Optional[int] = Field(primary_key=True, default=None)
    name: str = Field(sa_column=Column("Language"))
    comment: str


class LanguageCategory(SQLModel, table=True):
    __tablename__ = "LanguageCategory"

    id: Optional[int] = Field(primary_key=True, default=None)
    name: str = Field(sa_column=Column("category"))
    description: str
