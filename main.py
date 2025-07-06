from config import PATH_JSON
from src.utils import read_json, transaction_amount


def main(path):
    """"  Основная функция запуска. """
    list_transactions = read_json(path)
    for element in list_transactions:
        if not len(element):
            continue
        print(transaction_amount(element))


if __name__ == '__main__':
    main(PATH_JSON)
