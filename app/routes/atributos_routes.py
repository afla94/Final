from fastapi import APIRouter, HTTPException
from controllers.atributos_controller import *
from models.atributos_model import Atributos

router = APIRouter()

new_historial = AtributosController()


@router.get("/get_atributos/")
async def get_atributos():
    rpta = new_historial.get_atributos()
    return rpta


@router.get("/get_atributo/{atributo_id}",response_model=Atributos)
async def get_atributo(atributo_id: int):
    rpta = new_historial.get_atributo(atributo_id)
    return rpta


@router.post("/create_atributo")
async def create_atributo(atributo: Atributos):
    rpta = new_historial.create_atributo(atributo)
    return rpta

@router.put("/update_atributo/{idatributo}")
async def update_atributo(idatributo: int):
    rpta = new_historial.update_atributo(idatributo)
    return rpta


@router.delete("/delete_atributo/{idatributo}")
async def delete_atributo(idatributo: int):
    rpta = new_historial.delete_atributo(idatributo)
    return rpta