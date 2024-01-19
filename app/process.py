"""Modulo para analisis de texto."""
import time


def almacenar_en_db(num):
    """Almacenar valor calculado en la base de datos."""
    print(num)
    time.sleep(0.1)


def num_characters(text):
    """Calcular el numero de caracteres."""
    num = len(text)
    almacenar_en_db(num)
    return num


def average_word_size(text):
    """Calcular el tamano promedio de las palabras"""
    word_lengths = []
    for word in text.split():
        word_lengths.append(len(word))
    return sum(word_lengths) / len(word_lengths)


def text_analysis(text):
    """Realizar analisis de texto."""
    result = f"Texto: {text}"
    result += "<br>"
    result += f"Texto tiene {num_characters(text)} caracteres"
    result += "<br>"
    result += "El tamaño promedio de las "
    result += f"palabras es {average_word_size(text)}"
    return result
