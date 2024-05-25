from fastapi import APIRouter, HTTPException
from controllers.historial_controller import *
from models.historial_model import Historial

router = APIRouter()

new_historial = HistorialController()


@router.get("/get_historiales/")
async def get_historiales():
    rpta = new_historial.get_historiales()
    return rpta

@router.get("/get_historial/{historial_id}",response_model=Historial)
async def get_historial(historial_id: int):
    rpta = new_historial.get_historial(historial_id)
    return rpta


@router.post("/create_historial")
async def create_historial(historial: Historial):
    rpta = new_historial.create_historial(historial)
    return rpta


@router.put("/update_historial/{idhistorial}")
async def update_historial(idhistorial: int):
    rpta = new_historial.update_historial(idhistorial)
    return rpta


@router.delete("/delete_historial/{idhistorial}")
async def delete_historial(idhistorial: int):
    rpta = new_historial.delete_historial(idhistorial)
    return rpta


