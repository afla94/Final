import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.historial_model import Historial
from fastapi.encoders import jsonable_encoder

class HistorialController:


    def get_historiales(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM historial")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'idhistorial':data[0],
                    'idasesorias':data[1],
                    'diagnostico':data[2],
                    'plan_tratamiento':data[3],
                    'observaciones':data[4],
                    'estado':data[5],
                    'fecha':data[6],
                    'hora':data[7]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Historiales not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def get_historial(self, historial_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM historial WHERE idhistorial = %s", (historial_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'idhistorial':int(result[0]),
                    'idasesorias':result[1],
                    'diagnostico':result[2],
                    'plan_tratamiento':result[3],
                    'observaciones':result[4],
                    'estado':result[5],
                    'fecha':result[6],
                    'hora':result[7]
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Historial not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def create_historial(self, historial: Historial):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO historial (idasesorias,diagnostico,plan_tratamiento,observaciones,estado,fecha,hora) VALUES (%s, %s, %s, %s, %s, %s)", 
                           (historial.idasesorias, historial.diagnostico, historial.plan_tratamiento, historial.observaciones, historial.estado, historial.fecha, historial.hora))
            conn.commit()
            conn.close()
            return {"resultado": "Historial creada"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    '''def update_historial(self, idhistorial:int, historial: Historial):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                       UPDATE historial
                       SET idasesorias = %s,
                       diagnostico = %s,
                       plan_tratamiento = %s,
                       observaciones = %s,
                       estado = %s,
                        fecha = %s,
                        hora = %s
                       WHERE idhistorial = %s
                       """, (idasesorias, diagnostico, plan_tratamiento, observaciones, estado, fecha, hora))
            conn.commit()
            conn.close()
            return {"informacion":"Historial actualizada"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()'''


    def delete_historial(self, idhistorial:int):
        try:           
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE from historial where idhistorial = %s",(idhistorial,)) 
            conn.commit()
            conn.close()
            return {"informacion":"Historial eliminada"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    
       
    
    
    
       

##user_controller = UserController()