"""
Este módulo proporciona una función para revertir una cadena.
"""

def first_reverse(input_str):
    """
    Revierte la cadena de entrada.

    Args:
        input_str (str): La cadena que se debe revertir.

    Returns:
        str: La cadena revertida.
    """
    result = ""
    rev = reversed(list(input_str))
    for letter in rev:
        result = result + letter
    return result

if __name__ == "__main__":
    print(first_reverse('helloworld'))
