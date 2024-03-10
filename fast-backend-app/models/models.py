from db.Conexion import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Date, Boolean, text, String, URL, ForeignKey, Numeric

class DataLoadLog(Base):
    __tablename__ = "DataLoadLog"

    id = Column(Integer, primary_key=True, nullable=False)
    date = Column(Date, server_default=text('now()'))
    product_deals = relationship('ProductDeal', back_populates='date_log')

class ProductDeal(Base):
    __tablename__ = "ProductDeal"

    id = Column(Integer, primary_key=True, nullable=False)
    title =  Column(String)
    price = Column(Numeric(precision=10, scale=2), nullable=True)
    total_rating = Column(Integer, nullable=True)
    img = Column(String)
    discount = Column(Integer, nullable=True)
    url = Column(String)
    date = Column(Date, server_default=text('now()'))

    # Add the foreign key constraint and relationship definition
    date_log_id = Column(Integer, ForeignKey('DataLoadLog.id'))
    date_log = relationship('DataLoadLog', back_populates='product_deals')
