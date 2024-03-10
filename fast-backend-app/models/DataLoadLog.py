from db.Conexion  import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text


class Post(Base):
    __tablename__ = "DataLoadLog"

    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(TIMESTAMP(timezone=True), server_default=text('now()'))