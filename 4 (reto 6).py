def mayor_suma_consecutivos(lista_numeros):
    """
    Encuentra la mayor suma entre dos elementos consecutivos
    """
    if len(lista_numeros) < 2:
        return "La lista debe tener al menos 2 números"
    
    mayor_suma = lista_numeros[0] + lista_numeros[1]
    
    for i in range(len(lista_numeros) - 1):
        suma_actual = lista_numeros[i] + lista_numeros[i + 1]
        if suma_actual > mayor_suma:
            mayor_suma = suma_actual
    
    return mayor_suma

# Programa principal interactivo
print("=== MAYOR SUMA DE NÚMEROS CONSECUTIVOS ===")
print("Ingresa números separados por espacios")

entrada = input("Escribe los números: ")
numeros_texto = entrada.split()

# Convertir a enteros
numeros = []
for num in numeros_texto:
    try:
        numeros.append(int(num))
    except ValueError:
        print(f"'{num}' no es un número válido, se omitirá")

print("Lista ingresada:", numeros)

# Encontrar la mayor suma
resultado = mayor_suma_consecutivos(numeros)
print("Mayor suma entre consecutivos:", resultado)

# Mostrar todas las sumas para que el usuario vea el proceso
if len(numeros) >= 2:
    print("\nTodas las sumas consecutivas:")
    for i in range(len(numeros) - 1):
        suma = numeros[i] + numeros[i + 1]
        print(f"{numeros[i]} + {numeros[i + 1]} = {suma}")
else:
    print("Necesitas al menos 2 números para hacer sumas consecutivas")