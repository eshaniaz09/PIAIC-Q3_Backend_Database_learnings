from sqlmodel import SQLModel,Field


# creating table/models: 
# Field => To design database model
# table=True => create a table
class Todos(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    is_completed: bool = False
    
    
class UpdateTodos(SQLModel):
    title:str | None
    description:int | None
    is_completed: bool | None