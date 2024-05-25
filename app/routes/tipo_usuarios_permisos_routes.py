from fastapi import APIRouter, HTTPException
from controllers.tipo_usuarios_permisos_controller import *
from models.tipo_usuarios_permisos_model import Tipo_usuarios_permisos

router = APIRouter()

new_tipo_usuario_permiso = Tipo_usuarios_permisosController()


@router.get("/get_tipo_usuarios_permisos/")
async def get_tipo_usuarios_permisos():
    rpta = new_tipo_usuario_permiso.get_tipo_usuarios_permisos()
    return rpta


@router.get("/get_tipo_usuario_permiso/{tipo_usuario_permiso_id}",)
async def get_tipo_usuario_permiso(tipo_usuario_permiso_id: int):
    rpta = new_tipo_usuario_permiso.get_tipo_usuario_permiso(tipo_usuario_permiso_id)
    return rpta


@router.post("/create_tipo_usuario_permiso")
async def create_tipo_usuario_permiso(tipo_usuario_permiso: Tipo_usuarios_permisos):
    rpta = new_tipo_usuario_permiso.create_tipo_usuario_permiso(tipo_usuario_permiso)
    return rpta


@router.put("/update_tipo_usuario_permiso/{idtipo_usuarios_permisos}")
async def update_tipo_usuario_permiso(idtipo_usuarios_permisos: int):
    rpta = new_tipo_usuario_permiso.update_tipo_usuario_permiso(idtipo_usuarios_permisos)
    return rpta


@router.delete("/delete_tipo_usuario_permiso/{idtipo_usuarios_permisos}")
async def delete_tipo_usuario_permiso(idtipo_usuarios_permisos: int):
    rpta = new_tipo_usuario_permiso.delete_tipo_usuario_permiso(idtipo_usuarios_permisos)
    return rpta