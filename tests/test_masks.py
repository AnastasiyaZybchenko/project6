from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date


def test_get_mask_card_number():
    assert get_mask_card_number('1596837868705199') == '1596 83** **** 5199'


def test_get_mask_account():
    assert get_mask_account('35383033474447895560') == '**5560'


def test_mask_account_card():
    assert mask_account_card('Счет 64686473678894779589') == 'Счет **9589'

def test_get_date():
    pass