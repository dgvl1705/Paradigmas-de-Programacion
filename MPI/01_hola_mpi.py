from mpi4py import MPI

#=================================
# Crear un objeto comunicador
#=================================
comunicadores = MPI.COMM_WORLD

#==================================
# Número total de procesos
#==================================
n_procesos = comunicadores.Get_size()

#==========================================
# Número identificador de este proceso
#==========================================
quien_soy = comunicadores.Get_rank()

print("Saludos desde el proceso ", str(quien_soy), " de ", str(n_procesos))

