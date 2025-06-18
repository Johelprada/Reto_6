# Función para verificar si dos palabras tienen los mismos caracteres
def tienen_mismos_caracteres(palabra1, palabra2):
    try:
        # Verificar que las palabras no estén vacías
        if palabra1 == "" or palabra2 == "":
            return False
        
        # Convertir a minúsculas para comparar
        palabra1 = palabra1.lower()
        palabra2 = palabra2.lower()
        
        # Si no tienen la misma longitud, no pueden tener los mismos caracteres
        if len(palabra1) != len(palabra2):
            return False
        
        # Contar caracteres en cada palabra
        for letra in palabra1:
            contador1 = 0
            contador2 = 0
            
            # Contar cuántas veces aparece la letra en la primera palabra
            for char in palabra1:
                if char == letra:
                    contador1 += 1
            
            # Contar cuántas veces aparece la letra en la segunda palabra
            for char in palabra2:
                if char == letra:
                    contador2 += 1
            
            # Si los contadores no coinciden, no son anagramas
            if contador1 != contador2:
                return False
        
        return True
    
    except Exception as error:
        print(f"Error al comparar palabras: {error}")
        return False

# Función para filtrar palabras que tienen anagramas
def filtrar_anagramas(lista_palabras):
    try:
        # Verificar que la lista no esté vacía
        if len(lista_palabras) == 0:
            print("La lista está vacía")
            return []
        
        resultado = []
        
        # Revisar cada palabra de la lista
        for i in range(len(lista_palabras)):
            try:
                palabra_actual = lista_palabras[i]
                
                # Verificar que la palabra no esté vacía
                if palabra_actual == "":
                    print("Se encontró una palabra vacía, se omite")
                    continue
                
                encontro_pareja = False
                
                # Comparar con todas las otras palabras
                for j in range(len(lista_palabras)):
                    if i != j:  # No comparar la palabra consigo misma
                        if tienen_mismos_caracteres(palabra_actual, lista_palabras[j]):
                            encontro_pareja = True
                            break
                
                # Si encontró pareja y no está ya en el resultado, agregarla
                if encontro_pareja and palabra_actual not in resultado:
                    resultado.append(palabra_actual)
            
            except Exception as error:
                print(f"Error procesando palabra en posición {i}: {error}")
                continue
        
        return resultado
    
    except Exception as error:
        print(f"Error en filtrar_anagramas: {error}")
        return []

# Programa principal
try:
    print("FILTRADOR DE ANAGRAMAS")
    print("Ingresa palabras separadas por espacios")

    # Obtener entrada del usuario
    try:
        entrada = input("Escribe las palabras: ")
        
        # Verificar que el usuario escribió algo
        if entrada == "":
            print("Error: No escribiste ninguna palabra")
            exit()
        
        # Separar las palabras
        palabras = entrada.split()
        
        # Verificar que hay al menos 2 palabras
        if len(palabras) < 2:
            print("Error: Necesitas escribir al menos 2 palabras para buscar anagramas")
            exit()
        
        print("Lista ingresada:", palabras)

    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario")
        exit()
    except Exception as error:
        print(f"Error al leer la entrada: {error}")
        exit()

    # Filtrar anagramas
    try:
        resultado = filtrar_anagramas(palabras)
        print("Palabras con los mismos caracteres:", resultado)

        # Mostrar con quien hacen pareja las palabras
        if len(resultado) > 0:
            print("\nComparaciones encontradas:")
            for palabra in resultado:
                try:
                    print(f"'{palabra}' tiene pareja:")
                    for otra_palabra in palabras:
                        if palabra != otra_palabra and tienen_mismos_caracteres(palabra, otra_palabra):
                            print(f"  - '{palabra}' y '{otra_palabra}' tienen los mismos caracteres")
                except Exception as error:
                    print(f"Error mostrando parejas de '{palabra}': {error}")
        else:
            print("No se encontraron palabras con los mismos caracteres")
    
    except Exception as error:
        print(f"Error durante el filtrado: {error}")

except Exception as error:
    print(f"Error general del programa: {error}")

print("Programa terminado")