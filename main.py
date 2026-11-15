from scraper import extraer_libros
from exporter import guardar_en_excel_y_csv

def main():
    print("==========================================")
    print("   INICIANDO MONITOR DE PRECIOS (BOT)     ")
    print("==========================================")
    
    # 1. Ejecutamos el scraper para obtener los datos
    productos = extraer_libros()
    
    # 2. Si encontramos datos, los mandamos a exportar
    if productos:
        print("\n[*] Exportando datos a Excel y CSV...")
        guardar_en_excel_y_csv(productos, nombre_archivo="catalogo_libros")
        print("\n[✔] ¡Proceso completado con éxito!")
    else:
        print("\n[-] No se pudieron obtener datos para exportar.")

if __name__ == "__main__":
    main()