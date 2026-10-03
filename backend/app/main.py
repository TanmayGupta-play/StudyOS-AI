"""Entry point of the FastAPI app.

Run from the backend/ folder:  uvicorn app.main:app --reload
Then open http://localhost:8000/docs for the interactive API docs.
"""
from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(title=settings.app_name)


@app.get("/health")
def health_check():
    """A health endpoint: lets you (and later, deployment tools) check the server is alive."""
    return {"status": "ok", "app": settings.app_name}
@app.get("/hello/{name}")
def hello(name:str):
    return {"message":f"Hello,{name} from FastAPI"}