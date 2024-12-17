from fastapi import FastAPI, Path
import uvicorn
from typing import Union , Optional  , Annotated #for generic types list,dic,
from pydantic import BaseModel

app = FastAPI()

userName:str = "Eesha Niaz"
# age:int = 20
listOfStudents: list[str] = ["Esha","Hamna","tehzeeb","zani"]




# def getUserFullName(firstName:str,lastName:str, age:int):
#     return firstName + " " + lastName + " " + age

# union 
def getUserFullName(firstName:str|int,lastName):
    return firstName

# Union[str,int] is a type that can be either str or int
# old version , we have to import union 
def getAge(age:Union[str,int]):
    return age


def getDetails(info:Optional[str]=None):      # means the info type may be optional string and default value is None
    return info


def start():
    uvicorn.run("todos.pythonTypes:app", host="127.0.0.1", port=8080, reload=True)
    
    
   
# **************Test-type-errors*******************    
    # BY using command mypy we can test the python types:
    #  poetry  add mypy
    # poetry shell  
    # mypy todos/pythonTypes.py => is command will suggest the python types error occur in dictionary, lists etc..
    
    
# ************Pydantic-Models-in-Python-for-dic-types************
# By using pydantic, we can define the types of key-values pair of dictionary and objects etc....
# what is BaseModel()  : 
# BaseModel() is a class in pydantic which is used to define the schema of the data
# it is used to define the data structure of the data


class Todo(BaseModel):
    id:int
    title:str
    description:str
    
# Create an instance of Todo instead of using a dictionary
car_info = Todo(
    id=562,
    title="BMW car",
    description="This is the latest version"
)



# Metadata => extra detail 
# Annotated is the part of standard library, you can import it from typing 

# Annotated[variableType,(metadata)var-description]

home: Annotated[str, "This is the name of my home"] = "The Warraich house"

# you can also use the 2nd parameter of annotated to provide FastAPI with additional metadata
# about how you want your application to behave 
# Annotated is mostly used for the validation
age:Annotated[int,Path(ge=10)] = 20 # Now path is function that tells FastAPI that the value of age is more greater then 10 
 
 
 






