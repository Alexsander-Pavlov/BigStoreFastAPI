from typing import (List,
                    Optional,
                    )
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import (DeclarativeBase,
                            Mapped,
                            mapped_column,
                            relationship,
                            declared_attr,
                            )


class Base(DeclarativeBase):
    """Базовая модель
    """
    __abstract__ = True
    
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'

    id: Mapped[int] = mapped_column(primary_key=True)