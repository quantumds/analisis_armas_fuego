import subprocess

def get_git_root():
    try:
        # Ejecuta el comando git para obtener la ruta de la carpeta raíz:
        root_dir = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], stderr=subprocess.STDOUT)
        # Decodifica la salida y elimina cualquier espacio en blanco:
        return root_dir.decode('utf-8').strip()
    except subprocess.CalledProcessError:
        # Maneja el caso donde el comando git falla (por ejemplo, si no es un repositorio git):
        return None

# Llama a la función y muestra la carpeta raíz:
root_dir = get_git_root()
if root_dir:
    print(f"La carpeta raíz del proyecto Git es: {root_dir}")
else:
    print("No se encontró un repositorio Git.")
