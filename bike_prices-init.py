# codigo sobre el analisis de la venta de motos del taller 1
# Importancion de librerias
import numpy as np
import pandas as pd

# lectura de datos
df = pd.read_csv('.\\BikePrices.csv')

# Tipos de datos en el dataset
types = df.dtypes.value_counts()

print('Number of Features: %d'%(df.shape[1]))
print('Number of Customers: %d'%(df.shape[0]))
print('Data Types and Frequency in Dataset:')
print(types)

# Transformar la clase "Owner" a una variable binaria
df['classified_status'] = np.where(df['Owner'] == '1st owner', '1st owner', 'No 1st owner')