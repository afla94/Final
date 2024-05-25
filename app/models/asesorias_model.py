from pydantic import BaseModel

class Asesorias(BaseModel):
   idasesorias: int
   idusuarios: int
   idsolicitudes: int
   descripcion: str
   categoria: str
   duracion: str
   estado: str
   fecha: str
   hora: str