#Esto es un comentario de una sola linea
"""Esto es un comentario de 
varias lineas"""

#Inicializando variables
Nombre= "Mariel Sofia Lopez Estor"
edad=13
estado=False
nota=5.0

#Mostrar el contenido de las variables print()
print(Nombre)
print(edad)
print(estado)
print(nota)

#Que tipo de dato contiene cada variable.
print(type(Nombre))
print(type(edad))
print(type(estado))
print(type(nota))

#Vamos a utilizar la funcion input para recoger datos por medio del teclado.
nombre=input("¿Como te llamas? ")
edad=input("¿Que edad tienes? ")
estado=input("¿En que estado te encuentras? ")
nota=input("¿Cual es tu nota? ")

#Para visualizar que guardamos en las variables anteriores
print("Hola,",Nombre,"Un gusto conocerte")
print("tu edad es:",edad)
print("Tu estado es:",estado)
print("Tu nota es:",nota)