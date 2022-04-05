from enum import Enum

from fastapi import FastAPI

app = FastAPI()

# first steps
@app.get("/")
async def root():
    return {"message": "Hello World"}
    
# Using path parameters
#@app.get('/items/{item_id}')
#async def read_item(item_id):
#    return {"item_id": item_id}

# Path parameters with types
@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {"item_id": item_id}

# Order matters in when creating  path operations
# If the /users/{user_id} path comes before the /users/me path,
# the path for the former would match for /users/me thinking that it's recieving a parameter user_id with a value "me"

@app.get('/users/me')
async def read_user_me():
    return {"user_id": "the current user"}

@app.get('/users/{user_id}')
async def read_user(user_id: str):
    return {"user_id": user_id}

# Predefined values with enum
class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'

@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {'model_name': model_name, 'message': 'Deep Learning FTW!'}
    
    if model_name.value == 'lenet':
        return {'model_name': model_name, 'message': 'LeCNN all the images'}
    
    return {'model_name': model_name, 'message': 'Have some residuals'}

# Path parameters containing paths
@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {'file_path': file_path}