from fastapi import APIRouter, HTTPException
from controllers.tipo_usuarios_controller import *
from models.tipo_usuarios_model import Tipo_usuarios

router = APIRouter()

new_tipo_usuario = Tipo_usuariosController()


@router.get("/get_tipo_usuarios/")
async def get_tipo_usuarios():
    rpta = new_tipo_usuario.get_tipo_usuarios()
    return rpta


@router.get("/get_tipo_usuario/{tipo_usuario_id}",response_model=Tipo_usuarios)
async def get_tipo_usuario(tipo_usuario_id: int):
    rpta = new_tipo_usuario.get_tipo_usuario(tipo_usuario_id)
    return rpta


@router.post("/create_tipo_usuario")
async def create_tipo_usuario(tipo_usuario: Tipo_usuarios):
    rpta = new_tipo_usuario.create_tipo_usuario(tipo_usuario)
    return rpta


@router.put("/update_tipo_usuario/{idtipo_usuarios}")
async def update_tipo_usuario(idtipo_usuarios: int):
    rpta = new_tipo_usuario.update_tipo_usuario(idtipo_usuarios)
    return rpta


@router.delete("/delete_tipo_usuario/{idtipo_usuarios}")
async def delete_tipo_usuario(idtipo_usuarios: int):
    rpta = new_tipo_usuario.delete_tipo_usuario(idtipo_usuarios)
    return rpta