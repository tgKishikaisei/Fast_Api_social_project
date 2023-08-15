from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Admin@localhost/social_media'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Sessionalocal = sessionmaker(bind=engine)

Base = declarative_base()

from database.models import *

def get_db():
    db = Sessionalocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

        
