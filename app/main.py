from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    username:str 
    age:int 

@app.post("/user")
def validation(user:User):
    if(len(user.username)>3 and user.age>18):
        return{
            "status":201,
            "message":"Login Successful"
        }
    else:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
















