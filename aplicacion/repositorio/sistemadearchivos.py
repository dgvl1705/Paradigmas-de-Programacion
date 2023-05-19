from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario

#================================================
# Implementa la interface RepositorioDeUsuarios
#================================================
class SistemaDeArchivos(RepositorioDeUsuarios):
    __directorio: str

    def __init__(self, directorio:str):
        self.__directorio = directorio

    def abrir(self) -> None:
        print(f"Abrir directorio: {self.__directorio}")

    def guardar(self, usuario:Usuario) -> None:
        xml = f"</root></name>{usuario.getNombre()}</name></lastName>{usuario.getApellido()}</lastName></age>{usuario.getEdad()}</age></root>"
        print(f"Guardando usuario en el archivo :{self.__directorio}/{usuario.getNombre()}")
        print(xml)

    def cerrar(self) -> None:
        print("Cerrando el archivo")
        
        
