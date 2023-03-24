''' ESTE ES UN SUPERCOMENTARIO
    DE INICIO A NUESTRO RESUMEN
'''
#===========================
#   Operaciones básicas
#===========================
print(2+3)
print(2*3)
print(2/3)
print(2**10)
print(2**0.5)
print(2**0.5)   #raíz cuadrada
print(10%2)
print(10%0.1)   # exclusivo en python

#===========================================
# Para saber el tipo de objeto se usa type
#===========================================
t=0
print(type(t))  # entero
t=3.6
print(type(t))  # real (flotante)
t=True
print(type(t))  # booleano (bool)

#===========================
# Mensajes de pantalla
#===========================
print("Estes es un comando de python. ", "Este es otro enunciado. ", t)
print('id: ', 1)
print('First Name: ', 'Steve')
print('Last Name: ', 'Jobs')
print("vamos a sumar esto" + " con esto otro")

#===============================================
# Continuar una instrucción en varios renglones
#===============================================
if 100 > 99 and \
    200 <= 300 and \
    True != False:
        print('Hello World!')

#================================================
# Comandos diferentes en la misma línea
#================================================
print("Hola "); print("tu!")    # Se considera mala práctica

#================================================
# Usando paréntesis redondos, cuadrados o llaves
# se puede escribir en varios renglones
#================================================
list = [1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12]

matriz = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]

print(list)
print(matriz)

#==================================================================
# Identación estricta para procesos dependientes de : (dos puntos)
#==================================================================
if 10>5:
    print("diez es mayor que cinco")
    print("otraidentación")
for i in list:
    print(i)
    print("ok")
if 10>5:
    print("verdadero")
    if 10<20:
        print("verdadero")
elif 5>3:   # comienza segundo condicional
    print("esto no se imprimirá")
else:
    print("aquí nunca llega")

#===================
# Funciones
#===================
def say_hello(name):
    print("Hello ", name)
    print("Welcome to Python Tutorials")

say_hello("Diego")

#=======================================================
# Input permite obtener datos del usuario en prompter
#=======================================================
nombre=input("Dame tu nombre: ")
print("Hola como estas", nombre)

#=======================================================
# Los enteros son de precisión ilimitada
#=======================================================

y = 5000000000000000000000000000000
print(y)

#============================================================
# Se puede delimitar números con guión bajo pero no con coma
#============================================================
y = 5_000_000
print(y)

#============================================================
# La función int() cambia strings y floats a enteros
#============================================================
numero =  int(input("Dame tu edad: "))
type(numero)

#============================================================
# La notación científica de flotantes utiliza e o E
#============================================================
# 1.2 x 10^{-9}
#=======================
y = 1.2E-09
print(y)

#============================================================
# La función float() convierte strings y enteros a floats
#============================================================
y = float("14.3")
print(y)

#===========================================================
# Los complejos  se escriben con la raíz de menos uno
# j siempre  con un número como prefijo
# no acepta la j suelta
#===========================================================
z = 1+1j

# suma +
# resta -
# multiplicación *
# división /
# módulo %
# esponente **
# función piso //
# Funciones  para transformar números int() float() complex()
# Operaciones abs() round() pow()

print(round(3.14159, 4))

#=======================================
# String de varias líneas
#=======================================

parrafo = """ En el bosque de la china
 la chinita se perdió """
print(parrafo)

#================================================
# La función len() obtiene el tamaño del string
#================================================

n=len(parrafo)
print(n)

#===================================================================
# Las letras de un string ocupan lugares como en un arreglo
# (también de atrás para adelante comenzando en -1 el último)
#===================================================================

palabra = "hola"
print(palabra[0])
print(palabra[-4])
