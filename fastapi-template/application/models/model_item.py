from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from typing import Optional
import pytz
from sqlalchemy.ext.declarative import declarative_base


class Base(DeclarativeBase):
    """
    Class for the Postgres Database.

    :param DeclarativeBase: DeclarativeBase from sqlalchemy.orm.
    :type DeclarativeBase: DeclarativeBase
    """

    pass


class Item(Base):
    """
    Class for the Item table in the Postgres Database.

    :param Base: Base class created with sqlalchemy.orm.DeclarativeBase.
    :type Base: sqlalchemy.orm.DeclarativeBase
    """

    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(pytz.utc))
    last_time_updated: Mapped[datetime] = mapped_column(default=datetime.now(pytz.utc))
    name: Mapped[str]
    description: Mapped[Optional[str]]
