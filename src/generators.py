from typing import Iterator

def filter_by_currency(transactions, currency='USD') -> Iterator:
    """ Функция фильтрации списка по валюте"""
    result = filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions)
    return result


def transaction_descriptions(transaction_list):
    """ Функция вывода опервций транзакции """
    for transaction in [x["description"] for x in transaction_list]:
        yield transaction


def  card_number_generator(start: int, end: int) -> Iterator[str]:
    """ Функция генерации банковских карт """
    for number in range(start, end + 1):
        card_number = f"{number:016d}"
        formatted_card_number = " ".join(
            [card_number[i:i + 4] for i in range(0, 16, 4)]
        )
        yield formatted_card_number
