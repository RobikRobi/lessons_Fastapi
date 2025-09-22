from sqlalchemy import create_engine, ForeignKey, select
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

from .config import config

engine = create_engine(url=f'postgresql://{config.user}:{config.password}@localhost/lessons')
Session = sessionmaker(bind=engine)
session = Session()

def get_session():
    with Session() as session:
        yield session
        session.commit()
