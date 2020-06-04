import notas.nota as modelo


class Acciones:
    
    def crear(self,usuario):
        print(f"OK {usuario[1]}!! Vamos a crear una nueva nota...")
        
        titulo=input("Introduce el titulo de la nota\n:")
        
        descripcion=input("Introce el contenido de la nota\n:")
        
        nota=modelo.Nota(usuario[0],titulo,descripcion)
        
        guardar= nota.guardar()
        
        if guardar[0]>=1:
            print(f"\nPerfecto, has guardado la nota: {nota.titulo}")
        
        else:
            print("No se ha guardado la nota. Lo siento {usuario[1]} ")
        
    
    def mostrar(self,usuario):
        print(f"\nDe acuerdo {usuario[1]}!! Aquí tienes tus notas:")
        
        nota=modelo.Nota(usuario[0])
        
        notas=nota.listar()
        
        for nota in notas:
            print("\n*****************")
            print(nota[2])
            print(nota[3])
            print("\n*****************")

    def borrar(self,usuario):
        print(f"\nOkey {usuario[1]}, vamos a borrar notas")
        
        titulo=input("Introduce el titulo de la nota que quieres borrar: ")
        
        nota= modelo.Nota(usuario[0],titulo)
        
        eliminar= nota.eliminar()
        
        if eliminar[0]>=1:
            print(f"\nNota eliminada: {nota.titulo}")
            
        else:
            print(f"No se ha eliminado la nota: {nota.titulo}")