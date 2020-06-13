from fastapi import FastAPI

app = FastAPI()


@app.get("/saludo/hola")
def read_hola():
    return {"mensaje": "Hola Leidy"}


@app.get("/no_ha_hecho_flexiones/")
def no_ha_hecho_flexiones():
    respuesta_de_funcion = ejecutar_flexiones(iniciar_flexiones=True)

    return {"mensaje": respuesta_de_funcion}


@app.get("/ya_hizo_flexiones/")
def ya_hizo_flexiones():
    respuesta_de_funcion = ejecutar_flexiones(iniciar_flexiones=False, flexiones_a_realizar=0)

    return {"mensaje": respuesta_de_funcion}


def ejecutar_flexiones(iniciar_flexiones, flexiones_a_realizar=20):
    if iniciar_flexiones is True:
        # Procesamiento
        # Contador iniciado en cero
        contador_de_flexiones = 0

        # B. Aumentar en 1 el acumulador por cada flexión realizada
        while contador_de_flexiones < flexiones_a_realizar:
            contador_de_flexiones += 1
            print(f'Flexión número: {contador_de_flexiones}')

    elif iniciar_flexiones is False:
        return "Descansar"

    # Salida
    return f"{flexiones_a_realizar} Flexiones realizadas"

