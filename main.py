from aplicacion.banco.cliente_bancario import ClienteBancario

#====================================================
# try: intenta (correr las instrucciones)
# except: atrapa el error en una variable e
# e se puede convertir a string
#====================================================

#====================================================
# Error por sacar más dinero del que tiene
#====================================================
try:
    cliente = ClienteBancario("Jaime Andrade", "Hernández Sánchez", 28, 0.0)
    cliente.guardarDinero(300)
    print(cliente.imprimirInfo())
    cliente.retirarDinero(400)
    print(cliente.imprimirInfo())
#===================================================
# Exception es la forma más general de error
#===================================================
except Exception as e:
    print("Error: " + str(e))

#===================================================
# Error por usar un atributo privado
#===================================================
try:
    print(cliente.__nombres)
except Exception as e:
    print("Error: " + str(e))

#===================================
# Forma correcta
#===================================
print(cliente.getNombre())
