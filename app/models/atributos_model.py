from pydantic import BaseModel

class Atributos(BaseModel):
    idatributos: int
    nombre: str
    descripcion: str
    estado: str
    fecha: str
    hora: str