# test_monster.py
from unittest.mock import MagicMock, patch

from entities.monster import Monster


@patch("entities.monster.get_connection")
def test_save_inserta_monstruo_en_la_base_de_datos(mock_get_connection):
    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_connection.cursor.return_value = mock_cursor
    mock_get_connection.return_value = mock_connection

    monster = Monster(name="Godzilla", power=9000)

    monster.save()

    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO monster (name, power) VALUES (%s, %s)",
        ("Godzilla", 9000),
    )
    mock_connection.commit.assert_called_once()
    mock_cursor.close.assert_called_once()
    mock_connection.close.assert_called_once()