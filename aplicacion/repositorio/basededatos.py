from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario

#====================================================
# Para llenar la interface hay que heredar la clase
#====================================================
class BaseDeDatos(RepositorioDeUsuarios):
    __host: str
    __user: str
    __password: str

    def __init__(self, host:str, user:str, password:str):
        self.__host = host
        self.__user = user
        self.__password = password

    def abrir(self) -> None:
        print(f"Abriendo la conexión de la base de datos: {self.__host}:{self.__user}@{self.__password}")

    def guardar(self, usuario:Usuario) -> None:
        userElements = { "nombre": usuario.getNombre(),
                "apellido": usuario.getApellido(),
                "edad": usuario.getEdad() }
        print(f"Guardando el usuario en la base de datos {usuario.getNombre()}\n")
        print(f"INSERTAR DATOS DEL USUARIO ('{userElements['nombre']}', '{userElements['apellido']}', {userElements['edad']})")
        
    def cerrar(self) -> None:
        print("Cerrando la conexión")
