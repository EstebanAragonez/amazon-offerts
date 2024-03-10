from fastapi import FastAPI, HTTPException, status
from fastapi.params import Depends
from typing import List
from models.models import Base, DataLoadLog
import models.Schemas as schemas
from db.Conexion import engine, get_db
from sqlalchemy.orm import Session
from datetime import datetime
from ProductDealETL import ProductDealETL

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get('/')
def index():
    return 'hola que haces uwu'

@app.get('/DataLoadLog/',response_model=List[schemas.DataLoadLog])
def show_DateLog(db:Session=Depends(get_db)):
    try:
        # Verifica si hay algún objeto en la tabla DataLoadLog
        date_logs = db.query(DataLoadLog).all()

        productDealETL = ProductDealETL(date = datetime.now().date())
        productDealETL.load_date_csv(db=db)

    except Exception as e:
        # Captura cualquier excepción y devuelve un error HTTP
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error inesperado: {str(e)}"
        )

    return date_logs
