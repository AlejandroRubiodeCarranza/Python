import usuarios.conexion as conexion

connect= conexion.conectar()
database= connect[0]
cursor=connect[1]



class Nota:
    
    def __init__(self,usuario_id,titulo="",descripcion=""):
        self.usuario_id=usuario_id
        self.titulo=titulo
        self.descripcion=descripcion
    
    def guardar(self):
        sql="INSERT INTO notas VALUES(null,%s,%s,%s,NOW())"
        nota=(self.usuario_id,self.titulo,self.descripcion)
        
        cursor.execute(sql,nota)
        
        database.commit()
        
        return [cursor.rowcount,self]
    
    def listar(self):
        
        # Hago la consulta
        sql=f"SELECT * FROM notas WHERE usuario_id={self.usuario_id}"
        
        # La ejecuto
        cursor.execute(sql)
        
        # Guardo los resultados
        result=cursor.fetchall()
        
        # Devuelvo los resultados
        return result
    
    def eliminar(self):
        sql=f"DELETE FROM notas WHERE usuario_id={self.usuario_id} AND titulo LIKE '%{self.titulo}%' "
        
        cursor.execute(sql)
        
        # ejecuto los cambios en la base de datos
        database.commit()
        
        # Devuelvo el numero de filas eliminadas
        return [cursor.rowcount,self]