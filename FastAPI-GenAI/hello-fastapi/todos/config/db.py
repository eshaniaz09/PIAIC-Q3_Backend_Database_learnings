from sqlmodel import SQLModel, create_engine
import os

# connecting table to database
connection_string = os.getenv("DB_CONNECTION_STRING")
if not connection_string:
    raise ValueError("Database connection string is not set in the environment variables.")

engine = create_engine(connection_string)

# Create all tables stored in this metadata.
def create_tables():
    SQLModel.metadata.create_all(engine)    