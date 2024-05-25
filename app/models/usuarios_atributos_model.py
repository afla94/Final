from pydantic import BaseModel

class Usuarios_atributos(BaseModel):
    idusuarios_atributos: int
    idusuarios: int
    idatributos: int
    estado: str
    fecha: str
    hora: str