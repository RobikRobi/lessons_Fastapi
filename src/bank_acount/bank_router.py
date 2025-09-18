from fastapi import APIRouter

from src.bank_acount.bank_shema import Сheck
from src.bank_acount.bank_shema import DelCheck
from src.bank_acount.bank_shema import UpdateCheck

app = APIRouter(prefix="/bank", tags=["Bank"])

deposit = [100, 200, 0]

# Добавить запись в массив
@app.post("/add_check")
def cash_add(check: Сheck):
    deposit.append(check.balance)
    return {"msg": "Ваши средства переведены на депозит", "deposit": deposit}


# Получить запись по id (через query параметр)
@app.get("/get_check")
def cash_get(id: int):
    if 0 <= id < len(deposit):
        return {"balance": deposit[id]}
    else:
        return {"msg": "Такого счёта не существует!"}


# Обновить баланс по id
@app.put("/put_check")
def update_check(check: UpdateCheck):
    if 0 <= check.id < len(deposit):
        deposit[check.id] += check.amount
        return {"msg": "Баланс обновлён", "balance": deposit[check.id]}
    else:
        return {"msg": "Ошибка: индекс вне диапазона"}


# Удалить запись по id
@app.delete("/delete_check")
def cash_delete(id: int):
    if 0 <= id < len(deposit):
        cash = deposit.pop(id)
        return {"msg": f"Ваши средства на сумму {cash} были выведены со счёта"}
    else:
        return {"msg": "Такого счёта не существует!"}