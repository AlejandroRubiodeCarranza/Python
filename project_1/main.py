"""
PROYECTO PYTHON-MYSQL:
    -Abrir asistente
    -Login o registro
    -Si elegimos registro, creará un usuario en la base de datos
    -Crear nota, mostrar notas, borrar notas.
    
"""

from usuarios import acciones


print("""
Acciones disponibles:
    -Registro:
    -Login:
""")

hazEl= acciones.Acciones()


accion= input("Que quieres hacer?: ")

if accion == "Registro":
    hazEl.registro()
    
elif accion == "Login":
    hazEl.login()