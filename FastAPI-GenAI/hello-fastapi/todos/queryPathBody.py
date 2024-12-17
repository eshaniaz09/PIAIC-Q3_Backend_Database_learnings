from typing import Annotated
from fastapi import FastAPI, Body, Path, Query
import uvicorn
from pydantic import BaseModel , Field

app = FastAPI()
# defining path variables =>path params means we have to receive the data in path @app.get("/students/{id}") 
@app.get("/students/{id}")
def MainRout(id):
    print(id) # It prints in console
    return {
        "message": "server is up and running",
        "output": id
    }


# defining query parameters: we can write the values of variables in url by "?"
# like => http://127.0.0.1:8080/students_info?data=anyValue&name=Eesha
@app.get("/students_info")
def  get_students_info(data:str,name:str,count:int=10):
    return{
        "data": data,
        "name": name,
        "count":count
    }


# defining body parameters: In the postman url http://127.0.0.1:8080/items : we select the body/raw/json then define the dic like.....
# {
#     "id":2,
#     "title":"pencil box",
#     "description": "I have 10 pencils in my pencil box"
# }
# All the personal information is passed through body parameter
class Items(BaseModel):
    id:int
    title:str
    description:str
    
@app.get("/items")
def get_items(items:Items): 
    return items    
# ***************body-validation******************
# def get_items(items:Annotated[Items, Body()]): # Annotated is used to define the body parameter


#***************Query-validations*********************
class ID(BaseModel):
    myId:int
@app.get("/items_query")
def get_items_query(iD:Annotated[ID,Query(max_length=10,min_length=2)]):
    return iD

    
#*************path-validation**************
@app.get("/id-number/{id}")
def get_id_number(id:Annotated[int,Path(le=5,ge=3)]):  #le=less then and equal to , ge=greater then and equal to 
    return id
 



#*************multiple-body-params************
class userDetails(BaseModel):
    title:str
    description:str

class items(BaseModel):
    item_name:str
    item_price:float
    description:str

@app.get("/user-items/{id}")
def get_userInfo_items(id, userInfo:Annotated[userDetails,Body()], itemSelected:Annotated[items,Body()]):
    print(userInfo)
    print(id)
    return  itemSelected

# frontend side 
# url=>http://127.0.0.1:8080/user-items/09
# How to define data in body through postman: we have to define the nested keys 
# {
#     "userInfo":{
#     "title":"pencil box",
#     "description": "I have 10 pencils in my pencil box"
#     },
#     "itemSelected":{
#         "item_name":"shopping bag",
#         "item_price":209.08,
#         "description":"A handbag for laptop"
#     }

# }


# Note:we can also define the validation on the type of dic by using field(max-length,min-length..etc) like:


# class classItems(BaseModel):
#     board:str = Field()
#     noOfChairs:int= Field(max_length=10,min_length=2)


def start():
    uvicorn.run("todos.queryPathBody:app", host="127.0.0.1", port=8080, reload=True)
    
    
    
