import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    "C:/Users/user/PycharmProjects/PythonProject6/logs/masks.log", encoding="utf-8", mode="w"
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки банковской карты"""

    card_number = card_number.replace(" ", "")
    if len(card_number) != 16:
        logger.info("Проверка ввода формата карты")
        return "Введен неверный номер карты"

    result = []
    counter = 0

    logger.info("Начало операции маскировки карты")
    for number in card_number:
        counter += 1
        if 6 < counter <= len(card_number) - 4:
            result.append("*")
        else:
            result.append(number)

    masked_card = "".join(result)

    masked_card_result = []

    for i in range(0, len(masked_card), 4):
        masked_card_result.append(masked_card[i: i + 4])

    masked_card_result_with_space = " ".join(masked_card_result)

    return masked_card_result_with_space


def get_mask_account(card_account: str) -> str:
    """Функция маскировки банковского счета"""
    card_account = card_account.replace(" ", "")

    logger.info("Начало операции маскировки счета")
    last_part = str(card_account[-4:])
    return f"**{last_part}"
