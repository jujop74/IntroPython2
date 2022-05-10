import pandas as pd

# leer_fichero=pd.read_csv(r'directorio_pandas/catalogo_cf.csv', encoding='ISO-8859-1')
# leer_fichero.to_excel(r'directorio_pandas/catalogo_cf.xlsx', index=None, header=True)

# Se crea el dataframe con Pandas de un fichero Excel
dataframe_excel=pd.read_excel('directorio_csv/catalogo_cf.xlsx')
print(dataframe_excel)

# Selecciona todas las filas y la primera y la cuarta columna
print(dataframe_excel.iloc[:, [0, 3]])

# Se exporta a Excel
dataframe_excel.iloc[:, [0, 3]].to_excel('directorio_csv/catalogo_cf_resumen.xlsx', index=False)
