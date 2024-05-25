import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.solicitudes_model import Solicitudes
from fastapi.encoders import jsonable_encoder

class SolicitudesController:


    def get_solicitudes(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM solicitudes")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'idsolicitudes':data[0],
                    'descripcion':data[1],
                    'disponible':data[2],
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
                raise HTTPException(status_code=404, detail="Solicitudes not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close() 


    def get_solicitud(self, solicitud_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM solicitudes WHERE idsolicitudes = %s", (solicitud_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'idsolicitudes':int(result[0]),
                    'descripcion':result[1],
                    'disponible':result[2],
                    'estado':result[3],
                    'fecha':result[4],
                    'hora':result[5]
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Solicitud not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()    
            
                   
    def create_solicitud(self, solicitud: Solicitudes):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO solicitudes (descripcion,disponible,estdo,fecha,hora) VALUES (%s, %s, %s, %s, %s)", 
                           (solicitud.descripcion, solicitud.disponible, solicitud.estado, solicitud.fecha, solicitud.hora))
            conn.commit()
            conn.close()
            return {"resultado": "Solicitud creada"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    '''def update_solicitud(self, idsolicitudes:int, solicitud: Solicitudes):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                       UPDATE solicitudes
                       SET descripcion = %s,
                       disponible = %s,
                       estado = %s,
                        fecha = %s,
                        hora = %s
                       WHERE idservicios = %s
                       """, (descripcion, disponible, estado, fecha, hora))
            conn.commit()
            conn.close()
            return {"informacion":"Solicitud actualizada"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()'''

    def delete_solicitud(self, idsolicitud:int):
        try:           
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE from solicitudes where idsolicitudes = %s",(idsolicitud,)) 
            conn.commit()
            conn.close()
            return {"informacion":"Solicitud eliminada"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()    

    
       
    
    
    
       

##user_controller = UserController()