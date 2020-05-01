from fastapi import FastAPI

app = FastAPI()


@app.get("/saludo/hola")
def read_hola():
    return {"mensaje": "Hola Leidy"}
