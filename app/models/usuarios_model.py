from pydantic import BaseModel

class Usuarios(BaseModel):
    idusuarios: int
    idtipo_usuarios: int
    nombre: str
    direccion: str
    telefono: str
    email: str
    contraseña: str
    estado: str
    fecha: str
    hora: str