from fastapi import FastAPI
from src.db import engine, Base
from binascii import Error
from src.bank.router import app as bank_router


app = FastAPI()

app.include_router(bank_router)


@app.get("/")
def init():
    Base.metadata.create_all(engine)
    return{"Hello":"BankingAPP!"}