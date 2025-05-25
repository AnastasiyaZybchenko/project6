from datetime import datetime

from src.masks import get_mask_card_number


def mask_account_card(number_card_or_account: str) -> str:
    """Маскировка карты или счета"""
    number_card_or_account_list = number_card_or_account.split()
    if "Счет" in number_card_or_account_list or "счет" in number_card_or_account_list:
        return f"Счет **{number_card_or_account_list[-1][-4:]}"
    else:
        card_name = ' '.join(number_card_or_account_list[:-1])
        card_number = number_card_or_account_list[-1].replace(' ', '')
        return f"{card_name} {get_mask_card_number(card_number)}"


print(mask_account_card('Visa Gold 5999414228426353'))


def get_date(user_data: str) -> str:
    """Преобразование даты в формат ДД.ММ.ГГ"""
    data_obj = datetime.fromisoformat(user_data)
    formatted_data = data_obj.strftime("%d.%m.%Y")
    return formatted_data


print(get_date('2024-03-11T02:26:18.671407'))
