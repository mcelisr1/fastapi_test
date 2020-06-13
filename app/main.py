from fastapi import FastAPI

app = FastAPI()


@app.get("/saludo/hola")
def read_hola():
    return {"mensaje": "Hola Leidy"}


@app.get("/realizar_flexiones/")
def realizar_flexiones():    
    # iniciar_flexiones = False
    
    # Entradas
    # A. Identificar acción para iniciar las flexiones
    iniciar_flexiones = True # Boolean

    # B. Cantidad de flexiones a realizar
    flexiones_a_realizar = 20

    if iniciar_flexiones is True:
        # Procesamiento
        # Contador iniciado en cero
        contador_de_flexiones = 0

        # B. Aumentar en 1 el acumulador por cada flexión realizada
        while contador_de_flexiones < 20:
            contador_de_flexiones += 1
            print(f'Flexión número: {contador_de_flexiones}')

    elif iniciar_flexiones is False:
        return {"mensaje": f"Descansar"}

    # Salida
    return {"mensaje": f"{flexiones_a_realizar} Flexiones realizadas"}
