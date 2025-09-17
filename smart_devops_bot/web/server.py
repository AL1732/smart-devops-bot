from fastapi import FastAPI
from ..devops.system_info import get_system_info

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Smart DevOps Bot API"}

@app.get("/sysinfo")
def sysinfo():
    return get_system_info()
