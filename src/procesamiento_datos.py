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
