from datetime import date

from sqlalchemy import Date, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Machine(Base):
    __tablename__ = "machines"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    machine_code: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        index=True
    )

    machine_name: Mapped[str] = mapped_column(
        String(100)
    )

    manufacturer: Mapped[str] = mapped_column(
        String(100)
    )

    sector: Mapped[str] = mapped_column(
        String(100)
    )

    installation_date: Mapped[date] = mapped_column(
        Date
    )

    status: Mapped[str] = mapped_column(
        String(50)
    )

    hourly_capacity: Mapped[int] = mapped_column(
        Integer
    )