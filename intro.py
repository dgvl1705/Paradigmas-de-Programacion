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
lista = [1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12]

matriz = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]

print(lista)
print(matriz)

#==================================================================
# Identación estricta para procesos dependientes de : (dos puntos)
#==================================================================
if 10>5:
    print("diez es mayor que cinco")
    print("otraidentación")
for i in lista:
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


#================================================
# Conjunto en  python
#================================================
even_nums = {2, 4, 6, 8, 10} #Conjunto  de números pares
print(even_nums)

# El bool no es parte del conjunto
emp = {1, 'Steve', 10.5, True} # Conjunto de diferentes objetos
print(emp)

nums = {1, 2, 2, 3, 4, 4, 5, 5}
print(nums)

#======================================================
# Convertir secuencia a conjunto 
# No lo genera en orden
#======================================================
s = set('Hello')
print(s)
s = set((1, 2, 3, 4, 5)) # Tupla a conjunto
print(s)

#=====================================================
# De diccionario a conjunto: conjunto de llaves
#=====================================================
d = {1: 'One', 2: 'Two'}
s = set(d)
print(s)

s.add(100)
print(s)

s.update(nums)
print(s)

s.remove(100)
print(s)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

su = s1|s2 # Unión
print(su)

si = s1&s2 # Intersección
print(si)

sr =  s1 - s2 #Diferencia de conjuntos
print(sr)

sp = s2 - s1
print(sp)

ss = s1^s2 #Diferencia simétrica
print(ss)


#==========================================================
# Uso de diccionarios
#==========================================================
capitals = {"USA":"Washington D.C.", "France": "Paris", "India":"New Delhi"}
print(capitals)


#===========================================================
# llave: valor
#===========================================================
# diccionario vacío
d = {}

# Llave entera, valor string
numNames = {1: "One", 2: "Two", 3: "Three"}

# Llave real, valor string
decNames = {1.5: "One and Half", 2.5: "Two and Half", 3.5: "Three and Half"}

# Llave tupla, valor string
items = {("Parker", "Reynolds", "Camlin" ): "pen", ("LG", "Whirlpool", "Samsung"): "Refrigerator"}

# Llave string, valor int
romanNums = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5}
print(romanNums)
print(romanNums["I"])

print(capitals.get("India"))
print(capitals.get("india"))

# Reportar llave y valor
for k in capitals:
    print("Key = " + k + ", Value = " + capitals[k])

#Nuevo dato para el diccionario
capitals["Mexico"] = "CDMX"
print(capitals)

# Borrar dato del diccionario
del capitals["Mexico"]
print(capitals)

# Borrar todo el diccionario
del capitals
 
# Reportar llaves
print(romanNums.keys())

# Reportar valores
print(romanNums.values())

# Juicio de llave (está o no está la llave en el diccionario)
print("I" in romanNums)
print("X" in romanNums)
print("XX" in romanNums)



#=========================================================
# Listas
# Las listas pueden ser de objetos diferentes
#=========================================================
miprimeralista = [] # Lsita vacía
print(miprimeralista)

#========================================================
# Llenado de lista
#========================================================
miprimeralista = [1, "Javier", 1.34, "Bosco", "Angel", "Abigail", True]
print(miprimeralista)

#========================================================
# list: hacer una lista
# range(i,j): secuencia de i hasta j-1
#========================================================
nums = list(range(1,61))

for i in nums:
    print(i)
    
#=======================================================
# Incluir nuevos elementos en la lista
#=======================================================
nums.append(61)
nums.append(62)
nums.append(61)
print(nums)

#======================================================
# Quitar elementos de la lista
#======================================================
i = 61
del nums[i]
print(nums)

#=====================================================
# Borrar la lista
#=====================================================
del nums

#=====================================================
# Sumar listas
#=====================================================
L1 = [1, 2, 3]
L2 = [4, 5, 6]
print(L1 + L2)

#====================================================
# Llenado a mano
#====================================================
potencial = []
for i in range(0, 10000):
    potencial.append(float(i))
print(potencial[100])

#===================================================
# Generar una tupla con la lista
#===================================================
potencial = tuple(potencial)
print(potencial[100])

#==================================================
# Condicionales
#==================================================
precio = 50
#-------------------
# Si esto...
#-------------------
if precio < 50:
    print("El precio es menor que 50")
#---------------------------
# Si no... si esto otro...
#---------------------------
elif precio > 50:
    print("El precio es mayor a 50")
#-------------------------------------
# Si nada de lo anterior
#-------------------------------------
else:
    print("El precio es 50")

precio = 50
cantidad = 5
total =  precio*cantidad
#==================================
# Condicionales anidados
#==================================
if total > 100:
    if total > 500:
        print("Total es mayor que 500")
    else:
        if total < 500  and  total > 400:
            print("Total es mayor que 500 pero menor que 400")
        elif total < 500  and total > 300:
            print("Total entre 300 y 500")
        else:
            print("Total entre 100 y 300")

#----------------------------------------
# Condicional de igualdad son ==
#----------------------------------------
elif total == 100:
    print("Total  es 100")
else:
    print("Total menor que 100")

#==============================================
# Contador mientras la condición es verdadera
#==============================================
num = 0
while num < 5:
    num = num + 1
    print('num = ', num)

num = 0
while num < 5:
    num += 1                        # um += 1 es lo mismo  que num = num + 1
    print('num = ', num)
    if num == 3:                    # condición  antes de  salir del bucle       
        break

num = 0
while num < 5:
    num += 1
    if num > 3:
        continue                    # evitar lo que sigue,  continuar con las iteraciones
    print('num = ', num)

#====================================
# Bucle sobre lista
#====================================
nums = [10, 20, 30, 40 ,50]
for i in nums:
    print(i)


#====================================
# Bucle sobre un string
#====================================
for char in 'Hello':
    print(char)


#====================================
# Bucle sobre un diccionario
# items = elementos
#====================================
numNames = {1: 'One', 2: 'Two', 3: 'Three'}
for pair in numNames.items():
    print(pair)

#=====================================
# Bucle sobre diccionario
# key = llave
# value = valor
#=====================================
for k,v in numNames.items():
    print("key = ", k, ", value = ", v)


#====================================
# Primera función
#====================================

def saludo():
    #====================================
    # Documentación rápida de la función
    #====================================
    """ Esta función saluda """
    print('¡Quiúboles!, ¿Cómo estás?')

#====================================
# Llamado de la función
#====================================
saludo()

#===================================
# Se ejecuta pero no se asigna
#===================================
salida = saludo()


#====================================
# Esto no funciona
#====================================
print(salida)

#====================================
# Mostrar documentación
#====================================
#help(saludo)

#==================================
# Función con argumento
#==================================
def salu2(nombre):
    """ Esta función te saluda por tu nombre """
    print("¡Que onda ese", nombre, "!")
salu2("Julián")
salu2("Ángel")

#===========================================
# Ahorrar trabajo del intérprete
# nombre:str la variable nombre es un str
#===========================================

def saludos(nombre:str):
    """ Esta función te saluda por tu nombre estrictamente """
    print("¡Qué onda ese", nombre, "!")
saludos("Julián")
a = 123
print(type(a))
saludos(a)

#=================================================
# Función con muchos argumentos
#=================================================
def saludos_multiples(nombre1, nombre2, nombre3):
    """ Esta función saluda a 3 personas al mismo tiempo """
    print("Hola ", nombre1, ", ", nombre2, ", ", nombre3)
saludos_multiples("Hugo", "Paco", "Luis")

#===================================================
# Función con cualquier número de argumento
#===================================================
def muchos_saludos(*nombres):
    """ Esta función saluda a todos los que quieras """
    i = 0
    #==========================================
    # end= es para ponerlo corrido
    #==========================================
    print("Hola ", end="")
    while len(nombres) > i:
        # Último nombre
        if (i == len(nombres)-1):
            print(nombres[i])
        else:
            # Cualquier otro nombre
            print(nombres[i], end=", ")
        i+=1

muchos_saludos("Bosco", "Angel", "David", "Tamara", "Mill", "Edwin", "Lev", "Luis", "Abigail")

def greet(firstname, lastname):
    print("Hello ", firstname, lastname)

#================================================
# Llamar la función con argumentos en desorden
#================================================
greet(lastname='Jobs', firstname='Steve') # Se pueden especificar las variables en desorden

#===================================================
# Función con argumentos en desorden
#===================================================
def greet(**person):
    #====================================================
    # persona tiene características firstname y lastname
    #====================================================
    print('Hello ', person['firstname'], person['lastname'])

greet(firstname='Steve', lastname='Jobs')
greet(lastname='Jobs', firstname='Steve')
greet(firstname='Bill', lastname='Gates', age=55) # Se pueden pasar más parámetros de los necesarios

#===========================================
# Función con valores por defecto
#===========================================
def greet(name = 'Guest'):
    print('Hello ', name)

greet() # Utiliza el valor dado de antemano
greet('Steve')

#=======================================
# Función con resultado
#=======================================
def suma(a, b):
    return a + b

#======================================
# Programación funcional
# Se pueden funciones en funciones
#======================================
total = suma(5, suma(10, 20))
print(total)

#==================================================
# Cálculo lambda
# nombre de la función = lambda variable: función
#==================================================
x_al_cuadrado = lambda x: x * x
al = x_al_cuadrado(5)
print(al)

#==================================================
# Lambda de varias variables
#==================================================
suma = lambda x1, x2, x3: x1 + x2 + x3
print(suma(99, 98, 97))

sumas = lambda *x: x[0] + x[1] + x[2] + x[3]

print(sumas(100, 200, 300, 400))

#==================================================
# Uso de una función anónima
# El argumento  va afuera  entre paréntesis
#==================================================
print((lambda x: x*x)(6)) # Función anónima

#====================================================
# Función con variable global
# EVITE EL EXCESO !!!
#====================================================
name = 'Steve'
def greet():
    global name # Para utilizar una variable global (que viene fuera del bloque)
    name = 'Bill'
    print('Hello ', name)

greet()


#==========================================
# Algoritmo 1
#==========================================
# Serie exponencial
# Factorización de x
# Negativos con función inversa
#==========================================
n = 200
x = -100.0
flag = False 
if x < 0:
    flag = True
    x = -x
s = 1.0
for i in range(n, 0, -1):
    s *= x/float(i)
    s += 1.0
if flag == True:
    s = 1/s
print(s)


#===============================================
# PROGRAMACIÓN ORIENTADA A OBJETOS
#===============================================

#============================================
# Una clase para un objeto vacío
# No esta tan vacío, necesita
# la palabra pass = pasar
#============================================
class ObjetoVacio:
    pass

#=================================
# nada es un ObjetoVacio
#=================================
nada = ObjetoVacio()
print(type(nada))

#=========================================
# La clase llanta
#=========================================
class Llanta:
    #=====================================
    # Variable cuenta es de toda la clase
    #=====================================
    cuenta = 0
    #=============================================
    # Función constructora de identidad
    # __init__ es una función reservada
    # comienza con uno mismo: self
    # pero puede ser otro nombre (mi)
    # parámetros de entrada = default
    #=============================================
    def __init__(mi, radio=50, ancho=30, presion=1.5):
        # Variable de la estructura completa de la Llanta
        Llanta.cuenta += 1
        # Variables exclusivas de cada objeto
        mi.radio = radio
        mi.ancho = ancho
        mi.presion = presion

#==============================================
# Objetos (instanciados)
#==============================================
llanta1 = Llanta(50, 30, 1.5)
llanta2 = Llanta(presion = 1.2)
llanta3 = Llanta()
llanta4 = Llanta(40, 30, 1.6)

#========================================
# Objeto que contiene otros objetos
#========================================
class Coche:
    def __init__(mi, ll1, ll2, ll3, ll4):
        mi.llanta1 = ll1
        mi.llanta2 = ll2
        mi.llanta3 = ll3
        mi.llanta4 = ll4

micoche = Coche(llanta1, llanta2, llanta3, llanta4)

print("Total de llantas: ", Llanta.cuenta) # Variable global de la clase
print("Presión de la llanta 4 = ", llanta4.presion) # Presión de la llanta 4
print("Radio de la llanta 4 = ", llanta4.radio)
print("Radio de la llanta 3 = ", llanta3.radio)
print("Presión de la llanta 1 de mi coche = ", micoche.llanta1.presion)

#==================================
# Encapsulamiento
#==================================


#==================================================================================
# Uso de la función de python property para poner y obtener atributos
#==================================================================================
class Estudiante:
    def __init__(mi):
        mi.__nombre = ''
    def ponerme_nombre(mi, nombre):
        print('se llamó a ponerme_nombre')
        mi.__nombre = nombre
    def obtener_nombre(mi):
        print('se llamó a obtener nombre')
        return mi.__nombre
    nombre = property(obtener_nombre, ponerme_nombre)

#==========================================
# Crear objeto estudiante sin nombre
#==========================================
estudiante = Estudiante()


#========================================================================
# Ponerle nombre usando la propiedad nombre y el método ponerme_nombre
# (sin tener que llamar explícitamentela función)
#========================================================================
estudiante.nombre = "Diego"

#=======================================================================
# Obtener el nombre con el método obtener_nombre
# __nombre es una variable encapsulada (no visible desde fuera)
# (sin tener que llamar explícitamente a la función obtener_nombre)
#=======================================================================
print(estudiante.nombre)

# Esto no funciona
#print(estudiante.__nombre)

#=======================================
# herencia de clases
#======================================= 
class Cuadrilatero:
    def __init__(mi, a, b, c, d):
        mi.lado1 = a
        mi.lado2 = b
        mi.lado3 = c
        mi.lado4 = d
    
    def perimetro(mi):
        p=mi.lado1 + mi.lado2 + mi.lado3 + mi.lado4
        print("perimetro = ", p)
        return p

#================================================
# Su hijo rectángulo
# Rectángulo es hijo de Cuadrilátero
# Rectángulo(Cuadrilátero)
#================================================
class Rectangulo(Cuadrilatero):
    def __init__(self, a, b):
        #==========================
        # Constructor de su madre
        #==========================
        super().__init__(a, b, a, b)

#================================================
# Su nieto Cuadrado
# Hijo de Rectángulo
#================================================
class Cuadrado(Rectangulo):
    def __init__(self, a):
        super().__init__(a,a)
    def area(self):
        area = self.lado1**2 
        return area
    #def perimetro(self):
    #   p = 4.0*self.lado1
    #   print("perimetro = ", p)
    #   return p

#==============================================
# Crear un cuadrado
#==============================================
cuadrado1 = Cuadrado(5)

#========================================================
# Llamar al método perímetro de su abuelo Cuadrilátero
#========================================================
perimetro1 = cuadrado1.perimetro()

#====================================
# Llamar a su propio método área
#====================================
area1 = cuadrado1.area()

print("Perímetro = ", perimetro1)
print("Área = ", area1)

#==================================================================
# Sobre-escribir un método  de su madre o abuela o tatarabuela...
# Es volver  a definir  una función ya existente
#==================================================================

