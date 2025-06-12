def calculadora(num1, num2, operador):
    #definir las operaciones matematicas
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        if num2 == 0:
            return "Error: División por cero"
        return num1 / num2
    else:
        return "Error: Operador no válido"
# interfas del usuario
def main():
    print("CALCULADORA BÁSICA")
    print("Operaciones disponibles:")
    print("Suma")
    print("Resta") 
    print(" Multiplicación")
    print(" División")
    
    while True:
        try:
            # Solicitar los números al usuario
            num1 = float(input("\nIngresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            
            # Solicitar la operación
            operador = input("Ingresa la operación (+, -, *, /): ").strip()
            
            # Realizar el cálculo
            resultado = calculadora(num1, num2, operador)
            
            # Mostrar el resultado
            if isinstance(resultado, str):  # Es un mensaje de error
                print(f" {resultado}")
            else:
                print(f" Resultado: {num1} {operador} {num2} = {resultado}")
            
        except ValueError:
            print(" Error: Por favor ingresa números válidos")
        except KeyboardInterrupt:
            print(" ¡Hasta luego!")
            break
        
        # Preguntar si quiere continuar
        continuar = input("\n¿Quieres hacer otra operación? (s/n): ").lower().strip()
        if continuar != 's' and continuar != 'si':
            print("¡Hasta luego!")
            break

# Ejecutar el programa
if __name__ == "__main__":
    main()