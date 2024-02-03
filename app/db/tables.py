# create a sqlite db py running app/db/tables.py in root directory.
# only need to run once or you can delete the file and start over if you wanna
from sqlalchemy import create_engine
from sqlalchemy import Column, Boolean, Text, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("sqlite:///applications.db", echo=True)
Base = declarative_base()


class Names(Base):
    __tablename__ = "names"
    id = Column(String, primary_key=True)
    names = Column(Text, nullable=False)


if __name__ == "__main__":
    db_session = scoped_session(sessionmaker(bind=engine))
    Base.metadata.create_all(engine)