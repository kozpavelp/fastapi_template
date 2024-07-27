from app.dao.base_dao import BaseDAO
from app.models.db_model import DBModel


class DBModelDAO(BaseDAO):  # конкретный DAO для модели DBModel.
    model = DBModel

