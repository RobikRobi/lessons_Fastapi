from fastapi import APIRouter

from src.guess_number.number_shema import Numbers
from random import randint

app = APIRouter(prefix="/numbers", tags=["Numbers"])

@app.post("/")
def guess_number(num:Numbers):
    rand_num = randint(0,10)
    if num.number == rand_num:
        return {"msg":f"Молодец! Ты угадал число! Моё число {rand_num}"}
    if num.number > rand_num:
        return {"msg":"Ты не угадал. Твоё число больше моего"}
    if num.number < rand_num:
        return {"msg":"Ты не угадал. Твоё число меньше моего"}
