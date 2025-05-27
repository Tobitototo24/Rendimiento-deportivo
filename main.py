from calculos import *
from filtros import *
from utils import *
from participantes import *


def main():

    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            mostrar_participantes(participantes)

        elif opcion == "2":
            deporte = elegir_deporte()
            filtrados = filtrar_por_deporte(participantes, deporte)
            mostrar_participantes(filtrados)

        elif opcion == "3":
            deporte = elegir_deporte()
            distancia = elegir_distancia()
            filtrados = filtrar_por_distancia(
                participantes, deporte, distancia)
            mostrar_participantes(filtrados)

        elif opcion == "4":
            deporte = elegir_deporte()
            distancia = elegir_distancia()
            valor = float(
                input("Ingrese el valor de marca límite (ej: 10.00): "))
            filtrados = mejores_que(participantes, deporte, distancia, valor)
            mostrar_participantes(filtrados)

        elif opcion == "5":
            deporte = elegir_deporte()
            distancia = elegir_distancia()
            edades = elegir_edades()
            edad_min = edades[0]
            edad_max = edades[1]
            filtrados = filtrar_por_edad(
                participantes, deporte, edad_min, edad_max)
            mostrar_participantes(filtrados)

        elif opcion == "6":
            deporte = elegir_deporte()
            distancia = elegir_distancia()
            promedio = calcular_promedio(participantes, deporte, distancia)
            print(f"Promedio de marcas: {promedio:.2f}")

        elif opcion == "7":
            deporte = elegir_deporte()
            distancia = elegir_distancia()
            mejor = calcular_mejor_marca(participantes, deporte, distancia)
            print(f"Mejor marca: {mejor:.2f}")

        elif opcion == "8":
            deporte = elegir_deporte()
            distancia = elegir_distancia()
            peor = calcular_peor_marca(participantes, deporte, distancia)
            print(f"Peor marca: {peor:.2f}")

        elif opcion == "9":
            deporte = elegir_deporte()
            distancia = elegir_distancia()
            resultados = mejor_marca_por_categoria(
                participantes, deporte, distancia)

            for categoria, atleta in resultados.items():
                if atleta:
                    print(
                        f"{categoria}: {atleta['nombre']} - {atleta['marca']} s")
                else:
                    print(f"{categoria}: Sin participantes")

        elif opcion == "10":
            print("Vuelva pronto!!")
            break

        else:
            print("Opción inválida. Intentá de nuevo.")


if __name__ == "__main__":
    main()
    print("Hola")
