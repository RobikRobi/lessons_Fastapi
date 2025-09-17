from fastapi import APIRouter

from scr.bank_acount.bank_shema import Check
from scr.bank_acount.bank_sheme import IdCheck
from scr.bank_acount.bank_sheme import DelCheck
from scr.bank_acount.bank_sheme import UpdateCheck

app = APIRouter(prefix="/bank", tags=["Bank"])

deposit = [100, 200, 0]

# добавить запись в массив
@app.post("/add_check") 
def cash_add(check:Check):
    deposit.append(check)
    return {"msg":"Ваши средства переведены на депозит"}

# id - получение определенного числа из массива
@app.get("/get_check")
def cash_get(id:IdCheck):
    if id <= len(deposit):
        return deposit[id]
    else:
        return {"msg":"Такого счёта не существует!"}

# id - bal(int -inf до +inf) - сколько прибавляем к balance - уменьшить или увеличить баланс по id в массиве
@app.put("put_check")
def update_check(check:UpdateCheck):
    if 0 <=  check.id < len(deposit):
        deposit[check.id] += check.amount
    else:
        print("Ошибка: индекс вне диапазона")

@app.delete("/delet_check")
def cash_delet(id:DelCheck):
    if id <= len(deposit):
        cash = deposit.pop(id)
        return {"msg":f"Ваши средства на сумму {cash}, были выведены со счёта"}
    else:
        return {"msg":"Такого счёта не существует!"}
