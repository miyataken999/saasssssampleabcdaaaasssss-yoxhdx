from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from api.routers import user_router, team_router

app = FastAPI()

app.include_router(user_router)
app.include_router(team_router)

templates = Jinja2Templates(directory="templates")