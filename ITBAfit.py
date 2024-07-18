import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import pymysql

def conectar_db():
    try:
        return pymysql.connect(host='127.0.0.1',port=3306,user='root',password='Si9HYkqi0ZZ&&&',database='clientes')
    except Exception as er:
        print('No se pudo establecer conexion: {er}'.format(er))
    
def leer_imagen( path, size): 
        return ImageTk.PhotoImage(Image.open(path).resize(size, Image.Resampling.LANCZOS))  
def centrar_ventana(ventana,aplicacion_ancho,aplicacion_largo):    
    
    pantall_ancho = ventana.winfo_screenwidth()
    pantall_largo = ventana.winfo_screenheight()
    x = int((pantall_ancho/2) - (aplicacion_ancho/2))
    y = int((pantall_largo/2) - (aplicacion_largo/2))
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")       

def registrarse():
    def cerrar_registro():
        ventana_reg.destroy()
    def enviar():
        
        connection = conectar_db()
        cursor = connection.cursor()

        try:
            sql = '''INSERT INTO usuarios (DNI, NOMBRE, APELLIDO, CORREO, TELEFONO, PASSWORD) VALUES (%s, %s, %s, %s, %s, %s)'''
            cursor.execute(sql, (int(dni.get()), nom.get(), ape.get(), cor.get(), int(tel.get()), con.get()))
            connection.commit()
            messagebox.showinfo('Éxito', 'Usuario registrado correctamente')
        except Exception as e:
            connection.rollback()
            messagebox.showerror('Error', f'Se produjo una excepción: {e}')
        finally:
            cursor.close()
            connection.close()
            ventana_reg.destroy()
    
    ventana_reg=tk.Toplevel()
    ventana_reg.title('Nuevo registro') 
    ventana_reg.geometry('400x250')
    ventana_reg.resizable(width=0, height=0)
    centrar_ventana(ventana_reg,800,500)
    
    imagen_registro= leer_imagen("./imagenLI.jpg",(400,700))
    
    frame_imagen_reg = tk.Frame(ventana_reg, bd=0, width=400, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
    frame_imagen_reg.pack(side="left", expand=tk.NO, fill=tk.BOTH)
    label_img = tk.Label(frame_imagen_reg, image=imagen_registro)
    label_img.place(x=0, y=0, relwidth=1, relheight=1)
    
    # armar frames
    frame_1_datos = tk.Frame(ventana_reg, bd=0,relief=tk.SOLID, bg='#fcfcfc')
    frame_1_datos.pack(side="right", expand=tk.YES, fill=tk.BOTH)
    titulo_reg = tk.Label(frame_1_datos,text=" * BIENVENIDO *", font=('Times', 30), fg="#666a88", bg='#fcfcfc', pady=5)
    titulo_reg.pack()
    separador = tk.Label(frame_1_datos,text=" ----------------", font=('Times', 30), fg="#FFA07A", bg='#fcfcfc')
    separador.pack()
    subtit_reg = tk.Label(frame_1_datos,text="  Porfavor rellene sus datos ", font=('Times', 13), fg="#666a88", bg='#fcfcfc' )
    subtit_reg.pack()
    
    dni = StringVar()
    nom = StringVar()
    ape = StringVar()
    cor = StringVar()
    tel = StringVar()
    con = StringVar()
    
    Label(frame_1_datos, text='Nombre:',font=('Times', 14), fg="#666a88", bg='#fcfcfc').pack()
    Entry(frame_1_datos, textvariable=nom).pack()
    
    Label(frame_1_datos, text='Apellido:',font=('Times', 14), fg="#666a88", bg='#fcfcfc').pack()
    Entry(frame_1_datos, textvariable=ape).pack()
    
    Label(frame_1_datos, text='DNI:',font=('Times', 14), fg="#666a88", bg='#fcfcfc').pack()
    Entry(frame_1_datos, textvariable=dni).pack()
    
    Label(frame_1_datos, text='Correo:',font=('Times', 14), fg="#666a88", bg='#fcfcfc').pack()
    Entry(frame_1_datos, textvariable=cor).pack()
    
    Label(frame_1_datos, text='Teléfono:',font=('Times', 14), fg="#666a88", bg='#fcfcfc').pack()
    Entry(frame_1_datos, textvariable=tel).pack()
    
    Label(frame_1_datos, text='Contraseña:',font=('Times', 14), fg="#666a88", bg='#fcfcfc').pack()
    Entry(frame_1_datos, textvariable=con, show='*').pack()

    Button(frame_1_datos, text="Enviar",font=('Times', 14), fg="#FFFFFF", bg='#FFA07A', command=enviar).pack()
    Button(frame_1_datos, text="Volver",font=('Times', 12), fg="#FFFFFF", bg='#FFA07A',command=cerrar_registro).pack(side=RIGHT, padx=10)
    
    ventana_reg.mainloop()

    
def moderador_inicio(cerrar_ventana_principal):  
    def enviar():
        contraseña = mod_password.get()
        contraseña_correcta = "ITBAfit"
       
        if contraseña == contraseña_correcta:
            ventana_mod.destroy()
            messagebox.showinfo('Éxito', 'Login de moderador exitoso')
            cerrar_ventana_principal() 
            ModPanel()
                 
        else:
            messagebox.showerror('Error', 'Contraseña de moderador incorrecta')
            ventana_mod.destroy()
    
    ventana_mod=tk.Toplevel()
    ventana_mod.title('inicio moderadores') 
    ventana_mod.geometry('400x250')
    ventana_mod.resizable(width=0, height=0)
    centrar_ventana(ventana_mod,400,250) 
    
    contraseña_mod = tk.Label(ventana_mod, text="Contraseña", font=('Times', 14), fg="#666a88", anchor="w")
    contraseña_mod.pack(fill=tk.X, padx=20, pady=5)
    mod_password = ttk.Entry(ventana_mod, font=('Times', 14))
    mod_password.pack(fill=tk.X, padx=20, pady=10)
    mod_password.config(show="*")
    
    ingresar_mod=tk.Button(ventana_mod, text="Ingresar", font=('Times', 14), fg="#FFFFFF", bg='#FFA07A', anchor="w",command=enviar)
    ingresar_mod.pack()  

connection=conectar_db()
cursor=connection.cursor()

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
        
    def cerrar_ventana_principal(self):
        self.ventana.destroy()
    
class ModPanel:
    def Editor_BD():
        ventana_Edit = tk.Tk()
        ventana_Edit.title('Inicio de sesion')
        ventana_Edit.geometry('800x500') 
        ventana_Edit.config(bg='#FFA07A')
        ventana_Edit.resizable(width=0, height=0)
        centrar_ventana(ventana_Edit,400,200) 
        
        ventana_Edit.mainloop
    def __init__(self):
        self.ventana_mod = tk.Tk()
        self.ventana_mod.title('Inicio de sesion')
        self.ventana_mod.geometry('800x500') 
        self.ventana_mod.config(bg='#FFA07A')
        self.ventana_mod.resizable(width=0, height=0)
        centrar_ventana(self.ventana_mod,400,200) 
        # armar frames
        frame_1 = tk.Frame(self.ventana_mod,height=50, bd=0,relief=tk.SOLID, bg='#fcfcfc')
        frame_1.pack(side="top", fill=tk.X)
        
        titulo = tk.Label(frame_1, text="Seleccione producto a modificar",font=('Times', 20,BOLD), fg="#666a88", bg='#fcfcfc')
        titulo.pack()
        
        frame_relleno = tk.Frame(self.ventana_mod, height=50,  bd=0, relief=tk.SOLID, bg='#FFA07A')
        frame_relleno.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)
        
        subtitulo1 = tk.Label(frame_relleno, text="* Remeras *",font=('Times', 10), fg="#000000", bg='#FFA07A',padx=15,pady=5)
        subtitulo1.grid(row=0, column=0)
        subtitulo2 = tk.Label(frame_relleno, text="* Zapatillas *",font=('Times', 10), fg="#000000", bg='#FFA07A',padx=15,pady=5)
        subtitulo2.grid(row=0, column=1)
        subtitulo3 = tk.Label(frame_relleno, text="* Pantalones *",font=('Times', 10), fg="#000000", bg='#FFA07A',padx=15,pady=5)
        subtitulo3.grid(row=0, column=2)
        subtitulo4 = tk.Label(frame_relleno, text="* Gorras *",font=('Times', 10), fg="#000000", bg='#FFA07A',padx=15,pady=5)
        subtitulo4.grid(row=0, column=3)
        
        #TALLES REMERA
        talle_R_S = tk.Button(frame_relleno,bd=0, text="R-S",height=1,font=('Times', 10), fg="#000000", bg='#FFFFFF')
        talle_R_S.grid(row=1, column=0,pady=10)
        talle_R_M = tk.Button(frame_relleno,bd=0, text="R-M",height=1,font=('Times', 10), fg="#000000", bg='#FFFFFF')
        talle_R_M.grid(row=2, column=0,pady=10)
        talle_R_L = tk.Button(frame_relleno,bd=0, text="R-L",height=1,font=('Times', 10), fg="#000000", bg='#FFFFFF')
        talle_R_L.grid(row=3, column=0,pady=10)
        
        #TALLES Pantalon
        talle_P_S = tk.Button(frame_relleno,bd=0, text="T34",height=1,font=('Times', 10), fg="#000000", bg='#FFFFFF')
        talle_P_S.grid(row=1, column=1,pady=10)
        talle_P_M = tk.Button(frame_relleno,bd=0, text="T37",height=1,font=('Times', 10), fg="#000000", bg='#FFFFFF')
        talle_P_M.grid(row=2, column=1,pady=10)
        talle_P_L = tk.Button(frame_relleno,bd=0, text="T40",height=1,font=('Times', 10), fg="#000000", bg='#FFFFFF')
        talle_P_L.grid(row=3, column=1,pady=10)
        
        #TALLES PANTALON
        talle_P_S = tk.Button(frame_relleno,bd=0, text="P-S",height=1,font=('Times', 10), fg="#000000", bg='#FFFFFF')
        talle_P_S.grid(row=1, column=2,pady=10)
        talle_P_M = tk.Button(frame_relleno,bd=0, text="P-M",height=1,font=('Times', 10), fg="#000000", bg='#FFFFFF')
        talle_P_M.grid(row=2, column=2,pady=10)
        talle_P_L = tk.Button(frame_relleno,bd=0, text="P-L",height=1,font=('Times', 10), fg="#000000", bg='#FFFFFF')
        talle_P_L.grid(row=3, column=2,pady=10)
        
        #TALLES GORRA
        talle_G_S = tk.Button(frame_relleno,bd=0, text="Niño",height=1,font=('Times', 10), fg="#000000", bg='#FFFFFF')
        talle_G_S.grid(row=1, column=3,pady=10)
        talle_G_M = tk.Button(frame_relleno,bd=0, text="Adolecente",height=1,font=('Times', 10), fg="#000000", bg='#FFFFFF')
        talle_G_M.grid(row=2, column=3,pady=10)
        talle_G_L = tk.Button(frame_relleno,bd=0, text="Adulto",height=1,font=('Times', 10), fg="#000000", bg='#FFFFFF')
        talle_G_L.grid(row=3, column=3,pady=10)
    
        self.ventana_mod.mainloop()    

class MainPanel:
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title('Main Menu')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg="#fcfcfc")
        self.ventana.resizable(width=0, height=0)
        
        self.imagen =leer_imagen("./imagenLI.jpg", (200, 200))
        
        self.label = tk.Label(self.ventana, image=self.imagen, bg='#3a7ff6')
        self.label.place(x=0, y=0, relwidth=1, relheight=1)
        self.ventana.mainloop()
        
Login()    