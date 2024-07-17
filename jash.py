import tkinter as tk
from tkinter.font import BOLD
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import pymysql

try:
    connection=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='Si9HYkqi0ZZ&&&',database='clientes')
except Exception as er:
    print('No se pudo establecer conexion: {er}'.format(er))
    
cursor=connection.cursor()

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
        titulo = tk.Label(seccion_titulo, text=" * ITBAfit *", font=('Times', 30), fg="#666a88", bg='#fcfcfc', pady=50)
        titulo.pack(expand=tk.YES, fill=tk.BOTH)
        
        

        # frame que completa la interfaz restante
        frame_relleno = tk.Frame(frame_1, height=50,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_relleno.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_relleno, text="Usuario", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario = ttk.Entry(frame_relleno, font=('Times', 14))
        self.usuario.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_contraseña = tk.Label(frame_relleno, text="Contraseña", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_contraseña.pack(fill=tk.X, padx=20, pady=5)
        self.contraseña = ttk.Entry(frame_relleno, font=('Times', 14))
        self.contraseña.pack(fill=tk.X, padx=20, pady=10)
        self.contraseña.config(show="*")
                       
        inicio = tk.Button(frame_relleno, text="Iniciar sesion", font=('Times', 15,BOLD), fg="#FFFFFF", bg='#FFA07A', bd=0,command=self.IniciarSesion) 
        inicio.pack(fill=tk.X, padx=20, pady=20)
        
        moderador = tk.Button(frame_relleno, text="Soy moderador", font=('Times', 12,BOLD), fg="#FFFFFF", bg='#FFA07A', bd=0) 
        moderador.pack(side="right",padx=20)
        
        registro = tk.Button(frame_relleno, text="Registrarse", font=('Times', 12,BOLD), fg="#FFFFFF", bg='#FFA07A', bd=0) 
        registro.pack(side="left",padx=20)
        self.ventana.mainloop()
    
    def comprobacion(self,g,h):
        def pasaje(columna): #LOS DATOS LOS RECIBO EN FORMA DE TUPLAS DE TUPLAS PORQUE USÉ FETCHALL(). CON ESTA FUNCION PASO DE ESO A UNA LISTA, CUYOS ELEMENTOS SON LAS FILAS DE LA COLUMNA SELECCIONADA DE MI BASE DE DATOS
            cursor.execute('Select {} from usuarios'.format(columna))

            gen=list(cursor.fetchall())

            for i in range(len(gen)):
                gen[i]=list(gen[i])
                gen[i]=gen[i][0]

            print('Datos de la columna seleccionada: ',gen)
            return gen

        DNIusuario=int(g) #contiene al dni del usuario
        contraseña=h #contiene la contraseña del usuario
        
        a=pasaje('DNI') #Lista con los datos en la columna DNI de mi tabla en la base de datos 
        b=pasaje('PASSWORD')
        
        if DNIusuario in a:
            print('DNI del usuario encontrado')
            posicion=a.index(DNIusuario)
            
            if contraseña==b[posicion]:
                print('Contraseña correcta')
                return True            
            else:
                print('Contraseña incorrecta')
                messagebox.showerror('Advertencia', 'Contraseña Incorrecta')
                #DARLE LA OPORTUNIDAD DE VOLVER A INGRESAR LA CONTRASEÑA
                #INCLUIR MENSAJE DE QUE LA CONTRASEÑA ESTA MAL EN LA PANTALLA
        else:
            print('DNI del Usuario no encontrado')
            messagebox.showwarning('Advertencia', 'El usuario no existe')
            #INCLUIR MENSAJE DE QUE EL USUARIO NO EXISTE. DECIR QUE NO EXISTE. 
        return True    
    
    def IniciarSesion(self):
        c=self.usuario.get()
        d=self.contraseña.get()
        
        self.comprobacion(c,d)    
                    
Login()        