from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
class User(BaseModel):
    item:str 
    price:int 
    quantity:int 

@app.post("/order")
def order(user:User):
    if(user.price>0 and user.quantity>0):
        return{
            "status":200,
            "message":"Order placed",
            "total":user.price*user.quantity
        }
    else:
        return{
            "status":401,
            "Message":"Price and quantity is must be greater than 0"
        }















