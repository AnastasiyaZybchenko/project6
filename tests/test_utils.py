import json

from config import TEST_DATA
from src.utils import read_json, transaction_amount

path = TEST_DATA


def test_read_json():
    """ Тест чтения фацла """
    with open(path, "r", encoding='utf-8') as file:
        new_file = json.load(file)
        assert read_json(path) == [{'Hello': 'world'}]


def test_transaction_amount(amount_for_test):
    """ Тест возврата суммы транзакции """
    assert transaction_amount(amount_for_test) == 31957.58
