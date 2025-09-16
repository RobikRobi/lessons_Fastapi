from fastapi import APIRouter

from src.login.login_shema import User

app = APIRouter(prefix="/users", tags=["Users"])

@app.post("/")
async def valid_password(user:User):
    if user.password != "123":
        return {"msg":"Отличный пароль!"}
    return {"msg: Пароль не должен содержать '123'!"}
