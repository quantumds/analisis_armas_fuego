import pandas as pd
import matplotlib.pyplot as plt


def evolucion_temporal(df: pd.DataFrame) -> None:
    """
    Grafica la evolución temporal de verificaciones de antecedentes de armas de fuego agrupadas por año.

    Args:
        df (pd.DataFrame): DataFrame que contiene las columnas 'year', 'permit', 'handgun' y 'long_gun'.

    Returns:
        None
    """
    df_anual = df.groupby('year').sum().reset_index()
    plt.ion()  # Activar el modo interactivo
    plt.figure(figsize=(10, 6))
    plt.plot(df_anual['year'], df_anual['permit'], label='Permits')
    plt.plot(df_anual['year'], df_anual['handgun'], label='Handguns')
    plt.plot(df_anual['year'], df_anual['long_gun'], label='Long guns')
    plt.xlabel('Año')
    plt.ylabel('Recuentos')
    plt.legend()
    plt.title('Evolución Temporal de Verificaciones de Antecedentes de Armas de Fuego')
    plt.show()
    plt.pause(5)  # Pausa de 5 segundos para permitir que el gráfico se enseñe


def test_evolucion_temporal() -> None:
    """
    Prueba la función evolucion_temporal para asegurar que genera un gráfico sin errores.

    Args:
        None

    Returns:
        None
    """
    # Datos de prueba:
    data = {
        'year': [2010, 2011, 2012, 2013, 2014],
        'permit': [100, 150, 200, 250, 300],
        'handgun': [50, 60, 70, 80, 90],
        'long_gun': [30, 40, 50, 60, 70]
    }
    df_test = pd.DataFrame(data)

    # Ejecución de la función con los datos de prueba:
    evolucion_temporal(df_test)


if __name__ == "__main__":
    test_evolucion_temporal()
