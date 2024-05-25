import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.tipo_usuarios_model import Tipo_usuarios
from fastapi.encoders import jsonable_encoder

class Tipo_usuariosController:


    def get_tipo_usuarios(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tipo_usuarios")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'idtipo_usuarios':data[0],
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
                raise HTTPException(status_code=404, detail="Tipo Usuarios not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()    

    def get_tipo_usuario(self, tipo_usuario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tipo_usuario WHERE idtipo_usuarios = %s", (tipo_usuario_id,))
            result = cursor.fetchone()      
            payload = []
            content = {} 
            
            content={
                    'idtipo_usuarios':int(result[0]),
                    'nombre':result[1],
                    'descripcion':result[2],
                    'estado':result[3],
                    'fecha':result[4],
                    'hora':result[5]
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Tipo Usuario not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

            
    def create_tipo_usuario(self, tipo_usuario: Tipo_usuarios):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tipo_usuarios (nombre,descripcion,estado,fecha,hora) VALUES (%s, %s, %s, %s, %s)", 
                           (tipo_usuario.nombre, tipo_usuario.descripcion, tipo_usuario.estado, tipo_usuario.fecha, tipo_usuario.hora))
            conn.commit()
            conn.close()
            return {"resultado": "Tipo Usuario creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    '''def update_tipo_usuario(self, idtipo_usuarios:int, tipo_usuario: Tipo_usuarios):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                       UPDATE tipo_usuarios
                       SET nombre = %s,
                       descripcion = %s,
                       estado = %s,
                       fecha = %s,
                       hora = %s
                       WHERE idtipo_usuarios = %s
                       """, (nombre, descripcion, estado, fecha, hora))
            conn.commit()
            conn.close()
            return {"informacion":"Tipo Usuario actualizado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()'''

    def delete_tipo_usuario(self, idtipo_usuarios:int):
        try:           
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE from tipo_usuarios where idtipo_usuarios = %s",(idtipo_usuarios,)) 
            conn.commit()
            conn.close()
            return {"informacion":"Tipo Usuario eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    
    
    
       

##user_controller = UserController()