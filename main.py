from config import PATH_JSON
from src.masks import get_mask_account, get_mask_card_number
from src.utils import read_json, transaction_amount


def main(path):
    """"  Основная функция запуска. """
    list_transactions = read_json(path)
    for element in list_transactions:
        if not len(element):
            continue
        print(transaction_amount(element))

    get_mask_card_number("1234567891234567")
    get_mask_account("12345678912345678912")
    read_json(PATH_JSON)

if __name__ == '__main__':
    main(PATH_JSON)
#
# from config import PATH_JSON
# from src.utils import read_json, transaction_amount
# from src.masks import get_mask_card_number, get_mask_account
#
#
# def main(path):
#     """"  Основная функция запуска. """
#     list_transactions = read_json(path)
#     for element in list_transactions:
#         if not len(element):
#             continue
#         print(transaction_amount(element))
#
#     get_mask_card_number("1234567891234567")
#     get_mask_account("12345678912345678912")


# if __name__ == '__main__':
#     main(PATH_JSON)