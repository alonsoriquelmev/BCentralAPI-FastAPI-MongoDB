from typing import List
# from .data.data import swaps_from_bc
import pandas as pd
import datetime as dt
from .database import dbase
import app.schemas as schemas

async def get_swaps_daterange(request: schemas.SwapCamRequest) -> List[schemas.SwapResponse]:
    swap_cam = dbase['swap_cam']
    date_ini = datetime.datetime.combine(request.date_ini, datetime.time.min)
    date_end = datetime.datetime.combine(request.date_end, datetime.time.max)
    data = swap_cam.find({'swap_index':request.swap_name,'tenor':request.tenor,'fecha':{'$lt':date_end,'$gte':date_ini}},{"_id":0})
    output_list = []
    for x in data:
        output_list.append(x)
    
    return output_list

async def get_imacec_date(year:str) -> List[schemas.ImacecResponse]:

    imacec = dbase['imacec']
    data = imacec.find({'Año':year},{"_id":0})
    output_list = []
    for x in data:
        output_list.append(x)
    
    return output_list
