from fastapi import FastAPI

app = FastAPI(
    title="Textile Intelligence Platform",
    version="0.1.0",
    description="Data Engineering, Machine Learning and Generative AI Platform"
)


@app.get("/")
def root():
    return {
        "project": "Textile Intelligence Platform",
        "status": "running"
    }