"""Pruebas para el modulo process.py."""
from unittest.mock import patch

import pytest

from app.process import num_characters, average_word_size, text_analysis


@pytest.mark.parametrize(
    "text,expected",
    [
        ("texto de prueba", 15),
        ("prueba", 6),
        ("", 0),
        ("a e i o u", 9),
        ("dos palabras", 12),
    ]
)
def test_num_characters(text, expected):
    """Prueba para la funcion num_characters."""
    with patch("app.process.almacenar_en_db") as mock_db:
        assert num_characters(text) == expected
        mock_db.assert_called_once_with(expected)


def test_average_word_size():
    """Prueba para la funcion average_word_size."""
    assert average_word_size("texto ejemplo") == 6.0


def test_average_word_size_empty():
    """Prueba para la funcion average_word_size con texto vacio."""
    with pytest.raises(ZeroDivisionError):
        average_word_size("")


def test_text_analysis():
    """Prueba para la funcion text_analysis."""
    with patch("app.process.almacenar_en_db"):
        assert text_analysis("texto ejemplo") == (
            "Texto: texto ejemplo"
            "<br>"
            "Texto tiene 13 caracteres"
            "<br>"
            "El tamaño promedio de las palabras es 6.0"
        )
