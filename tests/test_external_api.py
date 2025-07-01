from unittest.mock import patch
from src.external_api import currency_conversion


@patch("requests.get")
def test_currency_conversion(mock_get):
    """ Тест обращения к API """
    mock_get.return_value.json.return_value = {"result": 1234}
    assert currency_conversion(mock_get, "o") == 1234
