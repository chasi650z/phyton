#Crear un programa que le solicite al usuarioa  generar un texto cualquiera y tambien 3 letras de su eleción 
#Para generar lo siguiente 
# Cuantas veces aparece cada una de las letras en el texto
#Cuantas palabras hay en todo el texto
#Cual es la primera y ultima letra del texto
# Nos va a mostrar el texto en orden inverso 
# aparece phyton dentro del texto ?

#Declaración de variables
Texto= input(
    "Ingrese un texto: "
)
Letras=[]

Letras.append(input("Ingrese la primera letra: ").lower())
Letras.append(input("Ingrese la segunda letra: ").lower())
Letras.append(input("Ingrese la tercera letra: ").lower())


Texto=Texto.lower()

#Apartado de retos 
print("\n")
CP = Texto.split()
print(f"Cuantas palabras existen: {len(CP)}")

#Cantidad de veces que se repiten las letras
print("\n")
print("Cantidad de letras")
CL1 = Texto.count(Letras[0])
CL2 = Texto.count(Letras[1])
CL3 = Texto.count(Letras[2])

print(f"Hemos encontrado la letra '{Letras[0]}', repetida {CL1} veces")
print(f"Hemos encontrado la letra '{Letras[1]}', repetida {CL2} veces")
print(f"Hemos encontrado la letra '{Letras[2]}', repetida {CL3} veces")

#Exite la palabra phyton en el texto ?
print("\n")
phyton = "phyton" in Texto
print(f"La palabra 'Phyton' esta en el texto: {phyton}")

#Letras de inicio y de fin 
print("\n")
letra_init = Texto[0]
letra_fin = Texto[-1]
print(f"la letra inicial es {letra_init} y la letra final es {letra_fin}")

#Texto invertido
print("\n")
CP.reverse()
texto_invertido = ' '.join(CP)
print(f"Tu texto invertido es: {texto_invertido}")

