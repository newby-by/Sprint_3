import datetime


MIN_NUMBER_LETTERS_IN_NAME = 0
MAX_NUMBER_LETTERS_IN_NAME = 40
NUMBER_ITEMS_IN_CART_WITH_DISCOUNT = 10
DISCOUNT = 0.9

VAT_TAX = 20
PERCENT_100 = 100


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

    def add_item_to_cheque(self, name):
        if not len(name) or len(name) > MAX_NUMBER_LETTERS_IN_NAME:
            raise ValueError('Нельзя добавить товар, если в его '
                             'названии нет символов или их больше 40')
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        
        self.__name_items.append(name)
        self.__number_items += 1

    def check_amount(self):
        total = sum([self.__item_price.get(item, 0) for item in self.__name_items])

        return (total * DISCOUNT 
                if self.__number_items > NUMBER_ITEMS_IN_CART_WITH_DISCOUNT 
                else total)

    def twenty_percent_tax_calculation(self):
        """Calculate VAT for goods with a rate of 20 percent."""

        twenty_percent_tax = [item for item in self.__name_items 
                              if self.__tax_rate.get(item, 0) == VAT_TAX]
        total = sum([self.__item_price.get(item, 0) for item in twenty_percent_tax])
        total_with_discount =  (total * DISCOUNT 
                                if (self.__number_items > 
                                    NUMBER_ITEMS_IN_CART_WITH_DISCOUNT )
                                else total)

        return total_with_discount * VAT_TAX / PERCENT_100


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


    # tests check_amount
    register_collector_total_with_2_items = OnlineSalesRegisterCollector()
    register_collector_total_with_2_items.add_item_to_cheque('чипсы') # 50
    register_collector_total_with_2_items.add_item_to_cheque('кола') # 100
    actual_total = register_collector_total_with_2_items.check_amount()
    assert actual_total == (50 + 100)

    register_collector_total_with_0_items = OnlineSalesRegisterCollector()
    actual_total = register_collector_total_with_0_items.check_amount()
    assert actual_total == 0, f'{actual_total}'

    register_collector_total_with_11_items = OnlineSalesRegisterCollector()
    [register_collector_total_with_11_items.add_item_to_cheque('чипсы') 
     for i in range(11)] # 50
    actual_total = register_collector_total_with_11_items.check_amount()
    assert actual_total == (50 * 11) * DISCOUNT, f'{actual_total}'

    # tests twenty_percent_tax_calculation
    register_collector_total_with_2_items_with_20 = OnlineSalesRegisterCollector()
    register_collector_total_with_2_items_with_20.add_item_to_cheque('чипсы') # 50 20%
    register_collector_total_with_2_items_with_20.add_item_to_cheque('кола') # 100 20%
    register_collector_total_with_2_items_with_20.add_item_to_cheque('кефир') # 70 10%
    actual_total = register_collector_total_with_2_items_with_20.twenty_percent_tax_calculation()
    assert actual_total == (50 + 100) * VAT_TAX / PERCENT_100

    register_collector_total_with_2_items_with_20 = OnlineSalesRegisterCollector()
    register_collector_total_with_2_items_with_20.add_item_to_cheque('кефир') # 70 10%
    register_collector_total_with_2_items_with_20.add_item_to_cheque('кефир') # 70 10%
    actual_total = register_collector_total_with_2_items_with_20.twenty_percent_tax_calculation()
    assert actual_total == 0

    register_collector_total_with_11_items_with_20 = OnlineSalesRegisterCollector()
    [register_collector_total_with_11_items_with_20.add_item_to_cheque('чипсы') 
     for i in range(11)] # 50
    actual_total = register_collector_total_with_11_items_with_20.twenty_percent_tax_calculation()
    assert actual_total == (50 * 11) * DISCOUNT * VAT_TAX / PERCENT_100, f'{actual_total}'

