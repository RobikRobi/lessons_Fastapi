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

    if account_update.inf == "+":
            account.balance += account_update.balance
    elif account_update.inf == "-":
        if account.balance < account_update.balance:
            raise HTTPException(status_code=400, detail="Insufficient funds")
        account.balance -= account_update.balance
    else:
        raise HTTPException(status_code=400, detail="Invalid operation, use '+' or '-'")

    session.commit()
    session.refresh(account)

    return {
        "message": f"Account {name} updated successfully",
        "balance": account.balance
        }  


# удалить счёт
@app.delete("/{name}/delete")
def close_account(name: str, session: Session = Depends(get_session)):
    account = session.scalar(select(Account).filter(Account.name == name))
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    if account.balance != 0.0:
        raise HTTPException(status_code=400, detail="Account must have zero balance to be closed")
    session.delete(account)
    session.commit()
    return {"message": f"Account with ID {name} closed successfully"}


