from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import config


host = config["DB_HOST"]
dbname = config["DB_NAME"]
user = config["DB_USER"]
password = config["DB_PASSWORD"]
connection_string = f"host={host} dbname={dbname} user={user} password={password}"


SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}/{dbname}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={},  # , connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
