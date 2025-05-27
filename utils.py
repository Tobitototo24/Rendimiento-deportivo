def mostrar_menu():
    print("\n=== Análisis de Rendimiento Deportivo ===")
    print("1. Mostrar todos los participantes")
    print("2. Filtrar por deporte")
    print("3. Filtrar por distancia")
    print("4. Filtrar mejores marcas")
    print("5. Filtrar por edad")
    print("6. Calcular promedio de marcas")
    print("7. Mostrar mejor marca")
    print("8. Mostrar peor marca")
    print("9. Mostrar mejor marca por categoria")
    print("10. Salir")
    

def mostrar_deportes():
    print("\n=== Deportes ===")
    print("1 - Atletismo")
    print("2 - Ciclismo")
    print("3 - Natacion")


def mostrar_distancias():
    print("\n=== Distancias ===")
    print("1 - 60m")
    print("2 - 100m")
    print("3 - 200m")
    print("4 - 400m")


def mostrar_categoria():
    print("\n=== Categoria ===")
    print("1 - Sub-18: < 20")
    print("2 - Sub-30: entre los 20 y 29")
    print("3 - sub-40: entre los 30 y 39")
    print("4 - Mayores: ≥ 40")


def mostrar_participantes(lista):
    if not lista:
        print("No hay participantes para mostrar.")
        return

    print(f"{'Nombre':<20} {'Edad':<5} {'Deporte':<12} {'Distancia':<10} {'Marca':<8}")
    print("-" * 60)

    for participante in lista:
        nombre = participante.get('nombre', 'N/A')
        edad = participante.get('edad', 'N/A')
        deporte = participante.get('deporte', 'N/A')
        distancia = participante.get('distancia', 'N/A')
        marca = participante.get('marca', 'N/A')

        print(f"{nombre:<20} {edad:<5} {deporte:<12} {distancia:<10} {marca:<8}")


def elegir_deporte():
    while True:
        mostrar_deportes()
        op = int(input("Ingresá el deporte (ej: 1): "))
        if op == 1:
            deporte = "atletismo"
            break
        elif op == 2:
            deporte = "ciclismo"
            break
        elif op == 3:
            deporte = "natacion"
            break
        else:
            print("error, deporte no disponible")
    return deporte


def elegir_distancia():
    while True:
        mostrar_distancias()
        op = int(input("Ingresá la distancia (ej: 1): "))
        if op == 1:
            distancia = "60m"
            break
        elif op == 2:
            distancia = "100m"
            break
        elif op == 3:
            distancia = "200m"
            break
        elif op == 3:
            distancia = "400m"
            break
        else:
            print("error, distancia no disponible")
        return distancia


def elegir_edades():
    while True:
        mostrar_categoria()
        op = int(input("Ingresá la categoria (ej: 1): "))
        if op == 1:
            par_edad = [14, 19]
            break
        elif op == 2:
            par_edad = [20, 29]
            break
        elif op == 3:
            par_edad = [30, 39]
            break
        elif op == 3:
            par_edad = [40, 60]
            break
        else:
            print("error, categoria no disponible")
        return par_edad
