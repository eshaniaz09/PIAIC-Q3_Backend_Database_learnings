from fastapi import FastAPI, HTTPException
import uvicorn
from sqlmodel import Session, select
from .config.db import create_tables , engine
from .models.tdoos import Todos, UpdateTodos 
from dotenv import load_dotenv
import os 
load_dotenv()


app = FastAPI()

  
# Reading data from postgres SQL (Retrieving a data from database by using session)
@app.get("/getTodos")
def getTodos():
    with Session(engine) as session:
        statement = select(Todos)
        result = session.exec(statement)
        data = result.all()
        print(data)
        return data

# updateTodos
@app.put("/update_todo/{id}")
def update_todo(todo: UpdateTodos):
    with Session(engine) as session:
        db_todo = session.get(Todos, id)
        if not db_todo:
            raise HTTPException(status_code=404,detail="Todo not found")
        todo_data = todo.model_dump(exclude_unset=True) 
        db_todo.sqlmodel_update(todo_data)
        session.add(db_todo)
        session.commit()
        session.refresh(db_todo)
        return {"status":200,"message":"todo update"}
    


#To create todos in table 
@app.post("/create_todo")
def create_todo(todo: Todos):
    try:
        with Session(engine) as session:
            session.add(todo)
            session.commit()
            session.refresh(todo)
            return {"status": 200, "message": "todo created"}
    except Exception as e:
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

 

@app.delete("/delete_todo/{todo_id}")
def delete_todo(todo_id):
    try:
        with Session(engine) as session:
            db_todo = session.get(Todos, todo_id)
            if not db_todo:
                raise HTTPException(status_code=404,detail="Todo not found")
            session.delete(db_todo)
            session.commit()
            session.refresh(db_todo)
            return {"status":200,"message":"todo deleted"}
    except Exception as e:
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
        
    
    


def start():
    create_tables()
    uvicorn.run("todos.sqlModel:app", host="127.0.0.1", port=8080, reload=True)
    
