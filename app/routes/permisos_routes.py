from fastapi import APIRouter, HTTPException
from controllers.permisos_controller import *
from models.permisos_model import Permisos

router = APIRouter()

new_permiso = PermisosController()


@router.get("/get_permisos/")
async def get_permisos():
    rpta = new_permiso.get_permisos()
    return rpta


@router.get("/get_permiso/{permiso_id}",response_model=Permisos)
async def get_permiso(permiso_id: int):
    rpta = new_permiso.get_permiso(permiso_id)
    return rpta


@router.post("/create_permiso")
async def create_permiso(permiso: Permisos):
    rpta = new_permiso.create_permiso(permiso)
    return rpta


@router.put("/update_permiso/{idpermisos}")
async def update_permiso(idpermisos: int):
    rpta = new_permiso.update_permiso(idpermisos)
    return rpta


@router.delete("/delete_permiso/{idpermisos}")
async def delete_permiso(idpermisos: int):
    rpta = new_permiso.delete_permiso(idpermisos)
    return rpta

