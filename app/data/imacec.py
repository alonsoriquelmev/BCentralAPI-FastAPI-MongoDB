import pandas as pd
import sys

sys.path.insert(1,"C:/Users/alons/Python Projects/BancoCentral/")
import app.variables as var

url = 'https://si3.bcentral.cl/Siete/ES/Siete/Cuadro/CAP_CCNN/MN_CCNN76/CCNN2018_IMACEC_01/637801073970808685?cbFechaInicio=2012&cbFechaTermino=2022&cbFrecuencia=MONTHLY&cbCalculo=NONE&cbFechaBase='
data = pd.read_html(url)
data = data[0]

data.drop(columns=['Sel.'], inplace=True)
data = data.T
data.reset_index(inplace = True)
headers = data.iloc[0]
df = pd.DataFrame(data.values[1:], columns = headers)


for key, value in var.months.items():
    df['Serie'] = df['Serie'].str.replace(key,value)

df[['Mes','Año']] = df['Serie'].str.split('.',expand=True)
df[['Imacec', 'Producción de bienes', 'Minería', 'Industria',
       'Resto de bienes', 'Comercio', 'Servicios',
       'Imacec a costo de factores', 'Imacec no minero']] = df[['Imacec', 'Producción de bienes', 'Minería', 'Industria',
       'Resto de bienes', 'Comercio', 'Servicios',
       'Imacec a costo de factores', 'Imacec no minero']]*0.1


df.rename(columns={'Imacec':'IMACEC','Producción de bienes':'PROD','Minería':'MIN','Industria':'IND','Resto de bienes':'RESTG',
'Comercio':'COM','Servicios':'SERV','Imacec a costo de factores':'IMACEC-CF','Imacec no minero':'IMACEC-NM'},inplace=True)
df.drop(columns=['Serie'],inplace=True)

json_output = []
for index,row in df.iterrows():
    json_output.append(row.to_dict())
print(json_output)
print(df.info())




 