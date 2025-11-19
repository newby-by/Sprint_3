import datetime


MIN_NUMBER_LETTERS_IN_NAME = 0
MAX_NUMBER_LETTERS_IN_NAME = 40


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

    """
    2. Добавь товар в чек
Напиши метод add_item_to_cheque. Он добавляет товары в чек.
В качестве аргумента метод принимает название товара — name.
В теле метода напиши условия:
Если в названии товара 0 или больше 40 символов, выводится исключение ValueError. 
Оно печатает сообщение: 
'Нельзя добавить товар, если в его названии нет символов или их больше 40'.
Если названия товара нет в списке item_price, выводится исключение NameError с 
текстом 'Позиция отсутствует в товарном справочнике'.
В остальных случаях метод добавляет товар в name_items 
и увеличивает значение number_items на 1.
    """

    def add_item_to_cheque(self, name):
        if not len(name) or len(name) > MAX_NUMBER_LETTERS_IN_NAME:
            raise ValueError('Нельзя добавить товар, если в его '
                             'названии нет символов или их больше 40')
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        
        self.__name_items.append(name)
        self.__number_items += 1
        


if __name__ == "__main__":
    register_collector = OnlineSalesRegisterCollector()

    assert register_collector.name_items == []
    assert register_collector.number_items == 0

    register_collector_add_crisps = OnlineSalesRegisterCollector()
    register_collector_add_crisps.add_item_to_cheque('чипсы')
    assert register_collector_add_crisps.number_items == 1
    assert register_collector_add_crisps.name_items[0] == 'чипсы'

    register_collector_add_without_name = OnlineSalesRegisterCollector()
    try:
        register_collector_add_without_name.add_item_to_cheque('')
    except Exception as e:
        assert type(e).__name__ == 'ValueError'
        assert 'Нельзя добавить товар, если в его названии нет символов или их больше 40' in str(e)

    register_collector_add_oversize_name = OnlineSalesRegisterCollector()
    try:
        register_collector_add_oversize_name.add_item_to_cheque(
            'a' * (MAX_NUMBER_LETTERS_IN_NAME + 1)
        )
    except Exception as e:
        assert type(e).__name__ == 'ValueError'
        assert 'Нельзя добавить товар, если в его названии нет символов или их больше 40' in str(e)
    
    register_collector_add_outlist_name = OnlineSalesRegisterCollector()
    try:
        register_collector_add_outlist_name.add_item_to_cheque(
            'a' * (MAX_NUMBER_LETTERS_IN_NAME - 1)
        )
    except Exception as e:
        assert type(e).__name__ == 'NameError'
        assert 'Позиция отсутствует в товарном справочнике' in str(e)
