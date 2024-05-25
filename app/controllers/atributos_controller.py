import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.atributos_model import Atributos
from fastapi.encoders import jsonable_encoder

class AtributosController:


    def get_atributos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM atributos")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'idatributos':data[0],
                    'nombre':data[1],
                    'descripcion':data[2],
                    'estado':data[3],
                    'fecha':data[4],
                    'hora':data[5]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Atributos not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def get_atributo(self, atributo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM atributos WHERE idatributos = %s", (atributo_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'idatributos':int(result[0]),
                    'nombre':result[1],
                    'descripcion':result[2],
                    'estado':result[3],
                    'fecha':result[4],
                    'hora':result[5],
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Atributo not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def create_atributo(self, atributo: Atributos):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO atributos (nombre,descripcion,estado,fecha,hora) VALUES (%s, %s, %s, %s, %s)", 
                           (atributo.nombre, atributo.descripcion, atributo.estado, atributo.fecha, atributo.hora))
            conn.commit()
            conn.close()
            return {"resultado": "Atributo creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close() 


    '''def update_atributo(self, idatributo:int, atributo: Atributos):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                       UPDATE atributos
                       SET nombre = %s,
                       descripcion = %s,
                       estado = %s,
                        fecha = %s,
                        hora = %s
                       WHERE idatributo = %s
                       """, (nombre, descripcion, estado, fecha, hora))
            conn.commit()
            conn.close()
            return {"informacion":"Atributo actualizado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()'''


    def delete_atributo(self, idatributo:int):
        try:           
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE from atributos where idatributo = %s",(idatributo,)) 
            conn.commit()
            conn.close()
            return {"informacion":"Atributo eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()   




##user_controller = UserController()