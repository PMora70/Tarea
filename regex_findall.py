import re


regex_patterns = {
    "numero_telefono": r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b",
    "cumpleaños": r"\b\d{2}/\d{2}/\d{4}\b|\b\d{4}-\d{2}-\d{2}\b",  
    "contraseña_8_caracteres": r"\b[a-zA-Z0-9]{8}\b",  
    "sitio_web": r"https://[^\s]+",  
    "numero_tarjeta": r"\b(?:\d[ -]*?){13,16}\b",  
}

def buscar_en_texto(texto):
    try:
        for tipo, patron in regex_patterns.items():
            try:
                coincidencias = re.findall(patron, texto)
                if coincidencias:
                    print(f"{tipo} encontrados: {coincidencias}")
                else:
                    print(f"{tipo}: No se encontraron coincidencias.")
            except re.error as e:
                print(f"Error en la expresión regular para {tipo}: {e}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


ejemplos = """
Numero de telefono: 123-456-7890 
Cumpleaños: 05/12/1999
Contraseña: ad203040
Tarjeta de crédito: 1234 5678 9012 3456.
Sitio web: https://www.sitioweb.com 
"""

buscar_en_texto(ejemplos)




