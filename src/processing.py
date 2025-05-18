from typing import Any, Dict, List

def filter_by_state(operation_list: List[Dict[str, Any]], state: str = 'EXECUTED') -> list[Dict[str, Any]]:
    """Функция сортировки по ключу state"""
    return list((item for item in operation_list if item.get('state') == state))


def sort_by_date(operation_list: List[Dict[str, Any]], reverse: bool=False) -> list[Dict[str, Any]]:
    """Функция сортировки даты"""
    return sorted(operation_list, key=lambda item: item['date'], reverse=reverse)
