from pydantic import BaseModel

class Solicitudes(BaseModel):
    idsolicitudes: int
    descripcion: str
    disponible: str
    estado: str
    fecha: str
    hora: str