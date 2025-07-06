import json
import logging
import os.path

from src.external_api import currency_conversion

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    "C:/Users/user/PycharmProjects/PythonProject6/logs/utils.log", encoding="utf-8", mode="w"
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(messege)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_json(path):
    """ Функция чтения файла"""
    if os.path.exists(path):
        try:
            logger.info("Открытие файла с операциями")
            with open(path, "r", encoding='utf-8') as file:
                new_file = json.load(file)
                logger.info("Запись транзакций в переменную")
        except FileNotFoundError:
            print(f"Ошибка: Файл '{file}' не найден в папке '{path}'.")
            logger.error(f"Ошибка: Файл '{file}' не найден в папке '{path}'.")
            return []
        except json.JSONDecodeError as e:
            print(f"Ошибка: Файл '{file}' не содержит валидный JSON. {e}")
            logger.error(f"Ошибка: Файл '{file}' не содержит валидный JSON. {e}")
            return []
        except Exception as e:
            print(f"Произошла ошибка при чтении файла: {e}")
            logger.error(f"Произошла ошибка при чтении файла: {e}")
            return []
    return new_file


def transaction_amount(transaction):
    """ Функция вывода суммы транзакции """
    logger.info("Проверка валюты транзакции")
    if transaction['operationAmount']['currency']['code'] == "RUB":
        return float(transaction['operationAmount']['amount'])
    else:
        logger.info("Операция вывода суммы транзакции")
        return currency_conversion(transaction['operationAmount']['amount'],
                                   transaction['operationAmount']['currency']['code'])
