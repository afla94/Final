from fastapi import APIRouter, HTTPException
from controllers.usuarios_controller import *
from models.usuarios_model import Usuarios

router = APIRouter()

new_usuario = UsuariosController()


@router.get("/get_usuarios/")
async def get_usuarios():
    rpta = new_usuario.get_usuarios()
    return rpta


@router.get("/get_usuario/{usuario_atributo_id}",response_model=Usuarios)
async def get_usuario(usuario_atributo_id: int):
    rpta = new_usuario.get_usuario(usuario_atributo_id)
    return rpta


@router.post("/create_usuarios")
async def create_usuarios(usuario: Usuarios):
    rpta = new_usuario.create_usuarios(usuario)
    return rpta


@router.put("/update_usuario/{idusuarios}")
async def update_usuario(idusuarios: int):
    rpta = new_usuario.update_usuario(idusuarios)
    return rpta


@router.delete("/delete_usuario/{idusuarios}")
async def delete_usuario(idusuarios: int):
    rpta = new_usuario.delete_usuario(idusuarios)
    return rpta