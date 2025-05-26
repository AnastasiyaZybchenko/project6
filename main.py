import src.processing
import src.masks
import src.widget

operation_list = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]
operation_list_number_card_or_account = [
    'Maestro 1596837868705199',
    'Счет 64686473678894779589',
    'MasterCard 7158300734726758',
    'Счет 35383033474447895560',
    'Visa Classic 6831982476737658',
    'Visa Platinum 8990922113665229',
    'Visa Gold 5999414228426353',
    'Счет 73654108430135874305'
]
if __name__ == '__main__':
    print(src.processing.sort_by_date(operation_list))
    print(src.processing.filter_by_state(operation_list))
    print(src.masks.get_mask_card_number(operation_list_number_card_or_account[0]))
    print(src.masks.get_mask_account(operation_list_number_card_or_account[0]))
    print(src.widget.mask_account_card(operation_list_number_card_or_account[0]))
    print(src.widget.get_date('2024-03-11T02:26:18.671407'))
