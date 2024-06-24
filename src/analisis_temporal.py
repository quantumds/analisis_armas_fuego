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
    plt.ion()  # Activamos el modo interactivo
    plt.figure(figsize=(10, 6))
    plt.plot(df_anual['year'], df_anual['permit'], label='Permisos')
    plt.plot(df_anual['year'], df_anual['handgun'], label='Pistolas')
    plt.plot(df_anual['year'], df_anual['long_gun'], label='Rifles de Asalto')
    plt.xlabel('Año')
    plt.ylabel('Recuentos')
    plt.legend()
    plt.title('Evolución Temporal de Verificaciones de Antecedentes de Armas de Fuego')
    plt.show()
    plt.pause(5)  # Pausa de 5 segundos para permitir que el gráfico se renderice
