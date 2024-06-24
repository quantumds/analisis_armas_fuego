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
    print(f"State: {df.loc[idx, 'state']}, Year: {df.loc[idx, 'year']}, Handguns: {df.loc[idx, 'handgun']}")


def print_biggest_longguns(df: pd.DataFrame) -> None:
    """
    Imprime el estado y el año con la mayor cantidad de armas largas.

    Args:
        df (pd.DataFrame): DataFrame de entrada.
    """
    idx: int = df['long_gun'].idxmax()
    print(f"State: {df.loc[idx, 'state']}, Year: {df.loc[idx, 'year']}, Long Guns: {df.loc[idx, 'long_gun']}")


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
    print(f"Mean permit percentage: {mean_permit_perc}")

    kentucky_info: pd.DataFrame = df[df['state'] == 'Kentucky']
    print(kentucky_info)

    df.loc[df['state'] == 'Kentucky', 'permit_perc'] = mean_permit_perc
    new_mean_permit_perc: float = round(df['permit_perc'].mean(), 2)
    print(f"New mean permit percentage: {new_mean_permit_perc}")

    if mean_permit_perc != new_mean_permit_perc:
        print("Removing outliers can significantly change statistical metrics.")


def test_functions() -> None:
    """
    Prueba las funciones del módulo para asegurar que funcionan correctamente.

    Args:
        None

    Returns:
        None
    """
    # Datos de prueba:
    data = {
        'year': [2010, 2011, 2011, 2010],
        'state': ['CA', 'CA', 'NY', 'NY'],
        'permit': [100, 150, 200, 250],
        'handgun': [50, 60, 70, 80],
        'long_gun': [30, 40, 50, 60],
        'pop_2014': [1000, 1000, 2000, 2000]
    }
    df_test = pd.DataFrame(data)

    # Prueba de groupby_state_and_year:
    df_grouped_state_year = groupby_state_and_year(df_test)
    assert 'year' in df_grouped_state_year.columns and 'state' in df_grouped_state_year.columns, "groupby_state_and_year falló."

    # Prueba de print_biggest_handguns:
    print_biggest_handguns(df_test)

    # Prueba de print_biggest_longguns:
    print_biggest_longguns(df_test)

    # Prueba de groupby_state:
    df_grouped_state = groupby_state(df_test)
    assert 'state' in df_grouped_state.columns, "groupby_state falló."

    # Prueba de clean_states:
    df_cleaned_states = clean_states(df_test)
    assert not df_cleaned_states['state'].isin(['Guam', 'Mariana Islands', 'Puerto Rico', 'Virgin Islands']).any(), "clean_states falló."

    # Prueba de merge_datasets:
    df_merged = merge_datasets(df_grouped_state, df_cleaned_states)
    assert 'state' in df_merged.columns, "merge_datasets falló."

    # Prueba de calculate_relative_values:
    df_relative_values = calculate_relative_values(df_test)
    assert 'permit_perc' in df_relative_values.columns and 'longgun_perc' in df_relative_values.columns and 'handgun_perc' in df_relative_values.columns, "calculate_relative_values falló."

    # Prueba de analysis_kentucky:
    analysis_kentucky(df_relative_values)

    print("Todas las pruebas pasaron.")


if __name__ == "__main__":
    test_functions()
