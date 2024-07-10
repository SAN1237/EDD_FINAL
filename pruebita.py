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

# cursor.execute('Select * from usuarios')
# for row in cursor:
#     print(row)

# NombreCampos=[i[0] for i in cursor.description]
# print(NombreCampos)
# print('conexion exitosa')

try:
    sql="""
    insert into usuarios (DNI,NOMBRE,APELLIDO,CORREO,DIRECCION,TELEFONO,PASSWORD) values (%s,%s, %s,%s,%s,%s,%s)
    """
    cursor.executescript(sql)
    connection.commit()
    print('se pudo')
except:
    connection.rollback()
    print('no se pudo')


























