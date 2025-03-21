def contarPalabras(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            texto = f.read()
        palabras = texto.split()
        return len(palabras)
    except FileNotFoundError:
        print("Error: El archivo no fue encontrado.")
        return 0

archivo = "ejemplo.txt"  # Ruta del archivo de texto a analizar
cantidadPalabras = contarPalabras(archivo)
print(f"El archivo: {archivo} tiene {cantidadPalabras} palabras.")
