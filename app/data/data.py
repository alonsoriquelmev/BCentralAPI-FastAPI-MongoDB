import pandas as pd
import variables as var

def add_dot(numberString):
    str_aux = numberString.replace(numberString[-1],'.'+numberString[-1])
    return str_aux

def swaps_from_bc(year:str) -> pd.DataFrame:
    url = f'https://si3.bcentral.cl/Siete/ES/Siete/Cuadro/CAP_TASA_INTERES/MN_TASA_INTERES_09/TI__TPM4/T31b?cbFechaDiaria={year}&cbFrecuencia=BUSINESS&cbCalculo=NONE&cbFechaBase='
    data = pd.read_html(url)
    data = data[0]
    data.drop(columns=['Sel.'], inplace=True)
    data = data.T
    data.reset_index(inplace = True)
    headers = data.iloc[0]
    df_scp = pd.DataFrame(data.values[1:], columns = headers)
    for key, value in var.months.items():

        df_scp['Serie'] = df_scp['Serie'].str.replace(key,value)
    df_scp['Serie'] = pd.to_datetime(df_scp['Serie'])
    df_scp = df_scp.sort_values('Serie')
    df_scp.rename(columns={'Serie':'Fecha'},inplace=True)
    df_scp = df_scp.melt(id_vars = ['Fecha'], var_name = 'Swap_Index', value_name='Valor')
    df_scp = df_scp.sort_values(by = ['Fecha','Swap_Index'])
    df_scp.reset_index(drop=True, inplace=True)
    df_scp['Swap_Index'] = df_scp['Swap_Index'].str.replace('en pesos','CLP')
    df_scp['Swap_Index'] = df_scp['Swap_Index'].str.replace('en UF','UF')
    df_scp['Tenor'] = df_scp['Swap_Index'].copy().str.replace('SPC CLP ','')
    df_scp['Tenor'] = df_scp['Tenor'].str.replace('SPC UF ','')
    df_scp['Swap_Index'] = df_scp['Swap_Index'].apply(lambda x: x.split(' ')[0]+' '+x.split(' ')[1])
    for key, value in var.swap_tenors.items():
        df_scp['Tenor'] = df_scp['Tenor'].str.replace(key,value)

    df_scp = df_scp[['Fecha','Swap_Index','Tenor','Valor']]
    return df_scp


url = "https://si3.bcentral.cl/Siete/ES/Siete/Cuadro/CAP_PRECIOS/MN_CAP_PRECIOS/PEM_VAR_IPC_NEW/637775848569931668?cbFechaInicio=2000&cbFechaTermino=2022&cbFrecuencia=MONTHLY&cbCalculo=NONE&cbFechaBase="
data = pd.read_html(url)
data = data[0]
data = data.T
data.reset_index(inplace = True)
headers = data.iloc[1]
df_ipc = pd.DataFrame(data.values[2:], columns = headers)

for key, value in var.months.items():

    df_ipc['Serie'] = df_ipc['Serie'].str.replace(key,value)

df_ipc[['Mes','Año']] = df_ipc['Serie'].str.split('.',expand=True)
# df_ipc['IPC General'] = df_ipc['IPC General'].astype(str).apply(lambda x: add_dot(x))
# print(df_ipc[['IPC General','Mes','Año']][df_ipc['IPC General'].astype(str).str.contains('.1.')])
# df_ipc['Serie'] = pd.to_datetime(df_ipc['Serie'])
# df_ipc = df_ipc.sort_values('Serie')
# df_ipc.rename(columns={'Serie':'Fecha'},inplace=True)
# print(df_ipc)
