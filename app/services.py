from typing import List
# from .data.data import swaps_from_bc
import pandas as pd
import datetime as dt
from .database import dbase
import app.schemas as schemas

# async def get_swapcam_daterange(request: schemas.SwapCamRequest) -> List[schemas.SwapResponse]:
#     year_ini = pd.to_datetime(request.date_ini).year
#     year_end = pd.to_datetime(request.date_end).year
#     years_diff = year_end - year_ini
#     # date_ini = dt.date.strptime(request.date_ini,
#     if years_diff == 0:
#         df_swaps = swaps_from_bc(str(year_ini))
#         df_swaps = df_swaps.sort_values('Fecha')
#     elif years_diff != 0:
#         year_aux = year_ini
#         df_swaps = pd.DataFrame()
#         for i in range(years_diff+1):
#             df_aux = swaps_from_bc(str(year_aux))
#             df_swaps = pd.concat([df_swaps,df_aux])
#             year_aux += 1
#         df_swaps = df_swaps.sort_values('Fecha')

#     data_swaps = df_swaps[(df_swaps['Fecha'] >= pd.to_datetime(request.date_ini)) & (df_swaps['Fecha'] <= pd.to_datetime(request.date_end)) & (df_swaps['Swap_Index'] == request.swap_name)]
#     swaps_object = {'Fecha' : [], 'Swap_Index' : [], 'Tenor' : [], 'Valor' : []}
#     for index,row in data_swaps.iterrows():
#         swaps_object['Fecha'].append(dt.date.strftime(row['Fecha'],'%Y-%m-%d'))
#         swaps_object['Swap_Index'].append(row['Swap_Index'])
#         swaps_object['Tenor'].append(row['Tenor'])
#         swaps_object['Valor'].append(row['Valor'])
#     # return list(map(schemas.SwapResponse.from_orm,swaps_object))
#     return [swaps_object]


async def get_imacec_date(year:str) -> List[schemas.ImacecResponse]:

    imacec = dbase['imacec']
    data = imacec.find({'Año':year},{"_id":0})
    output_list = []
    for x in data:
        output_list.append(x)
    
    return output_list
