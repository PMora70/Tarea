import re


regex_coincidencias = {
    "numero_telefono": r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b",  
    "cumpleaños": r"\b\d{2}/\d{2}/\d{4}\b|\b\d{4}-\d{2}-\d{2}\b",  
    "contraseña": r"\b[a-zA-Z0-9]{8}\b",  
    "sitio_web": r"https?://[^\s]+",  
    "numero_tarjeta": r"\b(?:\d[ -]*?){13,16}\b", 
}


def buscar_en_texto(texto):
   
    for tipo, patron in regex_coincidencias.items():
        coincidencias = re.findall(patron, texto)
        print(f"{tipo} encontrados: {coincidencias}")

texto_de_ejemplo = """
Número de teléfono: 123-456-7890
Cumpleaños: 20/12/1979
Contraseña: abcd1234, 
Tarjeta de crédito: 1234 5678 9012 3456.
sitio web:  https://www.ejemplo.com 
"""

buscar_en_texto(texto_de_ejemplo)



