import tkinter as tk
from tkinter import messagebox

# Stock inicial
stock = {
    'remera': {'S': 5, 'M': 5, 'L': 5},
    'pantalon': {'S': 5, 'M': 5, 'L': 5},
    'gorra': {'S': 5, 'M': 5, 'L': 5},
    'zapatilla': {'S': 5, 'M': 5, 'L': 5}
}

# Función para comprar producto
def comprar_producto(tipo, talle):
    global stock
    if stock[tipo][talle] > 0:
        stock[tipo][talle] -= 1
        return True  # Compra exitosa
    else:
        return False  # Producto agotado

# Función para manejar la acción del botón Comprar
def on_comprar_click(tipo, talle):
    if comprar_producto(tipo, talle):
        actualizar_stock_label(tipo, talle)
        messagebox.showinfo("Compra exitosa", f"Se ha comprado una {tipo} en talle {talle}.")
    else:
        messagebox.showwarning("Sin stock", f"No hay stock disponible para {tipo} en talle {talle}.")

# Función para actualizar el label de stock
def actualizar_stock_label(tipo, talle):
    stock_label.config(text=f"Stock de {tipo} {talle}: {stock[tipo][talle]}")

# Crear ventana principal
root = tk.Tk()
root.title("Gestión de Stock")

# Crear etiqueta para mostrar el stock actual
stock_label = tk.Label(root, text="")
stock_label.pack(pady=10)

# Botones para comprar productos
productos = ['remera', 'pantalon', 'gorra', 'zapatilla']
talles = ['S', 'M', 'L']

for producto in productos:
    for talle in talles:
        button_text = f"Comprar {producto} {talle}"
        tk.Button(root, text=button_text, command=lambda p=producto, t=talle: on_comprar_click(p, t)).pack()

# Función para actualizar el stock inicial en la etiqueta al inicio
actualizar_stock_label('remera', 'S')


root.mainloop()
