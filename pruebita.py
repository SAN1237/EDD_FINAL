import pymysql
from tkinter import *

connection=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='Si9HYkqi0ZZ&&&',database='clientes')
cursor=connection.cursor()

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
    print
    a=pasaje('DNI') #Lista con los datos en la columna DNI de mi tabla en la base de datos 
    b=pasaje('PASSWORD')
    
    for x in a:
        if DNIusuario==x:
            print('DNI del usuario encontrado')
            posicion=a.index(x)
            if contraseña==b[posicion]:
                print('Contraseña correcta')
                return True
                #DAR ACCESO A LA APP
            else:
                print('Contraseña incorrecta')
                
                #DARLE LA OPORTUNIDAD DE VOLVER A INGRESAR LA CONTRASEÑA
                #INCLUIR MENSAJE DE QUE LA CONTRASEÑA ESTA MAL EN LA PANTALLA
        else:
            print('DNI del Usuario no encontrado')
            
            #INCLUIR MENSAJE DE QUE EL USUARIO NO EXISTE. DECIR QUE NO EXISTE. 

    print(a)
    print(b)

ventana=Tk()

var1=StringVar()
var2=StringVar()

Tit_Usuario=Label(ventana, text="DNI:")
Barra_Usuario=Entry(ventana,textvariable=var1)
Tit_contraseña=Label(ventana, text="Contraseña:")
Barra_contraseña=Entry(ventana,textvariable=var2)
Boton_LogIn=Button(ventana,text='Ingresar',command=comprobacion)

Tit_Usuario.pack()
Barra_Usuario.pack()
Tit_contraseña.pack()
Barra_contraseña.pack()
Boton_LogIn.pack()

ventana.mainloop()
 
cursor.close    
connection.close


def usuario_existe(usuario):
    cursor.execute("select * from login where usuarios=%s".format(usuario))
    resultado = cursor.fetchone()
    return resultado is not None
