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
