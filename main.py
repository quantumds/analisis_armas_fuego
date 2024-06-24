import src.limpieza_datos as ld
import src.procesamiento_datos as dp
import src.agrupacion_datos as ad
import src.analisis_temporal as at
import src.analisis_estados as ae


def main():
    # Definir constantes del proyecto:
    url_background_checks = '/Users/anibalmartinez-sistac/Documents/anibal/git/analisis_armas_fuego/datos/nics-firearm-background-checks.csv'
    url_state_populations = '/Users/anibalmartinez-sistac/Documents/anibal/git/analisis_armas_fuego/datos/us-state-populations.csv'

    # Ejercicio 1:
    print("Inicio del Ejercicio 1")
    df_background = ld.read_csv(url_background_checks)
    df_cleaned = ld.clean_csv(df_background)
    df_renamed = ld.rename_col(df_cleaned)
    print("Fin del Ejercicio 1")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    # Ejercicio 2:
    print("Inicio del Ejercicio 2")
    df_date_breakdown = dp.breakdown_date(df_renamed)
    df_no_month = dp.erase_month(df_date_breakdown)
    print("Fin del Ejercicio 2")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    # Ejercicio 3:
    print("Inicio del Ejercicio 3")
    df_grouped = ad.groupby_state_and_year(df_no_month)
    ad.print_biggest_handguns(df_grouped)
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
    df_grouped_state = ae.groupby_state(df_grouped)
    df_clean_states = ae.clean_states(df_grouped_state)
    df_population = ld.read_csv(url_state_populations)
    df_merged = ae.merge_datasets(df_clean_states, df_population)
    df_relative = ae.calculate_relative_values(df_merged)
    ae.analysis_kentucky(df_relative)
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
