
def ListaOjetos(Objetos):
    print(Objetos)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sintaxis.py
#  
#  Copyright 2020 <<Pyro>> <https://pythones.net>
  
#Declaración de variables
a = "Python" #Instrucción simple
b = "Aprender" #Instrucción simple
c = "Fácil" #Instrucción simple
d = "Sintaxis" #Instrucción simple
e = True #Instrucción simple
#Bloque de código a continuación
if e == True: #Instrucción compuesta
    print(b + " " + a + " es " + c + " "+ "si comprendo su " + d)
    print ("Se acaba de ejecutar una instrucción compuesta..")
    #Sub-nivel Inst.Simple dentro de un bloque
#Instrucciones simples nuevamente
print ("Pero ahora estamos ejecutando instrucciones simples..")
print ("Simplemente una tras otra.")

Diccionario1 = {
    'Nombre':'Fabian',
    'Edad': 59,
    'Genero':'M'
}

propiedad = 'Nombre'
print(Diccionario1)
print(Diccionario1[propiedad])

print(Diccionario1[propiedad][0:3])

nombre = Diccionario1.get('Nombre')
print(nombre)
nombre = Diccionario1['Nombre'] = 'Coco'
print(nombre)

Cosas = ("casa", "puerta", "reloj", "mesa", "silla", "banco", "cuadro", "alfombra")

print(Cosas)

Objetos = ["casa", "puerta", "reloj", "mesa", "silla", "banco", "cuadro", "alfombra"]

print(Objetos)

Objetos[1] = 'porton'
print(Objetos)

ListaOjetos(Objetos)