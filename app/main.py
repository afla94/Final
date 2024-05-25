from fastapi import FastAPI

from routes.asesorias_routes import router as asesorias_routes
from routes.atributos_routes import router as atributos_routes
from routes.historial_routes import router as historial_routes
from routes.permisos_routes import router as permisos_routes
from routes.solicitudes_routes import router as solicitudes_routes
from routes.tipo_usuarios_permisos_routes import router as tipo_usuarios_permisos_routes
from routes.tipo_usuarios_routes import router as tipo_usuarios_routes
from routes.usuarios_atributos_routes import router as usuarios_atributos_routes
from routes.usuarios_routes import router as usuarios_routes

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    #"http://localhost.tiangolo.com",
    #"https://localhost.tiangolo.com",
    "http://localhost"
    #"http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(asesorias_routes)
app.include_router(atributos_routes)
app.include_router(historial_routes)
app.include_router(permisos_routes)
app.include_router(solicitudes_routes)
app.include_router(tipo_usuarios_permisos_routes)
app.include_router(tipo_usuarios_routes)
app.include_router(usuarios_atributos_routes)
app.include_router(usuarios_routes)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)