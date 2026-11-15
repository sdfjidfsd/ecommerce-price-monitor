import requests
from bs4 import BeautifulSoup

def extraer_libros(url="http://books.toscrape.com/"):
    """
    Se conecta a la URL indicada y extrae el título y el precio 
    de los productos de la página.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "es-ES,es;q=0.9"
    }
    
    try:
        print(f"[*] Conectando con la URL: {url}...")
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            print("[+] ¡Conexión exitosa! Analizando HTML...")
            soup = BeautifulSoup(response.text, 'html.parser')
            
            lista_datos = []
            
            # En 'Books to Scrape', cada libro está dentro de una etiqueta <article class="product_pod">
            productos = soup.find_all('article', class_='product_pod')
            
            for producto in productos:
                titulo = producto.h3.a['title']
                precio_texto = producto.find('p', class_='price_color').text
                
                # Limpiamos el precio eliminando símbolos de moneda y caracteres extraños
                precio_limpio = precio_texto.replace('£', '').replace('Â', '').strip()
                
                lista_datos.append({
                    "Título del Producto": titulo,
                    "Precio (£)": float(precio_limpio),
                    "Disponibilidad": "En Stock"
                })
                
            print(f"[+] Se extrajeron {len(lista_datos)} productos exitosamente.")
            return lista_datos
        else:
            print(f"[-] Error: El servidor respondió con el código {response.status_code}")
            return []
            
    except Exception as e:
        print(f"[-] Ocurrió un error durante el scraping: {e}")
        return []