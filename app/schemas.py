from pydantic import BaseModel
import datetime as dt
from typing import List

class SwapResponse(BaseModel):
    Fecha: List[dt.date]
    Swap_Index: List[str]
    Tenor: List[str]
    Valor: List[float]
    class Config:
        orm_mode = True

class SwapCamRequest(BaseModel):
    swap_name: str
    date_ini: dt.date
    date_end: dt.date
    class Config:
        orm_mode = True

class DateRangeRequest(BaseModel):
    code: str
    date_ini: str
    date_end: str

# class YearRequest(BaseModel):
#     code: str
#     year: str

class ImacecResponse(BaseModel):
    IMACEC: float
    PROD: float
    MIN: float
    IND: float
    RESTG: float
    COM: float
    SERV:float 
    IMACEC_CF:float
    IMACEC_NM:float 
    Mes: str
    Año: str
