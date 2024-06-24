import pandas as pd


def groupby_state_and_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa el DataFrame por estado y año, y calcula la suma de cada grupo.

    Args:
        df (pd.DataFrame): DataFrame que contiene las columnas 'state' y 'year'.

    Returns:
        pd.DataFrame: DataFrame agrupado por 'state' y 'year' con las sumas calculadas.
    """
    grouped_df = df.groupby(['state', 'year']).sum().reset_index()
    return grouped_df


def print_biggest_handguns(df: pd.DataFrame) -> None:
    """
    Imprime el estado y el año con la mayor cantidad de pistolas.

    Args:
        df (pd.DataFrame): DataFrame que contiene la columna 'handgun'.

    Returns:
        None
    """
    max_row = df.loc[df['handgun'].idxmax()]
    print(f"Estado: {max_row['state']}, Año: {max_row['year']}, Pistolas: {int(max_row['handgun'])}")


def print_biggest_longguns(df: pd.DataFrame) -> None:
    """
    Imprime el estado y el año con la mayor cantidad de armas largas.

    Args:
        df (pd.DataFrame): DataFrame que contiene la columna 'long_gun'.

    Returns:
        None
    """
    max_row = df.loc[df['long_gun'].idxmax()]
    print(f"Estado: {max_row['state']}, Año: {max_row['year']}, Armas Largas: {int(max_row['long_gun'])}")
