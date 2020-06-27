from fastapi import FastAPI

app = FastAPI()


@app.get("/saludo/hola")
def read_hola():
    return {"mensaje": "Hola Leidy"}


@app.get("/explorando_variables")
def explorando_variables():
    edad = 18
    nombre = 'Juanita'
    es_mujer = True
    estatura = 1.58
    comidas_favoritas = ['Arepa de Huevo', 'Mote de queso', 'Posta Cartagenera']

    print(f'Nombre: {nombre} Edad: {edad} Mujer: {es_mujer} Estatura: {estatura}')    
    print(f'Comidas favoritas: {comidas_favoritas}')

    print(f'Segunda Comida favorita: {comidas_favoritas[1]}')
    comidas_favoritas.append('Carimañola')    
    print(f'Comidas favoritas: {comidas_favoritas}')
    comidas_favoritas.insert(2, 'Buñuelo')
    print(f'Comidas favoritas: {comidas_favoritas}')
    print(f'Slice: {comidas_favoritas[1:3]}')
    print(f'Slice -2: {comidas_favoritas[:-2]}')
    otras_comidas = ['Arroz de coco', 'Sopa de Mondongo']
    comidas_favoritas.extend(otras_comidas)    
    print(f'Comidas favoritas: {comidas_favoritas}')
    comidas_favoritas.pop(0)
    print(f'Comidas favoritas: {comidas_favoritas}')
    comidas_favoritas.remove('Buñuelo')
    print(f'Comidas favoritas: {comidas_favoritas}')

    print(f'Tipos: {type(nombre)} {type(edad)} {type(es_mujer)} {type(estatura)} {type(comidas_favoritas)}')

    edad = 'Veinte'
    nombre = 'Juanchito'
    es_mujer = 'No'
    estatura = 168
    comidas_favoritas = ('Bandeja paisa', 'Ajiaco', 'Tamal')

    print(f'Nombre: {nombre} Edad: {edad} Mujer: {es_mujer} Estatura: {estatura}')
    print(f'Comidas favoritas: {comidas_favoritas}')

    print(f'Tercera Comida favorita: {comidas_favoritas[2]}')
    print(f'Slice: {comidas_favoritas[0:2]}')
    print(f'Slice -2: {comidas_favoritas[:-2]}')

    print(f'Tipos: {type(nombre)} {type(edad)} {type(es_mujer)} {type(estatura)} {type(comidas_favoritas)}')

    return {"mensaje": "Variables exploradas"}


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

