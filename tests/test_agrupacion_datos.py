import pandas as pd
import pytest


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
    print(f"State: {max_row['state']}, Year: {max_row['year']}, Handguns: {max_row['handgun']}")


def print_biggest_longguns(df: pd.DataFrame) -> None:
    """
    Imprime el estado y el año con la mayor cantidad de armas largas.

    Args:
        df (pd.DataFrame): DataFrame que contiene la columna 'long_gun'.

    Returns:
        None
    """
    max_row = df.loc[df['long_gun'].idxmax()]
    print(f"State: {max_row['state']}, Year: {max_row['year']}, Long guns: {max_row['long_gun']}")


def test_groupby_state_and_year() -> None:
    """
    Prueba la función groupby_state_and_year.

    Args:
        None

    Returns:
        None
    """
    data = {
        'state': ['CA', 'CA', 'NV', 'NV'],
        'year': [2020, 2021, 2020, 2021],
        'handgun': [100, 150, 200, 250],
        'long_gun': [50, 75, 125, 175]
    }
    df = pd.DataFrame(data)
    expected_data = {
        'state': ['CA', 'CA', 'NV', 'NV'],
        'year': [2020, 2021, 2020, 2021],
        'handgun': [100, 150, 200, 250],
        'long_gun': [50, 75, 125, 175]
    }
    expected_df = pd.DataFrame(expected_data)
    result_df = groupby_state_and_year(df)
    pd.testing.assert_frame_equal(result_df, expected_df)


def test_print_biggest_handguns(capfd) -> None:
    """
    Prueba la función print_biggest_handguns.

    Args:
        capfd: Captura la salida impresa por la función.

    Returns:
        None
    """
    data = {
        'state': ['CA', 'NV', 'TX'],
        'year': [2020, 2021, 2020],
        'handgun': [100, 200, 150]
    }
    df = pd.DataFrame(data)
    print_biggest_handguns(df)
    captured = capfd.readouterr()
    assert captured.out == "State: NV, Year: 2021, Handguns: 200\n"


def test_print_biggest_longguns(capfd) -> None:
    """
    Prueba la función print_biggest_longguns.

    Args:
        capfd: Captura la salida impresa por la función.

    Returns:
        None
    """
    data = {
        'state': ['CA', 'NV', 'TX'],
        'year': [2020, 2021, 2020],
        'long_gun': [50, 125, 175]
    }
    df = pd.DataFrame(data)
    print_biggest_longguns(df)
    captured = capfd.readouterr()
    assert captured.out == "State: TX, Year: 2020, Long guns: 175\n"


if __name__ == "__main__":
    pytest.main()
