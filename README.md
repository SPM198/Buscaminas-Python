# 💣 Buscaminas Gráfico e Interactivo en Python

Este proyecto es una recreación clásica del juego **Buscaminas (Minesweeper)** a nivel principiante (cuadrícula de 9x9 con 10 minas distribuidas aleatoriamente). Fue desarrollado en Python utilizando la librería nativa **Tkinter** para el diseño de la Interfaz Gráfica de Usuario (GUI), sirviendo como un proyecto base de lógica lógica y control visual.

---

## 🚀 Características y Algoritmos Implementados

* **Interfaz Gráfica Dinámica (Tkinter):** El tablero genera dinámicamente una matriz de botones interactivos vinculados directamente mediante funciones `lambda` a coordenadas matemáticas en un arreglo bidimensional.
* **Algoritmo de Expansión por Inundación (Flood Fill):** Al hacer clic en una casilla vacía (cero minas alrededor), el sistema utiliza un algoritmo **recursivo** para buscar, evaluar y revelar automáticamente todas las celdas vacías contiguas hasta delimitar con celdas numéricas. Esto optimiza la jugabilidad y evita que el usuario tenga que dar clics innecesarios.
* **Cómputo de Matriz Vecina:** Implementación de ciclos anidados con control de desbordamiento de límites (`0 <= nueva_fila < FILAS`) para escanear en tiempo real el entorno 3x3 de cada celda y calcular el número exacto de advertencia de minas periféricas.

---

## 🛠️ Arquitectura del Proyecto

El código está estructurado bajo el enfoque de desarrollo de aplicaciones de escritorio en un solo script modularizado:

* **Estructura de Datos:** Uso de listas anidadas (matrices en Python) para independizar la capa lógica (`tablero_minas`) de la capa de renderizado visual (`botones`).
* **Manejo de Eventos (Event-Driven Programming):** Interrupción y captura inmediata de las acciones del ratón para determinar condiciones críticas de juego como **Game Over** (al pisar una mina) o **Victoria** (al revelar todas las celdas seguras).

---

## ⚙️ Tecnologías y Requerimientos

* **Lenguaje:** Python 3.x
* **Librerías:** `tkinter` (Nativa para entornos de escritorio) y `random` (Para la dispersión aleatoria estocástica de las minas).
* **Entorno:** Multiplataforma (Windows, Linux, macOS).

---

## 💻 Instrucciones de Ejecución

Para iniciar el entorno gráfico del simulador de forma local, clona este repositorio y ejecuta el script principal desde tu terminal:

```bash
# Ejecutar la interfaz gráfica del juego
python buscaminas.py
