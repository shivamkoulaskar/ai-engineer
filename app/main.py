from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/user")

class User(BaseModel):
    username:str 
    age:int 

@app.post("/user")
def validation(user:User):
    if(len(user.username)>3 and user.age>18):
        if user.username=="Shivam":
            return{
                "status":201,
                "message":"Login successful",
                "data":user
            }
        else:
            raise HTTPException(
                status_code=401,
                detail="Invalid Username"
            )
    else:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
















