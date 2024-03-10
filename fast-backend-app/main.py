from fastapi import FastAPI
from models.DataLoadLog import Base
from db.Conexion import engine

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get('/')
def index():
    return 'hola mundo'
