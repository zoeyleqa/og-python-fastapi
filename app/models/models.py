from typing import Optional, List
from sqlmodel import SQLModel, Field, Column, Relationship
from datetime import date

# TODO Relationship definitions

# Linker tables toward top, since they need to be defined first in order for base
# models to use them.


class AttendeeRoleLink(SQLModel, table=True):
    __tablename__ = "RS_People_Roles_Assigned"

    id: Optional[int] = Field(primary_key=True, default=None)
    RoleId: Optional[int] = Field(
        # sa_column=Column("RoleId"),
        default=None, foreign_key="Roles.id", primary_key=True,
    )
    HumanResourceId: Optional[int] = Field(
        # sa_column=Column("HumanResourceId"),
        default=None, foreign_key="RS_People.id", primary_key=True
    )
    pay: float


# class EventsOnSite(SQLModel, table=True):
#     __tablename__ = "Events_Sites_Assignment"

#     id: Optional[int] = Field(primary_key=True, default=None)
#     EventId: Optional[int] = Field(
#         default=None,
#         foreign_key="Events.id",
#         primary_key=True
#     )
#     SiteId: Optional[int] = Field(
#         default=None,
#         foreign_key="Sites.id",
#         primary_key=True
#     )

class AttendeeLangLink(SQLModel, table=True):
    __tablename__ = "RS_People_LangSkills_Assigned"

    id: Optional[int] = Field(primary_key=True, default=None)
    HumanResourceId: Optional[int] = Field(
        # sa_column=Column("HumanResourceId"),
        default=None, foreign_key="RS_People.id", primary_key=True,
    )
    LangId: Optional[int] = Field(
        # sa_column=Column("LangId"),
        default=None, foreign_key="Languages.id", primary_key=True
    )
    LangCatId: Optional[int] = Field(
        # sa_column=Column("LangCatId"),
        default=None, foreign_key="LanguageCategory.id", primary_key=True
    )
    test_date: Optional[date] = Field(
        sa_column=Column("TestDate"))
    test_score: Optional[float] = Field(
        sa_column=Column("TestScore"))


class UserTagPermLink(SQLModel, table=True):
    __tablename__ = "UserTagPermissions"

    id: Optional[int] = Field(primary_key=True, default=None)
    Tag: Optional[int] = Field(
        # sa_column=Column("RoleId"),
        default=None, foreign_key="PermissionTags.Tag", primary_key=True,
    )
    HumanResourceId: Optional[int] = Field(
        # sa_column=Column("HumanResourceId"),
        default=None, foreign_key="Users.User_ID", primary_key=True
    )
    # hr_id: Optional[int] = Field(
    #     sa_column=Column("HumanResourceId",
    #                      primary_key=True), foreign_key="Users.User_ID", 
    #     default=None
    # )
    # tag: Optional[str] = Field(
    #     sa_column=Column(
    #         "Tag", primary_key=False),
    #     foreign_key="PermissionTags.Tag",
    #     default=None
    # )
    access_rights: Optional[str] = Field(sa_column=Column("AccessRights"))


class UserExercisePermLink(SQLModel, table=True):
    __tablename__ = "UserExercisePermissions"

    id: Optional[int] = Field(primary_key=True, default=None)
    SubGroupId: Optional[int] = Field(
        # sa_column=Column("RoleId"),
        default=None, foreign_key="SubGroups.id", primary_key=True,
    )
    UserId: Optional[int] = Field(
        # sa_column=Column("HumanResourceId"),
        default=None, foreign_key="Users.User_ID", primary_key=True
    )
    # user_id: Optional[int] = Field(
    #     sa_column=Column("UserId",
    #                      foreign_key="Users.User_ID", primary_key=True),
    #     default=None
    # )
    # exercise_id: Optional[int] = Field(
    #     sa_column=Column(
    #         "SubGroupId", foreign_key="SubGroups.id", primary_key=True),
    #     default=None
    # )


# Base models below
class User(SQLModel, table=True):
    __tablename__ = "Users"

    id: Optional[int] = Field(sa_column=Column(
        "User_ID", primary_key=True), default=None)
    username: str
    first_name: str = Field(sa_column=Column("FirstName"))
    last_name: str = Field(sa_column=Column("LastName"))
    email: str
    password: str
    admin: str
    activation_token: str = Field(sa_column=Column("ActivationToken"))
    last_activation_request: int = Field(
        sa_column=Column("LastActivationRequest"))
    lost_password_request: int = Field(
        sa_column=Column("LostPasswordRequest"), default=0)
    active: int
    group_id: int = Field(sa_column=Column("Group_ID"))
    sign_up_date: int = Field(sa_column=Column("SignUpDate"))
    last_sign_in: int = Field(sa_column=Column("LastSignIn"))
    last_selected_event: int = Field(
        sa_column=Column("LastSelectedEvent"), default=0)
    password_request: Optional[str] = Field(
        sa_column=Column("PasswordRequest"))

    user_tag: Optional["PermissionTag"] = Relationship(
        back_populates="tag_user", link_model=UserTagPermLink)
    user_exercise: Optional["Exercise"] = Relationship(
        back_populates="exercise_user", link_model=UserExercisePermLink)


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
    social_security_number: Optional[str] = Field(
        sa_column=Column("SocialSecID"))
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
    force_protection_date: Optional[date] = Field(
        sa_column=Column("ForceProtectionDate"))
    clear_type: Optional[str] = Field(sa_column=Column("ClearType"))
    clear_expire_at: Optional[date] = Field(sa_column=Column("ClearExp"))
    medical_expire_at: Optional[date] = Field(sa_column=Column("MedicalExp"))
    liability_expire_at: Optional[date] = Field(sa_column=Column("LiabExp"))
    physical_date: Optional[date] = Field(sa_column=Column("PhysicalDate"))
    status: Optional[str]

    emergency_one_first_name: Optional[str] = Field(
        sa_column=Column("EFirstNameA"))
    emergency_one_last_name: Optional[str] = Field(
        sa_column=Column("ELastNameA"))
    emergency_one_phone_home: Optional[str] = Field(
        sa_column=Column("EPhoneHomeA"))
    emergency_one_phone_cell: Optional[str] = Field(
        sa_column=Column("EphoneCellA"))
    emergency_one_street: Optional[str] = Field(sa_column=Column("EStreetA"))
    emergency_one_city: Optional[str] = Field(sa_column=Column("ECityA"))
    emergency_one_state: Optional[str] = Field(sa_column=Column("EStateA"))
    emergency_one_zip: Optional[str] = Field(sa_column=Column("EZipA"))

    emergency_two_first_name: Optional[str] = Field(
        sa_column=Column("EFirstNameB"))
    emergency_two_last_name: Optional[str] = Field(
        sa_column=Column("ELastNameB"))
    emergency_two_phone_home: Optional[str] = Field(
        sa_column=Column("EPhoneHomeB"))
    emergency_two_phone_cell: Optional[str] = Field(
        sa_column=Column("EphoneCellB"))
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
    birth_country_code: Optional[str] = Field(
        sa_column=Column("BirthCountryCode"))

    us_passport_number: Optional[str] = Field(
        sa_column=Column("USAPassportNum"))
    us_alien_registration_number: Optional[str] = Field(
        sa_column=Column("USAAlienRegNum")
    )

    alternative_passport_number: Optional[str] = Field(
        sa_column=Column("AltPassportNum"))
    alternative_passport_country: Optional[str] = Field(
        sa_column=Column("AltPassportCountry")
    )

    is_us_citizen: Optional[int] = Field(sa_column=Column("IsUSACitizen"))
    country_of_citizenship: Optional[str] = Field(
        sa_column=Column("CountryOfCitizenship")
    )

    driver_license_number: Optional[str] = Field(
        sa_column=Column("DriverLicNum"))
    driver_license_state: Optional[str] = Field(
        sa_column=Column("DriverLicState"))

    langs: Optional["Language"] = Relationship(
        back_populates="attendee_lang", link_model=AttendeeLangLink)
    lang_cats: Optional["LanguageCategory"] = Relationship(
        back_populates="attendee_lang_cat", link_model=AttendeeLangLink)
    attendee_roles: Optional["Role"] = Relationship(
        back_populates="role_attendee", link_model=AttendeeRoleLink)


class Role(SQLModel, table=True):
    __tablename__ = "Roles"

    id: Optional[int] = Field(primary_key=True, default=None)
    name: str = Field(sa_column=Column("Role"))
    description: str
    pay: float

    role_attendee: Optional[Attendee] = Relationship(
        back_populates="attendee_roles", link_model=AttendeeRoleLink)


class Site(SQLModel, table=True):
    __tablename__ = "Sites"

    id: Optional[int] = Field(primary_key=True, default=None)
    name: str = Field(sa_column=Column("Name"))
    description: str = Field(sa_column=Column("Description"))
    country: str = Field(sa_column=Column("Country"))
    city: str = Field(sa_column=Column("City"))
    state: str = Field(sa_column=Column("State"))
    latitude: Optional[float] = Field(sa_column=Column("LatDeg"))
    latitude_min: Optional[float] = Field(sa_column=Column("LatMin"))
    latitude_sec: Optional[float] = Field(sa_column=Column("LatSec"))
    longitude: Optional[float] = Field(sa_column=Column("LongDeg"))
    longitude_min: Optional[float] = Field(sa_column=Column("LongMin"))
    longitude_sec: Optional[float] = Field(sa_column=Column("LongSec"))

    # events: List["Event"] = Relationship(
    #   back_populates="sites",
    #   link_model=EventsOnSite
    # )


class Event(SQLModel, table=True):
    __tablename__ = "Events"

    id: Optional[int] = Field(primary_key=True, default=None)
    name: str = Field(sa_column=Column("Name"))
    open_at: Optional[date] = Field(sa_column=Column("OpenDate"))
    start_at: date = Field(sa_column=Column("StartDate"))
    end_at: date = Field(sa_column=Column("EndDate"))
    infil_suspend_at: Optional[date] = Field(
        sa_column=Column("InfilSuspenseDate")
    )
    exfil_suspend_at: Optional[date] = Field(
        sa_column=Column("ExfilSuspenseDate")
    )
    po_suspend_at: Optional[date] = Field(sa_column=Column("POSuspenseDate"))
    final_suspend_at: Optional[date] = Field(
        sa_column=Column("FinalSuspenseDate")
    )
    allow_override_dates: Optional[bool] = Field(
        sa_column=Column("OverrideDates")
    )

    SubGroupId: int = Field(
        default=None, foreign_key="SubGroups.id"
    )
    event_exercise: "Exercise" = Relationship(back_populates="exercise_event")
    # sites: List["Site"] = Relationship(
    #     back_populates="events",
    #     link_model=EventsOnSite
    # )


class Group(SQLModel, table=True):
    __tablename__ = "MainGroups"

    id: Optional[int] = Field(primary_key=True, default=None)
    name: str = Field(sa_column=Column("Name"))
    unit: Optional[str] = Field(sa_column=Column("Unit"))
    lead_one: Optional[str] = Field(sa_column=Column("OGTLead1"))
    lead_two: Optional[str] = Field(sa_column=Column("OGTLead2"))

    group_exercise: Optional["Exercise"] = Relationship(back_populates="group")


class Exercise(SQLModel, table=True):
    __tablename__ = "SubGroups"

    id: Optional[int] = Field(primary_key=True, default=None)
    name: str = Field(sa_column=Column("Name"))
    description: Optional[str] = Field(sa_column=Column("Description"))
    background_color: Optional[str] = Field(sa_column=Column("BkColor"))
    text_color: Optional[str] = Field(sa_column=Column("TextColor"))

    GroupId: Optional[int] = Field(
        default=None, foreign_key="MainGroups.id"
    )
    group: Optional[Group] = Relationship(back_populates="group_exercise")
    exercise_event: Optional[Event] = Relationship(
        back_populates="event_exercise")
    exercise_user: Optional[User] = Relationship(
        back_populates="user_exercise", link_model=UserExercisePermLink)


class Language(SQLModel, table=True):
    __tablename__ = "Languages"

    id: Optional[int] = Field(primary_key=True, default=None)
    name: str = Field(sa_column=Column("Language"))
    comment: str

    attendee_lang: Optional[Attendee] = Relationship(
        back_populates="langs", link_model=AttendeeLangLink)


class LanguageCategory(SQLModel, table=True):
    __tablename__ = "LanguageCategory"

    id: Optional[int] = Field(primary_key=True, default=None)
    name: str = Field(sa_column=Column("category"))
    description: str

    attendee_lang_cat: Optional[Attendee] = Relationship(
        back_populates="lang_cats", link_model=AttendeeLangLink)


class PermissionTag(SQLModel, table=True):
    __tablename__ = "PermissionTags"

    id: Optional[int] = Field(primary_key=True, default=None)
    tag: str = Field(sa_column=Column("Tag"))
    # tag: Optional[str] = Field(
    #     sa_column=Column("Tag", foreign_key="UserTagPermissions.tag"),
    #     default=None
    # )
    tag_user: Optional[User] = Relationship(
        back_populates="user_tag", link_model=UserTagPermLink)
