import pandas as pd


def breakdown_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Descompone la columna 'month' en columnas separadas de 'year' y 'month'.

    Args:
        df (pd.DataFrame): DataFrame que contiene una columna 'month' con formato 'YYYY-MM'.

    Returns:
        pd.DataFrame: DataFrame con columnas 'year' y 'month' añadidas.
    """
    df[['year', 'month']] = df['month'].str.split('-', expand=True)
    df['year'] = df['year'].astype(int)
    df['month'] = df['month'].astype(int)
    print(df.head())
    return df


def erase_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina la columna 'month' del DataFrame.

    Args:
        df (pd.DataFrame): DataFrame que contiene una columna 'month'.

    Returns:
        pd.DataFrame: DataFrame sin la columna 'month'.
    """
    df = df.drop(columns=['month'])
    print(df.head())
    print(df.columns)
    return df


def test_functions() -> None:
    """
    Prueba las funciones breakdown_date y erase_month para asegurar que funcionan correctamente.

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
        'long_gun': [30, 40]
    }
    df_test = pd.DataFrame(data)

    # Prueba de breakdown_date:
    df_broken_down = breakdown_date(df_test)
    assert 'year' in df_broken_down.columns and 'month' in df_broken_down.columns, "breakdown_date falló en añadir las columnas 'year' y 'month'."
    assert df_broken_down['year'].dtype == int and df_broken_down['month'].dtype == int, "breakdown_date falló en convertir las columnas 'year' y 'month' a enteros."

    # Prueba de erase_month:
    df_erased = erase_month(df_broken_down)
    assert 'month' not in df_erased.columns, "erase_month falló en eliminar la columna 'month'."

    print("Todas las pruebas pasaron.")


if __name__ == "__main__":
    test_functions()
