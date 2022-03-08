import mysql.connector
from mysql.connector import Error

class DAO():
    
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = '3306',
                user = 'root',
                password = '',
                db = 'despachos'
            )
        except Error as ex:
            print("Error al intentar la conxexion: {0}".format(ex))

    def listarDespachos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM despacho")
                despachos = cursor.fetchall()
                return despachos
            except Error as ex:
                print("Error al intentar la conxexion: {0}".format(ex))

    def registrarDespacho(self, desp):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO despacho (cliente, direccion, ciudad, telefono, unidades, observacion, fecha) VALUES ('{0}', '{1}', '{2}', '{3}', {4}, '{5}', '{6}')"
                cursor.execute(sql.format(desp[0], desp[1], desp[2], desp[3], desp[4], desp[5], desp[6]))
                self.conexion.commit()
                print("¡El despacho se ha creado con exito!") 
            except Error as ex:
                print("Error al intentar la conxexion: {0}".format(ex))