import pymysql
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.font import BOLD
from PIL import ImageTk, Image


try:
    connection=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='Si9HYkqi0ZZ&&&',database='clientes')
except Exception as er:
    print('No se pudo establecer conexion: {er}'.format(er))
    
cursor=connection.cursor()

def registrar():
   def enviar():
       cursor=connection.cursor()
      
       try:
           sql='''insert into usuarios (DNI,NOMBRE,APELLIDO,CORREO,TELEFONO,PASSWORD) values (%s,%s,%s,%s,%s,%s)'''
           cursor.execute(sql,(int(dni.get()),nom.get(),ape.get(),cor.get(),int(tel.get()),con.get()))
           #Hacer los cambios a la BD
           connection.commit()
           print('Usuario registrado')
           messagebox.showinfo('Registro', 'Usuario registrado correctamente')           
       except Exception as e:
          #Volver para atras, deshacer los cambios --> ROLLBACK
          connection.rollback()
          print('Se produjo una excepción: {}'.format(e))
       
       cursor.close    
       connection.close
       root.destroy()                 

   print("Registro en proceso")
   
   root=Toplevel() #Abre una nueva ventana para que el usuario se registre
   root.title('Registrarse')
   root.geometry('500x500')

   LBname=Label(root, text='Nombre:')
   LBname.grid(row=0,column=0)
   LBentry=Entry(root, textvariable=nom)
   LBentry.grid(row=0,column=1)
   
   LBname1=Label(root, text='Apellido:')
   LBname1.grid(row=1,column=0)
   LBentry1=Entry(root, textvariable=ape)
   LBentry1.grid(row=1,column=1)
   
   LBname2=Label(root, text='DNI:')
   LBname2.grid(row=2,column=0)
   LBentry2=Entry(root, textvariable=dni)
   LBentry2.grid(row=2,column=1)
   
   LBname3=Label(root, text='Correo:')
   LBname3.grid(row=3,column=0)
   LBentry3=Entry(root, textvariable=cor)
   LBentry3.grid(row=3,column=1)
   
   LBname4=Label(root, text='Telefono:')
   LBname4.grid(row=4,column=0)
   LBentry4=Entry(root, textvariable=tel)
   LBentry4.grid(row=4,column=1)
   
   LBname5=Label(root, text='Contraseña:')
   LBname5.grid(row=5,column=0)
   LBentry5=Entry(root, textvariable=con)
   LBentry5.grid(row=5,column=1)

   BTenviar=Button(root, text="Enviar", command=enviar)
   BTenviar.grid(row=7,column=1)
def comprobacion():
    def pasaje(columna): #LOS DATOS LOS RECIBO EN FORMA DE TUPLAS DE TUPLAS PORQUE USÉ FETCHALL(). CON ESTA FUNCION PASO DE ESO A UNA LISTA, CUYOS ELEMENTOS SON LAS FILAS DE LA COLUMNA SELECCIONADA DE MI BASE DE DATOS
        cursor.execute('Select {} from usuarios'.format(columna))

        gen=list(cursor.fetchall())

        for i in range(len(gen)):
            gen[i]=list(gen[i])
            gen[i]=gen[i][0]

        print('Datos de la columna seleccionada: ',gen)
        return gen

    DNIusuario=int(var1.get()) #contiene al dni del usuario
    contraseña=var2.get() #contiene la contraseña del usuario
    
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
def comprobacion_moderador():
    def enviar():
        contraseña = moderador_password.get()
        contraseña_correcta = "moderador123"

        if contraseña == contraseña_correcta:
            messagebox.showinfo('Éxito', 'Login de moderador exitoso')
        else:
            messagebox.showerror('Error', 'Contraseña de moderador incorrecta')
        root.destroy()

    root = Toplevel()
    root.title('Login Moderador')
    root.geometry('300x200')

    Label(root, text='Contraseña de Moderador:').pack(pady=10)
    moderador_password = StringVar()
    Entry(root, textvariable=moderador_password, show='*').pack(pady=5)
    Button(root, text="Ingresar", command=enviar).pack(pady=20)

ventana=Tk()
ventana.geometry('400x200')
ventana.title('Aplicacion')

var1=StringVar()
var2=StringVar()
dni=StringVar()
nom=StringVar()
ape=StringVar()
cor=StringVar()
tel=StringVar()
con=StringVar()

Label(ventana, text="NOMBRE DE LA APP").pack()
Label(ventana, text="slogan").pack()
Label(ventana, text="DNI:").pack()
Entry(ventana,textvariable=var1).pack()
Label(ventana, text="Contraseña:").pack()
Entry(ventana,textvariable=var2).pack()
Button(ventana,text='Ingresar',command=comprobacion).pack()
Label(ventana, text= "¿no tenés una cuenta?").pack()
Button(ventana, text= "registrate", command=registrar).pack()
Button(ventana, text="Soy moderador", command=comprobacion_moderador).pack(side=RIGHT)

ventana.mainloop()
