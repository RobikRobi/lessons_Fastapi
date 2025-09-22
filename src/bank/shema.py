from pydantic import BaseModel, Field

# схема для создания счёта
class AccountCreate(BaseModel):
    name: str

# схема для пополнения баланса счёта
class AccountUpdate(BaseModel):
    balance: float = Field(ge=0.0)