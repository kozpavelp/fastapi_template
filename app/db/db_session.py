from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from app.config import config

# Асинхронный движок базы данных
engine = create_async_engine(config.DATABASE_URL, echo=True)

# фабрика асинхронных сессий
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
#  expire_on_commit=False означает, что объекты не будут автоматически становиться устаревшими (detached) после коммита транзакции


# базовый класс для всех моделей в приложении
class Base(DeclarativeBase):
    pass
