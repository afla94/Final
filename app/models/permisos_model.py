from pydantic import BaseModel

class Permisos(BaseModel):
    idpermisos: int
    descripcion: str
    estado: str
    fecha: str
    hora: str