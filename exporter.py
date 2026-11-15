import pandas as pd
from datetime import datetime

def guardar_en_excel_y_csv(lista_productos, nombre_archivo="productos_monitoreados"):
    """
    Toma una lista de diccionarios con los productos extraídos
    y los exporta ordenadamente a CSV y Excel usando Pandas.
    """
    if not lista_productos:
        print("[-] No hay datos para exportar.")
        return

    # Convertimos nuestra lista de datos en un DataFrame de Pandas (como una tabla de Excel en memoria)
    df = pd.DataFrame(lista_productos)
    
    # Añadimos una marca de tiempo actual para saber cuándo se hizo el escaneo
    fecha_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    archivo_csv = f"{nombre_archivo}_{fecha_actual}.csv"
    archivo_excel = f"{nombre_archivo}_{fecha_actual}.xlsx"
    
    try:
        # Exportar a CSV (delimitado por comas)
        df.to_csv(archivo_csv, index=False, encoding='utf-8-sig')
        print(f"[+] Datos guardados con éxito en CSV: {archivo_csv}")
        
        # Exportar a Excel (.xlsx) usando openpyxl por debajo
        df.to_excel(archivo_excel, index=False, sheet_name="Precios Monitoreados")
        print(f"[+] Datos guardados con éxito en Excel: {archivo_excel}")
        
    except Exception as e:
        print(f"[-] Error al guardar los archivos: {e}")