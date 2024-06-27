"""""
#Day 1
# con comillas si es texto
print("Hello Word")
# sin comillas cuando son números
print(1234)
# para colocar comillas dentro de un texto se utilizan '' comillas simples 
print("Good Afernoon 'Señor'")
# generar el resultado / sin comillas se ejecuta la operación
print (100+50)

#Cadenas de texto \n salto de linea \t tabular si quiero imprimir una \ debo colocar 2 \\
print("Hello "+"Pablo\n Estamos prácticando")
print("\t Practice")


#Imput

print("Tu nombre es "+ input(" Enter your name: "))
print("Tu Apellido es "+ input("Enter your lastname: "))

print("Tu nombre es "+ input("Enter your name: ")+ " "+ input("Enter your lastname: ")) 

"""
#-------------------------------------------------------------------------------------------------------

#Day 2
#Variables
"""
name="Pablo"
print(name)

name="Juan"
print(name)

edad = 30

print(edad)
#lo que se ingresa por un input es un str no un int o float por eso hay errores se deben hacer convercinoes 

val = input("Ingresa un número: ")
print("tu edad es "+ val) 

print(type(val))

#Conversiones 

# conversión: phyton lo hace de manera automática 
# explicita: quiero convertir un tipo de valor en otro por ejemplo de string a num o viceversa

#Conversión implicita
num1 = 20 
num2 = 30.5
print(type(num1))
print(type(num2))
num1 = num1 + num2
print(type(num1))

#explicita 

num3 = 5.8
print(num3)
print(type(num3))

num3 = int(num3)
print(num3)
print(type(num3))

#Esta conversión no hace redondeo directamente elimina los decimales 

val = input("Ingresa un número: ")
val = int(val)
print(type(val))
print(val+1)

#Formatos 

x = 10 
y = 5

print("Mis numeros son {} y {}".format(x,y))

print("La suma de {} y {} es {}".format(x,y,y+x))

color = "rojo"
matricula = 256
print(f"El auto es {color} y su matricula es {matricula}")

#Operadores 

x = 6
y = 2
z = 7

print(f"{x} mas {y} es igual a {x+y}")
print(f"{x} mas {y} es igual a {x-y}")
print(f"{x} mas {y} es igual a {x/y}")
print(f"{x} mas {y} es igual a {x*y}")


#división al piso, si es decimal va a eliminar el decimal colocando solo el entero, no redondea

print(f"{z} divido al piso de {y} es igual a {z//y}")

#Modulo solo obtiene el residuo de la división

print(f"{z} modulo de {y} es igual {z%y}")

#potencia de un número 

print(f"{x} elevado a la {y} es igual a {x**y}")

#raíz cuadrada

print(f"La raiz cuadrada de {x} es {x**0.5}")

#redondeo 

print(round(90/7,1))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#Index en phyton
# Acepta 3 parametros uno lo que busco, el segundo desde que posición lo quiero buscar y el ultimo hasta que posición lo quiero buscar 

text = "this is a test"


resultado = text[0]

print(resultado)

resultado = text.index("test")
print(resultado)
# rindex busca desde la ultima posición

resultado = text.rindex("this")

#Slicing extraigo todos los caracteres comprendidos entre 2 posiciones no incluye la posición final

# Si añado un tercer parametro es cada cuanto salto es decir si coloco 2 salta de 2 en 2 y toma el caracter
# Si coloco menos -1 en el ultimo caracter va desde atras 
fragmento = text[2:5]
print(fragmento)


 # Metodo upper para colocar todo en mayusculas 
 # Metodo lower para minusculas
 # split separa en partes /lista
 # join unir items usando separadores
 # find encontrar un sub-string
 # replace remplaza una palabra o substring para dos argumentos el primero es el texto a remplazar, el segundo con lo que quiero remplazar

texto = "Este es un texto de prueba"
resultado = texto

print(texto.upper())
print(texto.lower())

print(texto.split()) # los separa en palabras no caracteres, si coloco algo como argumento se usara como separador

#Listas se puede tener una lista hecha de listas y de casi cualquier cosa

mi_lista = ['a','b','c']
resultado = len(mi_lista)
resultado2 = mi_lista[0]


mi_lista[0] = "alfa"

mi_lista.append('g')
mi_lista.pop() # si no coloco parametros dentor de pop elimina el ultimo elemento

print(resultado)
print(type(mi_lista))

mi_lista.sort() # ordena alfabeticamente
mi_lista.reverse() # ordena alfabeticamente pero al reves



# Dicionarios no tienen un orden o indice, estos tienen claves y valores 

diccionario = {'c1':'valor 1', 'c2':'valor2', 'c3':'valor 3'}

resultado = diccionario['c2'] # obtengo el valor o valores asociados a la clave c2

# puede haber dicionario dentro de dicionarios , Parece 


#tuples son inmutables no se pueden cambiar

t = (1,2,3)

# set, solo admiten elementos únicos es importante esto
# no se puede incluir ni listas ni diccionarios dentro de ellos 

mi_set = set([1,2,3,4,5])

print(type(mi_set))
print(mi_set)



#boolean 

var1 = True
var2 = False
numero = 5 > 2+3



# operadores lógicos como mayor igual etc 
# y operadores como and u or 
# No hubo nada nuevo la vdd 


# Los if van SIEMPRE con dos puntos al final de la sentencia 
# Para un else if se escribre 
# elif

X   = True

if X:
    print("es correcto")
elif X:
    print("es correcto")
else:
    print("es correcto")

"""

#For 

lista =['a','b','c']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"letra {numero_letra}: {letra}")

# los whiles son literalmente igual 
# el range tiene 3 parametros primero desde donde, segundo hasta donde, y tercero y no obligatorio cuantos se salta en los elementos
for numero in range(20,31):
    print (numero)
    
# Creo una lista que va desde el 1 al 100, Nota no toma el ultimo valor 
lista = list(range(1,101))
