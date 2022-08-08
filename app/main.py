from ast import keyword
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.models import mongodb
from app.models.book import BookModel


BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()



templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    book = BookModel(keyword="파이썬", publisher = "BJPublic",price=2000,image='me.png',hhh="askewq")#쓸데없는 값은 모델 변수에 없는 것으로, 알아서 걸러줌
    print(await mongodb.engine.save(book)) #DB에 저장
    return templates.TemplateResponse("./index.html", {"request": request, "title":"콜렉터북부기"},)



@app.get("/search", response_class=HTMLResponse)
async def sarch(request: Request, q:str):
    print(q)
    return templates.TemplateResponse("index.html", {"request": request, "title":"콜렉터북부기"},)


@app.on_event("startup")
def on_app_start():
    print("helloserver")
    """before app starts"""
    mongodb.connect()
    

    
@app.on_event("shutdown")
def on_app_shutdown():
    print("byeserver")
    """start app shutdown"""
    mongodb.close()

    