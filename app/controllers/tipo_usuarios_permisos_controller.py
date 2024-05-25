import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.tipo_usuarios_permisos_model import Tipo_usuarios_permisos
from fastapi.encoders import jsonable_encoder

class Tipo_usuarios_permisosController:


    def get_tipo_usuarios_permisos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tipo_usuarios_permisos")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'idtipo_usuarios_permisos':data[0],
                    'idtipo_usuarios':data[1],
                    'idpermisos':data[2],
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
                raise HTTPException(status_code=404, detail="Tipo usuarios permisos not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()    

    def get_tipo_usuario_permiso(self, tipo_usuario_permiso_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tipo_usuarios_permisos WHERE idtipo_usuarios_permisos = %s", (tipo_usuario_permiso_id,))
            result = cursor.fetchone()      
            payload = []
            content = {} 
            
            content={
                    'idtipo_usuarios_permisos':int(result[0]),
                    'idtipo_usuarios':result[1],
                    'idpermisos':result[2],
                    'estado':result[3],
                    'fecha':result[4],
                    'hora':result[5]
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Tipo usuario permiso not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

            
    def create_tipo_usuario_permiso(self, tipo_usuario_permiso: Tipo_usuarios_permisos):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tipo_usuarios_permisos (idtipo_usuarios,idpermisos,estado,fecha,hora) VALUES (%s, %s, %s, %s, %s)", 
                           (tipo_usuario_permiso.idtipo_usuarios, tipo_usuario_permiso.idpermisos, tipo_usuario_permiso.estado, tipo_usuario_permiso.fecha, tipo_usuario_permiso.hora))
            conn.commit()
            conn.close()
            return {"resultado": "Tipo usuario permiso creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    '''def update_tipo_usuario_permiso(self, idtipo_usuarios_permisos:int, tipo_usuario_permiso: Tipo_usuarios_permisos):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                       UPDATE tipo_usuarios_permisos
                       SET idtipo_usuarios = %s,
                       idpermisos = %s,
                       estado = %s,
                       fecha = %s,
                       hora = %s
                       WHERE idtipo_usuarios_permisos = %s
                       """, (idtipo_usuarios, idpermisos, estado, fecha, hora))
            conn.commit()
            conn.close()
            return {"informacion":"Tipo usuario permiso actualizado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()'''

    def delete_tipo_usuario_permiso(self, idtipo_usuarios_permisos:int):
        try:           
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE from tipo_usuarios_permisos where idtipo_usuarios_permisos = %s",(idtipo_usuarios_permisos,)) 
            conn.commit()
            conn.close()
            return {"informacion":"Tipo usuario permiso eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    
    
    
       

##user_controller = UserController()