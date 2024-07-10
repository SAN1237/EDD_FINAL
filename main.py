import pymysql

connection=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='Si9HYkqi0ZZ&&&',database='clientes')
cursor=connection.cursor()

dni=input('Ingrese su dni: ')
nom=input('Ingrese su nombre: ')
ape=input('Ingrese su apellido: ')
cor=input('Ingrese su correo: ')
dir=input('Ingrese su direccion: ')
tel=input('Ingrese su telefono: ')
con=input('Ingrese su contraseña: ')

try:
    
    sql='''
    insert into usuarios (DNI,NOMBRE,APELLIDO,CORREO,DIRECCION,TELEFONO,PASSWORD) values (%s,%s, %s,%s,%s,%s,%s)
    '''
    cursor.execute(sql,(dni,nom,ape,cor,dir,tel,con))
    #Hacer los cambios a la BD
    connection.commit()
    print('se pudo')
except:
    #Volver para atras, deshacer los cambios --> ROLLBACK
    connection.rollback()
    print('no se pudo')
    
cursor.close    
connection.close    

    
    
    