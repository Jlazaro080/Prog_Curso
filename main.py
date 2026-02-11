"""
Programa principal
"""
import time


def suma(a, b):
    """
    Realiza la suma de dos números
    """
    return a + b


def resta(a, b):
    """
    Realiza la resta de dos números
    """
    return a - b


def main():
    """
    Función principal del programa
    """
    print("Iniciando programa...")
    print("\n--- CALCULADORA ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    
    opcion = input("\nElige una opción (1, 2 o 3): ")
    
    if opcion in ["1", "2","3"]:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
       
        
        if opcion == "1":
            resultado = suma(num1, num2)
            print(f"\nResultado: {num1} + {num2} = {resultado}")
        elif opcion == "2":
            resultado = resta(num1, num2)
            print(f"\nResultado: {num1} - {num2} = {resultado}")
        elif opcion == "3":
            resultado = num1 * num2
            print(f"\nResultado: {num1} * {num2} = {resultado}")
    else:
        print("\nOpción no válida.")
    
    print("\nPrograma finalizado.")


if __name__ == "__main__":
    main()
