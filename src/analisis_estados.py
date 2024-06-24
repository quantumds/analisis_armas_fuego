import pandas as pd


def groupby_state_and_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa los datos por año y estado y devuelve un DataFrame con la suma de los valores agrupados.

    Args:
        df (pd.DataFrame): DataFrame de entrada.

    Returns:
        pd.DataFrame: DataFrame agrupado por año y estado con la suma de los valores.
    """
    df_grouped: pd.DataFrame = df.groupby(['year', 'state']).sum().reset_index()
    return df_grouped


def print_biggest_handguns(df: pd.DataFrame) -> None:
    """
    Imprime el estado y el año con la mayor cantidad de armas cortas.

    Args:
        df (pd.DataFrame): DataFrame de entrada.
    """
    idx: int = df['handgun'].idxmax()
    print(f"Estado: {df.loc[idx, 'state']}, Año: {df.loc[idx, 'year']}, Pistolas: {df.loc[idx, 'handgun']}")


def print_biggest_longguns(df: pd.DataFrame) -> None:
    """
    Imprime el estado y el año con la mayor cantidad de armas largas.

    Args:
        df (pd.DataFrame): DataFrame de entrada.
    """
    idx: int = df['long_gun'].idxmax()
    print(f"Estado: {df.loc[idx, 'state']}, Año: {df.loc[idx, 'year']}, Armas Largas: {df.loc[idx, 'long_gun']}")


def groupby_state(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa los datos por estado y devuelve un DataFrame con la suma de los valores agrupados.

    Args:
        df (pd.DataFrame): DataFrame de entrada.

    Returns:
        pd.DataFrame: DataFrame agrupado por estado con la suma de los valores.
    """
    df_grouped: pd.DataFrame = df.groupby(['state']).sum().reset_index()
    print(df_grouped.head())
    return df_grouped


def clean_states(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina los estados especificados del DataFrame y devuelve el DataFrame limpio.

    Args:
        df (pd.DataFrame): DataFrame de entrada.

    Returns:
        pd.DataFrame: DataFrame limpio sin los estados especificados.
    """
    states_to_remove: list[str] = ['Guam', 'Mariana Islands', 'Puerto Rico', 'Virgin Islands']
    df_cleaned: pd.DataFrame = df[~df['state'].isin(states_to_remove)]
    print(len(df_cleaned['state'].unique()))
    return df_cleaned


def merge_datasets(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    Combina dos DataFrames en uno solo basándose en la columna 'state'.

    Args:
        df1 (pd.DataFrame): Primer DataFrame.
        df2 (pd.DataFrame): Segundo DataFrame.

    Returns:
        pd.DataFrame: DataFrame combinado.
    """
    df_merged: pd.DataFrame = pd.merge(df1, df2, on='state')
    print(df_merged.head())
    return df_merged


def calculate_relative_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula los valores relativos de permisos, armas largas y armas cortas por población de 2014 y
    añade estas columnas al DataFrame.

    Args:
        df (pd.DataFrame): DataFrame de entrada.

    Returns:
        pd.DataFrame: DataFrame con los valores relativos añadidos.
    """
    df['permit_perc'] = (df['permit'] * 100) / df['pop_2014']
    df['longgun_perc'] = (df['long_gun'] * 100) / df['pop_2014']
    df['handgun_perc'] = (df['handgun'] * 100) / df['pop_2014']
    return df


def analysis_kentucky(df: pd.DataFrame) -> None:
    """
    Realiza un análisis de los datos del estado de Kentucky y ajusta los valores de permisos.

    Args:
        df (pd.DataFrame): DataFrame de entrada.
    """
    mean_permit_perc: float = round(df['permit_perc'].mean(), 2)
    print(f"Porcentaje medio de permisos: {mean_permit_perc}")

    kentucky_info: pd.DataFrame = df[df['state'] == 'Kentucky']
    print(kentucky_info)

    df.loc[df['state'] == 'Kentucky', 'permit_perc'] = mean_permit_perc
    new_mean_permit_perc: float = round(df['permit_perc'].mean(), 2)
    print(f"Nuevo porcentaje medio de permisos: {new_mean_permit_perc}")

    if mean_permit_perc != new_mean_permit_perc:
        print("Eliminar los valores atípicos puede cambiar significativamente las métricas estadísticas.")
