# codigo sobre el analisis de la venta de motos del taller 1
# Importancion de librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

df.boxplot(column='Selling_Price', by='classified_status')

# Adjust the size of the image
plt.figure(figsize=(8, 6))

# Set a logarithmic scale on the y-axis
plt.yscale('log')

plt.title('Boxplot of Selling price by owner status')
plt.suptitle('')  # Remove default subplot title
plt.xlabel('Owner Status')
plt.ylabel('Selling Price')
plt.show()

# Observar la estadistica descriptiva de los datos observados
df.describe()
# Observar los diferentes tipos de marcas en la base de datos
df['Brand'].unique()