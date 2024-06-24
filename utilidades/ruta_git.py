import subprocess
from pathlib import Path


def get_git_root() -> Path:
    """Obtiene el directorio raíz del repositorio Git actual.

    Returns:
        Path: El directorio raíz del repositorio Git.

    Raises:
        RuntimeError: Si el directorio actual no es un repositorio Git.
    """
    result = subprocess.run(
        ['git', 'rev-parse', '--show-toplevel'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    if result.returncode != 0:
        raise RuntimeError("Este no es un repositorio Git.")
    return Path(result.stdout.strip())


def main() -> None:
    """Función principal para obtener y mostrar el directorio raíz del repositorio Git."""
    try:
        git_root = get_git_root()
        print("Directorio raíz de Git:", git_root)
    except RuntimeError as e:
        print(e)


if __name__ == "__main__":
    main()
