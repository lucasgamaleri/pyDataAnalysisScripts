import pandas as pd
print("\nGESTION DE HISTORICOS DE COMANDOS DEL PISO DE PLANTA DECAPADO - EDA (Lucas GAMALERI [TERNIUM ARGENTINA SA])\n")
path = 'C:/Users/Lucas GAMALERI/Desktop/Cizalla 3/commands/commands_historicals_24_04_2020.csv'

print("Cargando Base de Datos...")
df = pd.read_csv(path)
print("OK")
print("Formateando datos de fecha...")
df['TIEMPO ENVÍO'] = pd.to_datetime(df['TIEMPO ENVÍO'])
print("OK")
print("Reordenando tabla por fecha...")
df.sort_values(by=['TIEMPO ENVÍO'], inplace= True, ascending=True)  #CORREGIR!!! REALMENTE NO ORDENA DE FORMA ASCENDENTE. SE NECESITA QUE EL PRIMER INDEX CORRESPONDA A LA FECHA MAS ANTIGUA
df['TIEMPO ENVÍO'].sort_index()
print("OK\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ BIENVENIDO ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Escriba ayuda() para ver una lista de los comandos disponibles\n")
def ayuda():
    print("\ncodigos() : Obtiene una lista con cada [CODIGO] DESCRIPCIÓN presente en la tabla")
    print("exit() : Salir del programa y volver a CMD")

def codigos():
    print("CÓDIGOS PRESENTES EN BBDD\n")
    codigo = df['[CODIGO] DESCRIPCIÓN'].unique()
    print(codigo) #Obtiene una lista con cada codigo (sin repetir) presente en la tabla


#def tiempos():




# df[df['[CODIGO] DESCRIPCIÓN'].isin(['[1549] SET VEL BRIDA 3 MEDIA'])]['[CODIGO] DESCRIPCIÓN'] #Extrae de '[CODIGO] DESCRIPCIÓN' una lista de valores que cumplen con parámetro "isin"
