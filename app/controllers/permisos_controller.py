import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.permisos_model import Permisos
from fastapi.encoders import jsonable_encoder

class PermisosController:


    def get_permisos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM permisos")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'idpermisos':data[0],
                    'descripcion':data[1],
                    'estado':data[2],
                    'fecha':data[3],
                    'hora':data[4]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Permisos not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def get_permiso(self, permiso_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM permisos WHERE idpermisos = %s", (permiso_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'idpermisos':int(result[0]),
                    'descripcion':result[1],
                    'estado':result[2],
                    'fecha':result[3],
                    'hora':result[4]
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Permiso not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def create_permiso(self, permiso: Permisos):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO permisos (descripcion,estado,fecha,hora) VALUES (%s, %s, %s, %s)", 
                           (permiso.descripcion, permiso.estado, permiso.fecha, permiso.hora))
            conn.commit()
            conn.close()
            return {"resultado": "Permiso creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    
    '''def update_permiso(self, idpermisos:int, permiso: Permisos):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                       UPDATE permisos
                       SET descripcion = %s,
                       estado = %s,
                       fecha = %s,
                       hora = %s
                       WHERE idpermisos = %s
                       """, (descripcion, estado, fecha, hora))
            conn.commit()
            conn.close()
            return {"informacion":"Permiso actualizado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()'''


    def delete_permiso(self, idpermisos:int):
        try:           
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE from permisos where idpermisos = %s",(idpermisos,)) 
            conn.commit()
            conn.close()
            return {"informacion":"Permiso eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    
       
    
    
    
       

##user_controller = UserController()