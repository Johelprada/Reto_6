def es_primo(numero):
    if numero < 2:
        return False
    
    for i in range(2, numero):
        if numero % i == 0:
            return False
    
    return True

def filtrar_primos(lista_numeros):
   
    #Recibe una lista de números y devuelve solo los que son primos
  
    numeros_primos = []
    
    for numero in lista_numeros:
        if es_primo(numero):
            numeros_primos.append(numero)
    
    return numeros_primos

# Programa principal
print("Filtrador de Números Primos")


# Permitir al usuario ingresar sus numero
print("Ingresa su lista de números:")
entrada = input("Escribe números separados por espacios: ")

try:
    lista_usuario = [int(x) for x in entrada.split()]
    primos_usuario = filtrar_primos(lista_usuario)
    print(f"Tu lista: {lista_usuario}")
    print(f"Números primos: {primos_usuario}")

except ValueError:
    print("Error: Por favor ingresa solo números enteros separados por espacios")