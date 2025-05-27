📊 Análisis de Rendimiento Deportivo
Este proyecto es una herramienta interactiva desarrollada en Python que permite analizar y visualizar datos de rendimiento deportivo en disciplinas como atletismo, aplicando filtros y cálculos estadísticos sobre los participantes.

🚀 Funcionalidades
El programa ofrece las siguientes funcionalidades a través de un menú interactivo:

Mostrar todos los participantes

Filtrar por deporte

Filtrar por distancia

Filtrar por marcas mejores que un valor límite

Filtrar por rango de edad

Calcular el promedio de marcas

Mostrar la mejor marca registrada

Mostrar la peor marca registrada

Mejor marca por categoría de edad

Salir del programa

🧱 Estructura del Proyecto
El proyecto está dividido en varios módulos para mantener una buena organización del código:

main.py – Contiene el menú principal y la lógica de interacción con el usuario.

calculos.py – Funciones para calcular promedios, mejores y peores marcas.

filtros.py – Funciones para filtrar participantes por deporte, distancia, edad, etc.

utils.py – Funciones utilitarias para interactuar con el usuario (como elegir deporte/distancia).

participantes.py – Base de datos simulada con los participantes y sus marcas.

🏃‍♂️ Estructura de los Participantes
Los participantes están representados como diccionarios con información como:

python
Copiar
Editar
{
    "nombre": "Juan Pérez",
    "edad": 25,
    "deporte": "Atletismo",
    "distancia": 100,
    "marca": 10.75,  # en segundos
    "categoría": "Adulto"
}
