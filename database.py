from sqlalchemy import create_engine  #sqlalchemy is ORM
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# URL_DATABASE = "postgresql://username:password@localhost:5432/db_name"
URL_DATABASE = "postgresql://postgres:panha123@localhost:5432/postgres"

engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
