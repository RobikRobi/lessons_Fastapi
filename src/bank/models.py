from sqlalchemy.orm import Mapped, mapped_column
from src.db import Base

class Account(Base):
    __tablename__ = 'accounts'

    name: Mapped[str] = mapped_column(unique=True, primary_key=True)
    balance: Mapped[float] = mapped_column(default=0.0)


