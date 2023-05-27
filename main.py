from data.apartamentos import apartamento1,apartamento2
from helpers.crearTablasHTML import crearTabla

import pandas as pd 
# crear dataframe 

tabla1 = pd.DataFrame(apartamento1)
tabla2 = pd.DataFrame(apartamento2)
tabla3 = pd.read_csv("./data/empleados.csv")


# EFECTUANDO FILTROS CON PYTHON 

# 1. Definir condicion logica 

analistasJovenesAnalista1 = tabla3.query("edad<25 and cargo == 'analista1'")
empleadosSalarioBajo = tabla3.query("salario< 5000000 and cargo == 'analista2'")
empleadosADespedir = tabla3.query('edad>50')

# 1. Creamos tabla html con el dataframe del analistasJovenesAnalista1  

crearTabla(analistasJovenesAnalista1, "tabla")
crearTabla(empleadosSalarioBajo, "tablaempleadosSalarioBajo")
crearTabla(empleadosADespedir, "tablaempleadosADespedir")

print(analistasJovenesAnalista1)
print(empleadosSalarioBajo)
print(empleadosADespedir)


# print(tabla2)
# print(tabla3)

# estadisticasApto1       = tabla1.describe()
# estadisticasApto2       = tabla2.describe()
# estadisticasEmpleados   = tabla3.describe()


# print(estadisticasApto1)
# print(estadisticasApto2)
# print(estadisticasEmpleados)