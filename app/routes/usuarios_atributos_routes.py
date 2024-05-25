from fastapi import APIRouter, HTTPException
from controllers.usuarios_atributos_controller import *
from models.usuarios_atributos_model import Usuarios_atributos

router = APIRouter()

new_usuario_atributo = Usuarios_atributosController()


@router.get("/get_usuarios_atributos/")
async def get_usuarios_atributos():
    rpta = new_usuario_atributo.get_usuarios_atributos()
    return rpta


@router.get("/get_usuario_atributo/{usuario_atributo_id}",response_model=Usuarios_atributos)
async def get_usuario_atributo(usuario_atributo_id: int):
    rpta = new_usuario_atributo.get_usuario_atributo(usuario_atributo_id)
    return rpta


@router.post("/create_usuario_atributo")
async def create_usuario_atributo(usuario_atributo: Usuarios_atributos):
    rpta = new_usuario_atributo.create_usuario_atributo(usuario_atributo)
    return rpta


@router.put("/update_usuario_atributo/{idusuarios_atributos}")
async def update_usuario_atributo(idusuarios_atributos: int):
    rpta = new_usuario_atributo.update_usuario_atributo(idusuarios_atributos)
    return rpta


@router.delete("/delete_usuario_atributo/{idusuarios_atributos}")
async def delete_usuario_atributo(idusuarios_atributos: int):
    rpta = new_usuario_atributo.delete_usuario_atributo(idusuarios_atributos)
    return rpta



