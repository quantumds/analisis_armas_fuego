import src.limpieza_datos as ld
import src.procesamiento_datos as dp
import src.agrupacion_datos as ad
import src.analisis_temporal as at
import src.analisis_estados as ae
from utilidades.ruta_git import get_git_root
from pathlib import Path


def main():

    # Definir constantes del proyecto:
    url_background_checks = str(Path(get_git_root())) + '/datos/nics-firearm-background-checks.csv'
    url_state_populations = str(Path(get_git_root())) + '/datos/us-state-populations.csv'

    # Ejercicio 1:
    print("Inicio del Ejercicio 1")
    print("")
    print("Ejercicio 1.1")
    df_background = ld.read_csv(url_background_checks)
    print(df_background.head())
    print("Ejercicio 1.2")
    df_cleaned = ld.clean_csv(df_background)
    print(df_cleaned.head())
    print("Ejercicio 1.3")
    df_renamed = ld.rename_col(df_cleaned)
    print(df_renamed.head())
    print("Fin del Ejercicio 1")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    # Ejercicio 2:
    print("Inicio del Ejercicio 2")
    print("Ejercicio 2.1.")
    df_date_breakdown = dp.breakdown_date(df_renamed)
    print(df_date_breakdown.head())
    print("Ejercicio 2.2.")
    df_no_month = dp.erase_month(df_date_breakdown)
    print(df_no_month.head())
    print("Fin del Ejercicio 2")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    # Ejercicio 3:
    print("Inicio del Ejercicio 3")
    print("Ejercicio 3.1.")
    df_grouped = ad.groupby_state_and_year(df_no_month)
    print(df_grouped.head())
    print("Ejercicio 3.2.")
    ad.print_biggest_handguns(df_grouped)
    print("Ejercicio 3.3.")
    ad.print_biggest_longguns(df_grouped)
    print("Fin del Ejercicio 3")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    # Ejercicio 4:
    print("Inicio del Ejercicio 4")
    print("Ejercicio 4.1.")
    print("Función graficada correctamente.")
    print("Ejercicio 4.2.")
    print("La correlación es clara. Las 3 series se encuentran claramente correlacionadas.")
    print("La tendencia es ascendente hasta poco después del año 2015. Después es descendente.")
    print("Desde finales del año 2019 (inicio del COVID) en adelante, la tendencia es decreciente.")
    print("Es posible que en los años siguientes haya un repunte, pero la estrategia hasta la fecha es claramente decreciente.")
    print("El panorama político en EE.UU. también es de una mayor regulación sobre la tenencia de armas. ")
    at.evolucion_temporal(df_no_month)
    print("Fin del Ejercicio 4")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    # Ejercicio 5:
    print("Inicio del Ejercicio 5")
    print("Ejercicio 5.1.")
    df_grouped_state = ae.groupby_state(df_grouped)
    print(df_grouped_state.head())
    print("Ejercicio 5.2.")
    df_clean_states = ae.clean_states(df_grouped_state)
    print(df_clean_states.head())
    df_population = ld.read_csv(url_state_populations)
    print(df_population.head())
    print("Ejercicio 5.3.")
    df_merged = ae.merge_datasets(df_clean_states, df_population)
    print(df_merged.head())
    print("Ejercicio 5.4.")
    df_relative = ae.calculate_relative_values(df_merged)
    print(df_relative.head())
    print("Ejercicio 5.5.")
    ae.analysis_kentucky(df_relative)
    print("La media cambia después de eliminar el valor atípico.")
    print("Esto demuestra como los outliers distorsionan las estadísticas y la importancia de identificarlos y tratarlos adecuadamente")
    print("La mediana es un estadístico que resiste mucho mejor a los valores atípicos. La media se afecta más.")
    print("Fin del Ejercicio 5")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    # Ejercicio 6
    # A pesar de intentarlo me fue difícil conseguir hacer este ejercicio.
    # Lo omitimos pues el paquete no logró compilar en PyCharm en ninguno de nuestros intentos.


if __name__ == "__main__":
    main()
