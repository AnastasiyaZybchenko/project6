import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency_incorrect_currency(transactions_for_test):
    filtered = filter_by_currency(transactions_for_test, 'EUR')
    with pytest.raises(StopIteration):
        next(filtered)


@pytest.mark.usefixtures("transactions")
def test_transaction_descriptions(transactions):
    generator = transaction_descriptions(transactions)
    assert next(generator) == 'Перевод организации'
    assert next(generator) == 'Перевод со счета на счет'
    assert next(generator) == 'Перевод со счета на счет'


@pytest.mark.parametrize(
    "start, end, result",
    [
        (1, 5, "0000 0000 0000 0001"),
        (10, 12, "0000 0000 0000 0010"),
    ]
)
def test_card_number_generator(start, end, result):
    gen = card_number_generator(start, end)
    assert next(gen) == result
