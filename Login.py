import tkinter as tk
from tkinter.font import BOLD
from tkinter import ttk, messagebox
from PIL import ImageTk, Image

def leer_imagen( path, size): 
        return ImageTk.PhotoImage(Image.open(path).resize(size, Image.Resampling.LANCZOS))  

def centrar_ventana(ventana,aplicacion_ancho,aplicacion_largo):    
    pantall_ancho = ventana.winfo_screenwidth()
    pantall_largo = ventana.winfo_screenheight()
    x = int((pantall_ancho/2) - (aplicacion_ancho/2))
    y = int((pantall_largo/2) - (aplicacion_largo/2))
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}") 

class Login:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('INICIO DE SESION')
        self.ventana.geometry('800x500') 
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        centrar_ventana(self.ventana,800,500) 
       
        # frame para la imagen
        img = leer_imagen("./imagenLI.jpg",(400,700))
        frame_imagen = tk.Frame(self.ventana, bd=0, width=400, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
        frame_imagen.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_imagen, image=img)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # armar frames
        frame_1 = tk.Frame(self.ventana, bd=0,relief=tk.SOLID, bg='#fcfcfc')
        frame_1.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        
        # frame_2
        # seccion del titulo
        seccion_titulo = tk.Frame(frame_1, height=50, bd=0, relief=tk.SOLID, bg='black')
        seccion_titulo.pack(side="top", fill=tk.X)
        titulo = tk.Label(seccion_titulo, text=" * ITBAfit *", font=(
            'Times', 30), fg="#666a88", bg='#fcfcfc', pady=50)
        titulo.pack(expand=tk.YES, fill=tk.BOTH)
        

        # frame que completa la interfaz restante
        frame_relleno = tk.Frame(frame_1, height=50,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_relleno.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_relleno, text="Usuario", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario = ttk.Entry(frame_relleno, font=('Times', 14), textvariable="hola")
        self.usuario.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_contraseña = tk.Label(frame_relleno, text="Contraseña", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_contraseña.pack(fill=tk.X, padx=20, pady=5)
        self.contraseña = ttk.Entry(frame_relleno, font=('Times', 14))
        self.contraseña.pack(fill=tk.X, padx=20, pady=10)
        self.contraseña.config(show="*")
        
        inicio = tk.Button(frame_relleno, text="Iniciar sesion", font=('Times', 15,BOLD), fg="#FFFFFF", bg='#FFA07A', bd=0) 
        inicio.pack(fill=tk.X, padx=20, pady=20)
        
        moderador = tk.Button(frame_relleno, text="Soy moderador", font=('Times', 12,BOLD), fg="#FFFFFF", bg='#FFA07A', bd=0) 
        moderador.pack(side="right",padx=20)
        
        registro = tk.Button(frame_relleno, text="Registrarse", font=('Times', 12,BOLD), fg="#FFFFFF", bg='#FFA07A', bd=0) 
        registro.pack(side="left",padx=20)
        self.ventana.mainloop()

Login()        