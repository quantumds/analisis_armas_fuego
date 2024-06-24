import pandas as pd


def read_csv(url: str) -> pd.DataFrame:
    """
    Lee un archivo CSV desde una URL y devuelve un DataFrame de pandas.

    Args:
        url (str): La URL del archivo CSV.

    Returns:
        pd.DataFrame: El DataFrame leído desde el archivo CSV.
    """
    df = pd.read_csv(url)
    print(df.head())
    print(df.info())
    return df


def clean_csv(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia un DataFrame seleccionando columnas específicas.

    Args:
        df (pd.DataFrame): El DataFrame a limpiar.

    Returns:
        pd.DataFrame: El DataFrame limpio con columnas específicas seleccionadas.
    """
    df = df[['month', 'state', 'permit', 'handgun', 'long_gun']]
    print(df.columns)
    return df


def rename_col(df: pd.DataFrame) -> pd.DataFrame:
    """
    Renombra una columna específica si está presente en el DataFrame.

    Args:
        df (pd.DataFrame): El DataFrame en el cual se renombrará la columna.

    Returns:
        pd.DataFrame: El DataFrame con la columna renombrada si estaba presente.
    """
    if 'longgun' in df.columns:
        df = df.rename(columns={'longgun': 'long_gun'})
    print(df.columns)
    return df


def test_functions() -> None:
    """
    Prueba las funciones read_csv, clean_csv y rename_col para asegurar que funcionan correctamente.

    Args:
        None

    Returns:
        None
    """
    # Datos de prueba:
    data = {
        'month': ['2021-01', '2021-02'],
        'state': ['NY', 'CA'],
        'permit': [100, 150],
        'handgun': [50, 60],
        'long_gun': [30, 40],
        'longgun': [30, 40]  # Columna adicional para probar renombrado
    }
    df_test = pd.DataFrame(data)

    # Prueba de clean_csv:
    df_cleaned = clean_csv(df_test)
    assert list(df_cleaned.columns) == ['month', 'state', 'permit', 'handgun', 'long_gun'], "clean_csv falló en seleccionar las columnas correctas."

    # Prueba de rename_col:
    df_renamed = rename_col(df_test)
    assert 'long_gun' in df_renamed.columns, "rename_col falló en renombrar la columna 'longgun' a 'long_gun'."

    print("Todas las pruebas pasaron.")


if __name__ == "__main__":
    test_functions()
