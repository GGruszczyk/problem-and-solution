def longest_word(sen):
    """
    Encuentra la palabra más larga en la cadena dada, ignorando la puntuación.

    Args:
        sen (str): Cadena de entrada.

    Returns:
        str: Palabra más larga en la cadena.
    """
    longest = ""
    longest_count = 0
    for word in sen.split():
        temp_count = 0
        for char in word:
            if char.isalpha():
                temp_count += 1
        if temp_count > longest_count:
            longest_count = temp_count
            longest = word
    return longest

# Ejemplo de uso
if __name__ == "__main__":
    input_sentence = "Hello, World! This is a test sentence."
    print(longest_word(input_sentence))
