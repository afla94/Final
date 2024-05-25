from pydantic import BaseModel

class Tipo_usuarios_permisos(BaseModel):
    idtipo_usuarios_permisos: int
    idtipo_usuarios: int
    idpermisos: int
    estado: str
    fecha: str
    hora: str