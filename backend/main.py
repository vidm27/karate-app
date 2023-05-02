from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.adapters import torneo_controller, categoria_controller, tablero_puntuacion_controller
from backend.core.config import settings, STATIC_PATH, TEMPLATE_PATH
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")
app.mount(
    STATIC_PATH,
    StaticFiles(directory=STATIC_PATH),
    name="static",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
template = Jinja2Templates(directory=TEMPLATE_PATH)

app.include_router(torneo_controller.router, prefix=settings.API_V1_STR)
app.include_router(categoria_controller.router, prefix=settings.API_V1_STR)
app.include_router(tablero_puntuacion_controller.router)
# template = Jinja2Templates(directory=TEMPLATE_PATH)
#