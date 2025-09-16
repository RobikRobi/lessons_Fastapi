from fastapi import FastAPI
from src.login.login_router import app as login_router


app = FastAPI()

app.include_router(login_router)


@app.get("/")
def great():
    return{"msg":"It's, ok!"}