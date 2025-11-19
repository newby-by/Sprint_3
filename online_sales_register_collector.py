import datetime


class OnlineSalesRegisterCollector:
    """OnlineSalesRegisterCollector class."""

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {
            'чипсы': 50, 
            'кола': 100, 
            'печенье': 45, 
            'молоко': 55, 
            'кефир': 70
        }
        self.__tax_rate = {
            'чипсы': 20, 
            'кола': 20, 
            'печенье': 20, 
            'молоко': 10, 
            'кефир': 10
        }

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items


if __name__ == "__main__":
    register_collector = OnlineSalesRegisterCollector()

    assert register_collector.name_items == []
    assert register_collector.number_items == 0
