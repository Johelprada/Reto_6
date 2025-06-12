def es_palindromo(palabra):
    """
    Valida si una palabra es un palíndromo
    """
    palabra = palabra.lower()
    longitud = len(palabra)
    
    for i in range(longitud // 2):
        if palabra[i] != palabra[longitud - 1 - i]:
            return False
    
    return True

# Programa principal
print("Validador de Palíndromos")

try:
    palabra = input("Ingresa una palabra: ")
    
    if palabra.strip() == "":
        print("Error: Debes ingresar una palabra")
    else:
        if palabra.strip() == int:
                print("Error: Debes ingresar una palabra")
        else:
            if es_palindromo(palabra):
                print("Es un palíndromo")
            else:
                print("No es un palíndromo")

except KeyboardInterrupt:
    print("\n¡Hasta luego!")
except Exception as e:
    print(f"Error inesperado: {e}")

# Ejemplos de prueba
print("\nEjemplos:")
print("radar ->", es_palindromo("radar"))
print("casa ->", es_palindromo("casa"))
print("oso ->", es_palindromo("oso"))