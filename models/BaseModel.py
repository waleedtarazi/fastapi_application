from sqlalchemy.ext.declarative import declarative_base

from db.database import Engine

# Base Entity Model Schema
EntityMeta = declarative_base()


def initDB():
    EntityMeta.metadata.create_all(bind=Engine)
