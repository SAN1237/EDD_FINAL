import pymysql
from tkinter import *

connection=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='Si9HYkqi0ZZ&&&',database='clientes')

def registrar():
   def enviar():
       cursor=connection.cursor()
      
       try:
           sql='''insert into usuarios (DNI,NOMBRE,APELLIDO,CORREO,TELEFONO,PASSWORD) values (%s,%s,%s,%s,%s,%s)'''
           cursor.execute(sql,(int(dni.get()),nom.get(),ape.get(),cor.get(),int(tel.get()),con.get()))
           #Hacer los cambios a la BD
           connection.commit()
           print('Usuario registrado')           
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
   
ventana=Tk()
ventana.geometry('400x200')
ventana.title('Aplicacion')

var=StringVar()
dni=StringVar()
nom=StringVar()
ape=StringVar()
cor=StringVar()
tel=StringVar()
con=StringVar()

titulo=Label(ventana, text="NOMBRE DE LA APP")
subtitulo=Label(ventana, text="slogan")
Tit_Usuario=Label(ventana, text="Usuario:")
Barra_Usuario=Entry(ventana,textvariable=var)
Tit_contraseña=Label(ventana, text="Contraseña:")
Barra_contraseña=Entry(ventana)
titulo_registro = Label(ventana, text= "¿no tienes una cuenta?")
Boton_registro = Button(ventana, text= "registrate", command=registrar)

titulo.pack()
subtitulo.pack()
Tit_Usuario.pack()
Barra_Usuario.pack()
Tit_contraseña.pack()
Barra_contraseña.pack()
titulo_registro.pack()
Boton_registro.pack()

ventana.mainloop()
