import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.usuarios_model import Usuarios
from fastapi.encoders import jsonable_encoder

class UsuariosController:


    def get_usuarios(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'idusuarios':data[0],
                    'idtipo_usuarios':data[1],
                    'nombre':data[2],
                    'direccion':data[3],
                    'telefono':data[4],
                    'email':data[5],
                    'contraseña':data[6],
                    'estado':data[7],
                    'fecha':data[8],
                    'hora':data[9]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Usuarios not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()    

    def get_usuario(self, usuario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE idusuarios = %s", (usuario_id,))
            result = cursor.fetchone()      
            payload = []
            content = {} 
            
            content={
                    'idusuarios':int(result[0]),
                    'idtipo_usuarios':result[1],
                    'nombre':result[2],
                    'direccion':result[3],
                    'telefono':result[4],
                    'email':result[5],
                    'contraseña':result[6],
                    'estado':result[7],
                    'fecha':result[8],
                    'hora':result[9]
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Usuario not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

            
    def create_usuarios(self, usuario: Usuarios):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (idtipo_usuarios,nombre,direccion,telefono,email,contraseña,estado,fecha,hora) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                           (usuario.idtipo_usuarios, usuario.nombre, usuario.direccion, usuario.telefono, usuario.email, usuario.contraseña, usuario.estado, usuario.fecha, usuario.hora))
            conn.commit()
            conn.close()
            return {"resultado": "Usuario creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    '''def update_usuario(self, idusuarios:int, usuario: Usuarios):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                       UPDATE usuarios
                       SET idtipo_usuarios = %s,
                       nombre = %s,
                       direccion = %s,
                       telefono = %s,
                       email = %s,
                        contraseña = %s,
                        estado = %s,
                        fecha = %s,
                        hora = %s   
                       WHERE idusuarios = %s
                       """, (idtipo_usuarios, nombre, direccion, telefono, email, contraseña, estado, fecha, hora))
            conn.commit()
            conn.close()
            return {"informacion":"Usuario actualizado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()'''

    def delete_usuario(self, idusuarios:int):
        try:           
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE from usuarios where idusuarios = %s",(idusuarios,)) 
            conn.commit()
            conn.close()
            return {"informacion":"Usuario eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    
    
    
       

##user_controller = UserController()