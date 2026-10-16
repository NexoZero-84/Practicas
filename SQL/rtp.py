import pandas as pd
import sqlite3

df = pd.read_csv('SQL\\datos_rtp.csv')
print(df.head())
print('\n', df.columns.tolist())

conexion = sqlite3.connect('cdmx_transporte.db')
df.to_sql('afluencia_rtp', conexion, if_exists='replace', index=False)
conexion.close()

print("\n¡Listo! Base de datos 'cdmx_transporte.db' creada con la tabla 'afluencia_rtp'.")