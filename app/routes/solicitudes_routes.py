from fastapi import APIRouter, HTTPException
from controllers.solicitudes_controller import *
from models.solicitudes_model import Solicitudes

router = APIRouter()

new_solicitud = SolicitudesController()


@router.get("/get_solicitudes/")
async def get_solicitudes():
    rpta = new_solicitud.get_solicitudes()
    return rpta


@router.get("/get_solicitud/{solicitud_id}",response_model=Solicitudes)
async def get_solicitud(solicitud_id: int):
    rpta = new_solicitud.get_solicitud(solicitud_id)
    return rpta


@router.post("/create_solicitud")
async def create_solicitud(solicitud: Solicitudes):
    rpta = new_solicitud.create_solicitud(solicitud)
    return rpta

@router.put("/update_solicitud/{idsolicitudes}")
async def update_solicitud(idsolicitudes: int):
    rpta = new_solicitud.update_solicitud(idsolicitudes)
    return rpta

@router.delete("/delete_solicitud/{idsolicitud}")
async def delete_solicitud(idsolicitud: int):
    rpta = new_solicitud.delete_solicitud(idsolicitud)
    return rpta



