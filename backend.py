from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {
        "status": "ok",
        "ollama": "connected"
    }

@app.post("/evaluate")
def evaluate():
    return {
        "message": "Prototype evaluation endpoint"
    }