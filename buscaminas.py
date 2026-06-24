import tkinter as tk
from tkinter import messagebox
import random

# Configuración del juego
FILAS = 9
COLUMNAS = 9
MINAS = 10

class Buscaminas:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title(" Buscaminas ")
        
        # Matrices lógicas para controlar el juego
        self.tablero_minas = [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]
        self.botones = [[None for _ in range(COLUMNAS)] for _ in range(FILAS)]
        self.celdas_reveladas = 0
        
        self.inicializar_tablero()
        self.crear_interfaz()

    def inicializar_tablero(self):
        # 1. Colocar las minas aleatoriamente usando una tupla de coordenadas
        minas_colocadas = 0
        while minas_colocadas < MINAS:
            f = random.randint(0, FILAS - 1)
            c = random.randint(0, COLUMNAS - 1)
            if self.tablero_minas[f][c] != -1: # -1 representará una mina
                self.tablero_minas[f][c] = -1
                minas_colocadas += 1

        # 2. Calcular los números de advertencia alrededor de las minas
        for f in range(FILAS):
            for c in range(COLUMNAS):
                if self.tablero_minas[f][c] == -1:
                    continue
                # Contamos cuántas minas hay en las 8 celdas vecinas
                self.tablero_minas[f][c] = self.contar_minas_vecinas(f, c)

    def contar_minas_vecinas(self, f, c):
        contador = 0
        # Ciclos anidados para revisar la cuadrícula vecina de 3x3
        for i in range(-1, 2):
            for j in range(-1, 2):
                nueva_f, nueva_c = f + i, c + j
                # Validamos que no nos salgamos de la matriz (límites del tablero)
                if 0 <= nueva_f < FILAS and 0 <= nueva_c < COLUMNAS:
                    if self.tablero_minas[nueva_f][nueva_c] == -1:
                        contador += 1
        return contador

    def crear_interfaz(self):
        # Creamos los botones físicos en la ventana usando el Grid de Tkinter
        for f in range(FILAS):
            for c in range(COLUMNAS):
                # Cada botón manda sus propias coordenadas al hacer clic
                btn = tk.Button(self.ventana, text=" ", width=4, height=2, 
                                font=("Arial", 10, "bold"), bg="#d1d1d1",
                                command=lambda row=f, col=c: self.revelar_celda(row, col))
                btn.grid(row=f, column=c, padx=1, pady=1)
                self.botones[f][c] = btn

    def revelar_celda(self, f, c):
        # Si la celda ya fue presionada, no hacemos nada
        if self.botones[f][c]["state"] == "disabled":
            return

        # ¡PUM! Pisó una mina
        if self.tablero_minas[f][c] == -1:
            self.botones[f][c].config(text="💥", bg="red")
            self.mostrar_minas()
            messagebox.showerror("GAME OVER", "¡Explotaste! Mejor suerte a la próxima.")
            self.ventana.quit()
            return

        # Si es un número, lo mostramos
        valor = self.tablero_minas[f][c]
        if valor > 0:
            colores = {1: "blue", 2: "green", 3: "red", 4: "purple"}
            color_texto = colores.get(valor, "black")
            self.botones[f][c].config(text=str(valor), disabledforeground=color_texto, state="disabled", bg="#f0f0f0")
            self.celdas_reveladas += 1
        else:
            # Si es un espacio vacío (0), usamos recursión automática para abrir los vacíos vecinos
            self.botones[f][c].config(text="", state="disabled", bg="#f0f0f0")
            self.celdas_reveladas += 1
            self.revelar_vacios_vecinos(f, c)

        # Validar condición de victoria
        if self.celdas_reveladas == (FILAS * COLUMNAS) - MINAS:
            messagebox.showinfo("¡VICTORIA!", "¡Felicidades! Desactivaste todas las minas con éxito.")
            self.ventana.quit()

    def revelar_vacios_vecinos(self, f, c):
        # Algoritmo de expansión automática (Inundación lógica)
        for i in range(-1, 2):
            for j in range(-1, 2):
                nueva_f, nueva_c = f + i, c + j
                if 0 <= nueva_f < FILAS and 0 <= nueva_c < COLUMNAS:
                    if self.botones[nueva_f][nueva_c]["state"] != "disabled":
                        self.revelar_celda(nueva_f, nueva_c)

    def mostrar_minas(self):
        # Muestra dónde estaban todas las minas al perder
        for f in range(FILAS):
            for c in range(COLUMNAS):
                if self.tablero_minas[f][c] == -1:
                    self.botones[f][c].config(text="💣", bg="#ff9999")

# Arrancar la aplicación gráfica
if __name__ == "__main__":
    raiz = tk.Tk()
    juego = Buscaminas(raiz)
    raiz.mainloop()