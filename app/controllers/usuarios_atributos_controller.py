import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.usuarios_atributos_model import Usuarios_atributos
from fastapi.encoders import jsonable_encoder

class Usuarios_atributosController:


    def get_usuarios_atributos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios_atributos")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'idusuarios_atributos':data[0],
                    'idusuarios':data[1],
                    'idatributos':data[2],
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
                raise HTTPException(status_code=404, detail="Usuarios atributos not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()    

    def get_usuario_atributo(self, usuario_atributo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios_atributos WHERE idusuarios_atributos = %s", (usuario_atributo_id,))
            result = cursor.fetchone()      
            payload = []
            content = {} 
            
            content={
                    'idusuarios_atributos':int(result[0]),
                    'idusuarios':result[1],
                    'idatributos':result[2],
                    'estado':result[3],
                    'fecha':result[4],
                    'hora':result[5]
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Usuario atributo not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

            
    def create_usuario_atributo(self, usuario_atributo: Usuarios_atributos):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios_atributos (idusuarios,idatributos,esatdo,fecha,hora) VALUES (%s, %s, %s, %s, %s)", 
                           (usuario_atributo.idusuarios, usuario_atributo.idatributos, usuario_atributo.estado, usuario_atributo.fecha, usuario_atributo.hora))
            conn.commit()
            conn.close()
            return {"resultado": "Usuario atributo creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    '''def update_usuario_atributo(self, idusuarios_atributos:int, usuario_atributo: usuarios_atributos):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                       UPDATE usuarios_atributos
                       SET idusuarios = %s,
                       idatributos = %s,
                       estado = %s,
                       fecha = %s,
                       hora = %s
                       WHERE idusuarios_atributos = %s
                       """, (idusuarios, idatributos, estado, fecha, hora))
            conn.commit()
            conn.close()
            return {"informacion":"Usuario atributo actualizado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()'''

    def delete_usuario_atributo(self, idusuarios_atributos:int):
        try:           
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE from usuarios_atributos where idusuarios_atributos = %s",(idusuarios_atributos,)) 
            conn.commit()
            conn.close()
            return {"informacion":"Usuario atributo eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    
    
    
       

##user_controller = UserController()