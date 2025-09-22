from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Numeric
from src.db import Base

class Account(Base):
    __tablename__ = 'accounts'

    name: Mapped[str] = mapped_column(unique=True, primary_key=True)
    balance: Mapped[float] = mapped_column(Numeric(10, 2), default=0.0)#для фиксированной точности баланса


