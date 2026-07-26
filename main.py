import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

# Absolute path set karna taake Railway ko static folder mil jaye
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_path = os.path.join(BASE_DIR, "static", "index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()