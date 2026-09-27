from fastapi import FastAPI

app = FastAPI(title="Objetos Perdidos UNI")


@app.get("/salud")
def salud():
    return {"estado": "ok"}

# Quien le toque aqui chambea carajo