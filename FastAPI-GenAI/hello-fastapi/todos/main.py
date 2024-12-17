# from fastapi import FastAPI
# import uvicorn

# app = FastAPI()

# # defining the get api
# @app.get("/gettodos") #This is responsible to catch the frontend request and match the /gettodos rout and call the gettodos function in response , the function below is called in the frontend request not in this python program, it only defines here
# # function definition
# def gettodos():
#     print("Get todos called")
#     return "Congratulations 😍 Get todos called" 


# # query-params 
# @app.get("/helloWorld")
# def helloWorld(userName:str,rollNo:str):
#     print("Get todos called", userName,rollNo)
#     return "Hello esha welcome to postman"

# # path variables
# @app.get("/getSingleTodo/{id}")
# def getSingleTodo(id):
#     print("Get single todo called ",id)
#     return "Get single todo called " + id



# # Q: Make a list of students and add new student in it

# # creating students list 
# students = [{
#     "userName": "Ali",
#     "rollNumber": 8077
# }]
# # function to call students list
# @app.get("/students")
# def get_students():
#     return students
# # function to add the new student in students list
# @app.get("/addStudent")
# def addStudent(userName:str,rollNo:str):
#     global students
#     students.append({ "userName": userName, "rollNumber": rollNo})
#     return students


# @app.post("/getSingleTodo")
# def getSingleTodo():
#     print("Get single todo called")
#     return "Get single todo called"


# @app.put("/updateTodo")
# def updateTodo():
#     return "Update todo called"

# @app.delete("/deleteTodo")
# def deleteTodo():
#     return "Delete todo called"
# # Note: 
# # The rout-name/function-name can be same but only in the case the api type should be different
# # For example: @app.get("/gettodos") and @app.post("/gettodos") are allowed
# #  but @app.get("/gettodos") and @app.get("/gettodos") are not allowed.
# # Now have to run our python program all the time by using uvicorn library 
# # What is uvicorn: 
# # uvicorn is a ASGI server for python, it is used to run the fastapi application
# # it is used to run the fastapi application in the production environment ,development environment,testing environment


# def start():
#     uvicorn.run("todos.main:app", host="127.0.0.1", port=8080, reload=True)



# # 127.0.0.1 and 0.0.0.0 is the local host ip address

# # how to run this start function=> IN pyproject/toml file we have to write: 
# # [tool.poetry.scripts]
# # start= "todos.main:start"

# # Now in the cmd run => poetry run start

# # Note:How get the documentation of our project : 
# #   http://127.0.0.1:8080/docs      (all methods and rout created are shown in this link )



# # ****************Data-Receiving-from-frontend-through-api************************

# # path variable:
# # path variable is used to get the data from the frontend through the api
# # example: dynamic-path/path-variable
# # @app.get("/getSingleTodo/{id}")
# # def getSingleTodo(id):
# #     print("Get single todo called",id)
# #     return "Get single todo called" + id
# # we have to give the value of id at run time dynamically at =>http://127.0.0.1:8080/getSingleTodo/13  here 13 = id 
# # path-variable is not a good method ,so  we use =>Query params 


# # Query parameters:
# # Query parameters are used to get the data from the frontend through the api, we don't have to define the path variables in the function parameter
# # example: dynamic-path?query-param=query-value
# # query-params 
# # @app.get("/helloWorld")
# # def helloWorld(userName:str,rollNo:str):
# #     print("Get todos called", userName,rollNo)
# #     return "Hello esha welcome to postman"

# # we have to define the variable key-value through postman 
# # http://127.0.0.1:8080/helloWorld?userName=Eesha Niaz&rollNo=09



