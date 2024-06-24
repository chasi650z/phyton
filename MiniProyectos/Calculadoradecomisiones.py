# Desafio propuesto 
# Cree una calculadora que ayudara a los empleados a calcular sus comisiones en base a su total de ventas de manera mensual
# La comisión es del 13% de las ventas totales y debe tener solo 2 decimales

nombre = input("Ingrese su nombre: ")
ventas = float((input("Ingrese su total de ventas: ")))

comision = round((ventas*13)/100,2)

print(f"Hola {nombre} tus ventas totales fueron de {ventas} y tu comision seria de {comision}")