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


def get_date(user_data: str) -> str:
    """Преобразование даты в формат ДД.ММ.ГГ"""
    data_obj = datetime.fromisoformat(user_data)
    formatted_data = data_obj.strftime("%d.%m.%Y")
    return formatted_data
