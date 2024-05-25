from pydantic import BaseModel

class Tipo_usuarios(BaseModel):
    idtipo_usuarios: int
    nombre: str
    descripcion: str
    estado: str
    fecha: str
    hora: str