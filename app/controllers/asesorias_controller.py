import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.asesorias_model import Asesorias
from fastapi.encoders import jsonable_encoder

class AsesoriasController:

#FUNCION OBTENER TODAS ASESORIAS DE LA TABLA
    def get_asesorias(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM asesorias")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'idasesorias':data[0],
                    'idusuarios':data[1],
                    'idsolicitudes':data[2],
                    'descripcion':data[3],
                    'categoria':data[4],
                    'duracion':data[5],
                    'estado':data[6],
                    'fecha':data[7],
                    'hora':data[8]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Asesorias not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

#FUNCION OBTENER ASESORIAS POR ID
    def get_asesoria(self, asesoria_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM asesorias WHERE idasesorias = %s", (asesoria_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'idasesorias':int(result[0]),
                    'idusuarios':result[1],
                    'idsolicitudes':result[2],
                    'descripcion':result[3],
                    'categoria':result[4],
                    'duracion':result[5],
                    'estado':result[6],
                    'fecha':result[7],
                    'hora':result[8]
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Asesoria not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

#FUNCION CREAR ASESORIAS
    def create_asesoria(self, asesoria: Asesorias):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO asesorias (idusuarios,idsolicitudes,descripcion,categoria,duracion,estado,fecha,hora) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                           (asesoria.idusuarios, asesoria.idsolicitudes, asesoria.descripcion, asesoria.categoria, asesoria.duracion, asesoria.estado, asesoria.fecha, asesoria.hora))
            conn.commit()
            conn.close()
            return {"resultado": "Asesoria creada"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

#FUNCION ACTUALIZAR ASESORIA
    '''def update_asesoria(self, idasesorias:int, asesoria: Asesorias):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                       UPDATE asesorias
                       SET idusuarios = %s,
                       idsolicitudes = %s,
                       descripcion = %s,
                        categoria = %s,
                        duracion = %s,
                        estado = %s,
                        fecha = %s,
                        hora = %s
                       WHERE idasesorias = %s
                       """, (idusuarios, idsolicitudes, descripcion, categoria, duracion, estado, fecha, hora))
            conn.commit()
            conn.close()
            return {"informacion":"Asesoria actualizada"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()'''

#FUNCION ELIMINAR ASESORIA
    def delete_asesoria(self, idasesorias:int):
        try:           
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE from asesorias where idasesorias = %s",(idasesorias,)) 
            conn.commit()
            conn.close()
            return {"informacion":"Asesoria eliminada"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()     
       
    
    
    
       

##user_controller = UserController()