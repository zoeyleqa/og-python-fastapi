from sqlmodel import SQLModel, create_engine, Session
import os

database_name = os.getenv('DATABASE_NAME')
database_user = os.getenv('DATABASE_USER')
database_password = os.getenv('DATABASE_PASSWORD')
database_host = os.getenv('DATABASE_HOST')
database_port = os.getenv('DATABASE_PORT')

# The recommended MySQL dialects are mysqlclient and PyMySQL.
mysql_url = f"mysql+pymysql://{database_user}:{database_password}@{database_host}:{database_port}/{database_name}"
connect_args = {}
engine = create_engine(mysql_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
  SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

def get_db():
    with Session(engine) as session:
      try:
          yield session
          session.commit()
      finally:
          session.close()