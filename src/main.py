from fastapi import FastAPI
from src.login.login_router import app as login_router
from src.guess_number.number_router import app as number_router


app = FastAPI()

app.include_router(login_router)
app.include_router(number_router)


@app.get("/")
def great():
    return{"msg":"It's, ok!"}