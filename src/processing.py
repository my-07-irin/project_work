def filter_by_state(spis_input: list[dict], key_input: str = "EXECUTED") -> list[dict]:
    """формирование нового списка словарей по заданному значению ключа state"""

    filter_spis = [str_from_spis for str_from_spis in spis_input if str_from_spis["state"] == key_input]
    return filter_spis


def sort_by_date(spis_input: list[dict], reverse_input: bool = True) -> list[dict]:
    """сортировка списка справочников по ключу date"""

    sort_spis = sorted(spis_input, key=lambda str_from_spis: str_from_spis["date"], reverse=reverse_input)
    return sort_spis


# if __name__ == '__main__':
#     spis_bank_operation = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#     ]
#
#     print(filter_by_state(spis_bank_operation))
#
#     print(sort_by_date(spis_bank_operation))
