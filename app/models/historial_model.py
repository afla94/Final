from pydantic import BaseModel

class Historial(BaseModel):
    idhistorial: int
    idasesorias: int
    diagnostico: str
    plan_tratamiento: str
    observaciones: str
    estado: str
    fecha: str
    hora: str