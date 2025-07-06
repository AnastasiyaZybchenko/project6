import json
import os.path

from src.external_api import currency_conversion


def read_json(path):
    """ Функция чтения файла"""
    if os.path.exists(path):
        with open(path, "r", encoding='utf-8') as file:
            new_file = json.load(file)
            if isinstance(new_file, dict):
                print("Неверный тип файла")
                return []
            if not len(new_file):
                return []
    return new_file


def transaction_amount(transaction):
    """ Функция вывода суммы транзакции """
    if transaction['operationAmount']['currency']['code'] == "RUB":
        return float(transaction['operationAmount']['amount'])
    else:
        return currency_conversion(transaction['operationAmount']['amount'],
                                   transaction['operationAmount']['currency']['code'])
