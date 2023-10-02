"""
Este módulo proporciona una función para calcular el factorial de un número.
"""

def first_factorial(num):
    """
    Calcula el factorial del número dado.

    Args:
        num (int): Número entero para calcular el factorial.

    Returns:
        int: Factorial del número dado.
    """
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

if __name__ == "__main__":
    print(first_factorial(4))
