from pydantic import BaseModel


class Сheck(BaseModel):

    balance: int

class UpdateCheck(BaseModel):
    
    id: int
    amount: int

class DelCheck(BaseModel):

    id: int