from fastapi import FastAPI
from .services import get_imacec_date
from typing import List
import app.schemas as schemas

app = FastAPI()

@app.get('/imacec/{year_request}', response_model = List[schemas.ImacecResponse])
async def imacec_by_year(year_request: str):
    response = await get_imacec_date(year=year_request)
    return response


# @app.post('/swapcam/daterange', response_model = List[schemas.SwapResponse])
# async def swapcam_by_daterange(request_body: schemas.SwapCamRequest):
#     response = await get_swapcam_daterange(request_body)
#     return response


# @app.post('/test')
# async def test(request_body: schemas.SwapCamRequest):
#     response = await get_swapcam_daterange(request_body)
#     return response

