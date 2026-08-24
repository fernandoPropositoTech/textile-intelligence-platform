from fastapi import FastAPI

from app.api.machines import router as machines_router


app = FastAPI(
    title="Textile Intelligence Platform",
    version="0.1.0",
    description="Data Engineering, Machine Learning and Generative AI Platform"
)


# Rotas
app.include_router(machines_router)


@app.get("/")
def root():
    return {
        "project": "Textile Intelligence Platform",
        "status": "running"
    }