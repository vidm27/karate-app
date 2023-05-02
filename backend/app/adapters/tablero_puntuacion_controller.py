from fastapi import APIRouter, WebSocket, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from backend.core.config import TEMPLATE_PATH, STATIC_PATH

router = APIRouter()
templates = Jinja2Templates(directory=TEMPLATE_PATH)
router.mount(
    STATIC_PATH,
    StaticFiles(directory=STATIC_PATH),
    name="static",
)


@router.get("/score_prompter")
async def score_prompter(request: Request):
    return templates.TemplateResponse('tableroPuntuacion/index.html', {'request': request})


@router.websocket("/score")
async def score_endpoint(webscoket: WebSocket):
    await webscoket.accept()
    while True:
        data = await webscoket.receive_text()
        print(data)
