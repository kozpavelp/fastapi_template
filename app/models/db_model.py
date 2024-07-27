from sqlalchemy.orm import mapped_column, Mapped

from app.db.db_session import Base


class DBModel(Base):
    __tablename__ = "db_model"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(index=True) # Индекс для примера
    description: Mapped[str] # Достаточно просто аннотации для описания типа данных
    note: Mapped[str] = mapped_column(nullable=True) # nullable=True для примера

#    id = Column(Integer, primary_key=True, index=True)
#    name = Column(String, index=True)
#    description = Column(String, index=True)

