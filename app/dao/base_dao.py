from sqlalchemy import select, insert
from typing import Generic, TypeVar
from app.db.db_session import async_session_maker


T = TypeVar("T")
'''
создаем универсальный тип T. Этот тип можно использовать для указания того, что методы класса будут работать
с любым типом данных, который будет указан при создании конкретного экземпляра этого класса.
'''


class BaseDAO(Generic[T]):  # базовый класс BaseDAO для доступа к данным
    model = None

    '''
    Методы класса, такие как find_one_or_none, find_all, add_data, и delete_data,
    используют тип T для обозначения типа возвращаемого значения и для работы с данными.
    find_one_or_none возвращает объект типа T или None, что делает его универсальным и применимым для различных моделей.
    '''

    @classmethod
    async def find_one_or_none(cls, **kwargs) -> T | None:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**kwargs)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, **filter_by) -> list[T]:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def add_data(cls, **data) -> None:
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete_data(cls, **filter_by) -> str:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = (await session.execute(query)).scalar_one_or_none()
            await session.delete(result)
            await session.commit()
            return f'{result.id} deleted successfully'
