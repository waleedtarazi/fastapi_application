# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from db.database import Engine

# Base Entity Model Schema
EntityMeta = declarative_base()


def init_db():
    """initilize the Database connection"""
    EntityMeta.metadata.create_all(bind=Engine)
    for table_name in EntityMeta.metadata.tables:
        print(f"Creating table: {table_name}")
