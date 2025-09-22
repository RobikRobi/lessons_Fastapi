from fastapi import APIRouter, Depends
from src.db import get_session
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.bank.models import Account
from src.bank.shema import AccountCreate, AccountUpdate


app = APIRouter(prefix="/bank", tags=["Bank"])


# создать счёт
@app.post("/")
def creat_account(name:str, session: Session = Depends(get_session)):
    new_account = Account(name=name)
    session.add(new_account)
    session.commit()

#узнать баланс счёта
@app.get("/{name}/balance")
def get_balance(name: str, session: Session = Depends(get_session)):
    account = session.scalar(select(Account).filter(Account.name == name))
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account.balance


# обновить счёт
@app.put("/{name}/deposit")
def deposit_to_account(name: str, account_update: AccountUpdate, 
                       session: Session = Depends(get_session)):
    account = session.scalar(select(Account).filter(Account.name == name))
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")

    account.balance += account_update.balance
    session.commit()
    session.refresh(account)

    return {"message": f"Deposit of {account_update.balance} to account {name}"}


# # DELETE
# session.delete(user)
# session.commit()
# # @app.get("/{account_id}/balance", response_model=float)
# # def get_balance(account_id: str, session: Session = Depends(get_session)):
# #     account = session.scalar(select(Account).filter(Account.id == account_id))
# #     if not account:
# #         raise HTTPException(status_code=404, detail="Account not found")
# #     return account.balance


