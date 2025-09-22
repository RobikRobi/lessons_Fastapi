from typing import Literal
from pydantic import BaseModel, Field
from decimal import Decimal

# схема для создания счёта
class AccountCreate(BaseModel):
    name: str

# схема для пополнения баланса счёта
class AccountUpdate(BaseModel):
    inf: Literal["+", "-"]
    balance: Decimal = Field(ge=0, description="Сумма для изменения баланса")