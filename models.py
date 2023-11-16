from sqlalchemy import Boolean, Column, Integer, ForeignKey, String
from database import Base

class WaterQuality(Base):
    __tablename__ = 'waterquality'
    
    id = Column(Integer, primary_key=True, index=True)
    TDS = Column(Integer, index=True)
    DOS = Column(Integer, index=True)
    PHS = Column(Integer, index=True)
    TempS = Column(Integer, index=True)
    