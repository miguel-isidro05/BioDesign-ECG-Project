#ejecutar servidor: uvicorn main:app --reload
#para control+c
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# Permitir solicitudes desde cualquier origen (ajusta según sea necesario)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar la carpeta 'Version_1/assets' como archivos estáticos
app.mount("/assets", StaticFiles(directory="Version_1/assets"), name="assets")

# Configurar Jinja2 para ingresar a mi template
templates = Jinja2Templates(directory="Version_1")

# Rutas para servir tus archivos HTML (sirve para ingresar a mis diferentes archivo html responsives
@app.get("/login.html", response_class=HTMLResponse)
async def read_root(request: Request):
    #Aqui se coloca la ruta, lo que no es lo mismo que el nombr de ruta
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/menu_principal.html", response_class=HTMLResponse)
async def menu_principal(request: Request):
    return templates.TemplateResponse("menu_principal.html", {"request": request})

@app.get("/register.html", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/signal_menu.html", response_class=HTMLResponse)
async def signal_menu(request: Request):
    return templates.TemplateResponse("signal_menu.html", {"request": request})

@app.get("/formulario.html", response_class=HTMLResponse)
async def signal_menu(request: Request):
    return templates.TemplateResponse("formulario.html", {"request": request})

# Ejecutar el servidor usando Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

