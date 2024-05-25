from fastapi import APIRouter, HTTPException
from controllers.asesorias_controller import *
from models.asesorias_model import Asesorias

router = APIRouter()

new_asesoria = AsesoriasController()


@router.get("/get_asesorias/")
async def get_asesorias():
    rpta = new_asesoria.get_asesorias()
    return rpta


@router.get("/get_asesoria/{asesoria_id}",response_model=Asesorias)
async def get_asesoria(asesoria_id: int):
    rpta = new_asesoria.get_asesoria(asesoria_id)
    return rpta


@router.post("/create_asesoria")
async def create_asesoria(asesoria: Asesorias):
    rpta = new_asesoria.create_asesoria(asesoria)
    return rpta


@router.put("/update_asesoria/{idasesorias}")
async def update_asesoria(idasesorias: int):
    rpta = new_asesoria.update_asesoria(idasesorias)
    return rpta


@router.delete("/delete_asesoria/{idasesorias}")
async def delete_asesoria(idasesorias: int):
    rpta = new_asesoria.delete_asesoria(idasesorias)
    return rpta