# Estas funciones recorren la lista de diccionarios y trabajan sobre los campos 'marca', 'deporte' y 'disciplina'.

def calcular_promedio(lista, deporte, distancia):
    # calcula el promedio de las marcas de todos los participantes que compiten en cierto deporte
    # FRanco Quispe
    pass


def calcular_mejor_marca(lista, deporte, distancia):
    # Encuentra la mejor marca entre todos los participantes que compiten en el deporte
    # FRanco Quispe
    pass


def calcular_peor_marca(lista, deporte, distancia):
    # Encuentra la peor marca entre todos los participantes que compiten en el deporte
    # Valentino
    pass


def mejor_marca_por_categoria(lista, deporte, distancia):
  #diccionarios con las categorias
    categorias = {
        "Sub-20": None,
        "Sub-30": None,
        "Sub-40": None,
        "Mayores de 40": None
    }

    rangos = {
        "Sub-20": (14, 19),
        "Sub-30": (20, 29),
        "Sub-40": (30, 39),
        "Mayores de 40": (40, 60)
    }
#esto filtra a los atletas por el deporte y la distancia usando el "filtrar_por_edad"
    for categoria, (edad_min, edad_max) in rangos.items():
        sublista = filtrar_por_edad(lista, deporte, edad_min, edad_max)
        sublista = [p for p in sublista if p["distancia"] == distancia]

        if sublista: 
            mejor = min(sublista, key=lambda x: x["marca"])
            categorias[categoria] = mejor
        else:
            categorias[categoria] = None

    return categorias


def calcular_3(lista, deporte, distancia):
    # funcion a implementar
    pass
