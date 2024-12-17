# sql-model fastapi data fetching and connection with postgresql

from fastapi import FastAPI
import uvicorn
from sqlmodel import Field, SQLModel, Session, create_engine, select

app = FastAPI()

# connecting table to database

connection_string = 'postgresql://postgres.hiskhygafkgouitenqwd:Vsy9Wps4DM!PbnB@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres'
connection = create_engine(connection_string)

# create_engine => to create connection , it needs a connection string

# Field => To design database model

# table=True => create a table

# creating table:

class Todos(SQLModel, table=True):
id: int = Field(default=None, primary_key=True)
title:str
description:int
is_completed: bool

# Create all tables stored in this metadata.

SQLModel.metadata.create_all(connection)

# Reading data from postgres SQL (Retrieving a data from database by using session)

@app.get("/getPersons")
def getPersons():
with Session(connection) as session:
statement = select(Persons)
result = session.exec(statement)
data = result.all()
print(data)
return data

def start():
uvicorn.run("todos.sqlModel:app", host="127.0.0.1", port=8080, reload=True)
