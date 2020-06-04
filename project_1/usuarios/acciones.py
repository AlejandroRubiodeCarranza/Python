
import usuarios.usuario as modelo
import notas.acciones



class Acciones:
    def registro(self):
        print("Ok!! Vamos a registrarte en el sistema..")
        nombre= input("Introduce tu nombre: ")
        apellidos= input("Introduce tus apellidos: ")
        email= input("Introduce tu email:")
        password=input("Introduce  tu password: ")
        
        usuario=modelo.Usuario(nombre,apellidos,email,password)
        
        registro=usuario.registrar()
        
        
        if registro[0]>=1:
            print(f"Perfecto {registro[1].nombre}, te has registrado con el email {registro[1].email}")
        else:
            print("No te has registrado correctamente")
        
    def login(self):
        print("\nDe acuerdo!! Identificate en el sistema..")
        
        try:
            
            email= input("Introduce tu email:")
            
            password=input("Introduce  tu password: ")
            
            usuario= modelo.Usuario('','',email,password)
            
            login= usuario.identificar()
            
            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                
                self.proximasacciones(login)
                
        except:
            print(f"Login incorrecto!! Intentalo más tarde.")
            
        
    def proximasacciones(self,usuario):
        print("""
              Acciones disponibles:
                  -Crear nota (crear)
                  -Mostrar tus notas (mostrar)
                  -Eliminar nota (eliminar)
                  -Salir (salir)
                """)
            
        accion= input("Qué quieres hacer?: ")
        hazEl=notas.acciones.Acciones()
        
        
        
        if accion=="crear":

            hazEl.crear(usuario)
            # Esto es para que me siga preguntando cosas hasta que le de a salir
            
            self.proximasacciones(usuario)
            
        elif accion=="mostrar":
            hazEl.mostrar(usuario)          
            
            self.proximasacciones(usuario)

        elif accion=="eliminar":
            hazEl.borrar(usuario)            
            
            
            self.proximasacciones(usuario)
           
        elif accion=="salir":
            print(f"Ok {usuario[1]}, hasta pronto!!!")


             
            
            
            
            
            
            