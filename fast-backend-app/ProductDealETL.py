import pandas as pd
import numpy as np
from datetime import datetime
from models.DataLoadLog import DataLoadLog, ProductDeal
from decimal import Decimal

class ProductDealETL():

    def __init__(self, date = None):
        self.path = f'products-deal-{date}.csv'
        try:
            self.df = pd.read_csv(f'./data/{self.path}')
        except  FileNotFoundError as e:
            raise(e)

    def load_date_csv(self, db):
        self.df['date'] = pd.to_datetime(self.df['date'])

        data_load_log  = db.query(DataLoadLog).filter_by(date = datetime.now().date()).first()

        if not data_load_log:
            data_load_log  = DataLoadLog(date=datetime.now().date())
            db.add(data_load_log)
            db.commit()

        for _, row in self.df.iterrows():
            product_deal = ProductDeal(
            title=row['title'],
            price=float(row['price'].replace('$', '').replace(',', '')),
            total_rating= 0 if '$' in row['total_rating'] else int(row['total_rating'].replace(',', '')),
            img=row['img'],
            discount=int(row['discount'].replace('%', '')),
            url=row['url'],
            date=row['date'].date(),
            date_log=data_load_log 
        )
            db.add(product_deal)
        db.commit()
