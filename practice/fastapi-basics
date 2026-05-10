from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

class Login(BaseModel):
    username:str 
    password:str 

@app.post("/login")
def login(user:Login):
    if user.username=="Shivam":
        if len(user.username)<3 and len(user.password)<8:
            return{
                "status":401,
                "Message":"Error"
            }
        else:
            return{
                "status":200,
                "Message":"Login Successful"
            }
    else:
        return{
            "status":401,
            "Message":"username must be shivam "
        }





















