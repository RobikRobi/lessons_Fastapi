from pydantic import BaseModel


class Сheck(BaseModel):

    cash: int

class IdCheck(BaseModel):

    id: int

class UpdateCheck(BaseModel):
    
    id: int
    amount: int

class DelCheck(BaseModel):

    id: int