from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel #data validation
from typing import List, Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import desc

mekong = FastAPI()
models.Base.metadata.create_all(bind=engine)

class WaterQuality(BaseModel):
    TDS: int
    PHS: int
    DOS: int
    TempS: int
    
#==================================================================================================#
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()      
#==================================================================================================#
db_dependancy = Annotated[Session, Depends(get_db)]
#==================================================================================================#

@mekong.post('/waterquality/')
async def create_waterquality_database(waterquality: WaterQuality, db: db_dependancy):
    db_waterquality = models.WaterQuality(
        TDS = waterquality.TDS,
        PHS = waterquality.PHS,
        DOS = waterquality.DOS,
        TempS = waterquality.TempS
        )
    db.add(db_waterquality)
    db.commit()
    db.refresh(db_waterquality)
    
@mekong.get('/waterquality')
async def read_waterquality_database(db:db_dependancy):
    result = db.query(models.WaterQuality).order_by(desc(models.WaterQuality.id)).first()
    if not result:
        raise HTTPException(status_code=404, detail="database is not found.")
    return result
    
