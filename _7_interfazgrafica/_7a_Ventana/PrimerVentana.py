import tkinter as tk

# Función que se ejecutará al presionar el botón
def boton_presionado():
    print("¡Botón presionado desde la ventana gráfica!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo Gráfico en Consola")
ventana.geometry("400x200")  # Establecer tamaño de la ventana

# Crear un botón
boton = tk.Button(ventana, text="Haz clic aquí", command=boton_presionado)
boton.pack(pady=50)  # Agregar el botón a la ventana con margen vertical

# Mostrar un mensaje inicial en la consola
print("La ventana gráfica está activa. Presiona el botón para interactuar.")

# Iniciar el bucle principal de la ventana
ventana.mainloop()
