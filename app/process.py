import time

def almacenar_en_db(num):
    time.sleep(0.1)

def num_characters(text):
    num = len(text)
    almacenar_en_db(num)
    return num

def average_word_size(text):
    word_lengths = []
    for word in text.split():
        word_lengths.append(len(word))
    return sum(word_lengths) / len(word_lengths)

def text_analysis(text):
    result = f"Texto: {text}"
    result += "<br>"
    result += f"Texto tiene {num_characters(text)} caracteres"
    result += "<br>"
    result += f"El tamaño promedio de las palabras es {average_word_size(text)}"
    return result
