import datetime


MIN_NUMBER_LETTERS_IN_NAME = 0
MAX_NUMBER_LETTERS_IN_NAME = 40
NUMBER_ITEMS_IN_CART_WITH_DISCOUNT = 10
DISCOUNT = 0.9

VAT_TAX_20 = 20
VAT_TAX_10 = 10
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

    @staticmethod
    def get_telephone_number(telephone_number):
        """Check a telephone number.
        
        Raises:
            ValueError: The telephone number is not integer.
            ValueError: The length of telephone number is not 10.

        Returns:
            str: full telephone number, e.g. +71234567890
        """
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
        
        if len(str(telephone_number)) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        
        return f'+7{telephone_number}'
    
    @staticmethod
    def get_date_and_time():
        """Split of current date into a list. 

        Returns:
            list: list of splitted of current date, 
            e.g. ['часы: 13', 'минуты: 31', 'день: 10', 'месяц: 7', 'год: 2023']
        """

        now = datetime.datetime.now()
        date = [
            ['часы', lambda td: td.hour],
            ['минуты', lambda td: td.minute],
            ['день', lambda td: td.day],
            ['месяц', lambda td: td.month],
            ['год', lambda td: td.year],
        ]

        return [f'{t_name}: {fun(now)}' for (t_name, fun) in date]

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

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        self.__name_items.remove(name)
        self.__number_items -= 1

    def check_amount(self):
        total = sum([self.__item_price.get(item, 0) for item in self.__name_items])

        return (total * DISCOUNT 
                if self.__number_items > NUMBER_ITEMS_IN_CART_WITH_DISCOUNT 
                else total)

    def twenty_percent_tax_calculation(self):
        """Calculate VAT for goods with a rate of 20 percent."""

        twenty_percent_tax = [item for item in self.__name_items 
                              if self.__tax_rate.get(item, 0) == VAT_TAX_20]
        total = sum([self.__item_price.get(item, 0) for item in twenty_percent_tax])
        total_with_discount =  (total * DISCOUNT 
                                if (self.__number_items > 
                                    NUMBER_ITEMS_IN_CART_WITH_DISCOUNT )
                                else total)

        return total_with_discount * VAT_TAX_20 / PERCENT_100

    def ten_percent_tax_calculation(self):
        """Calculate VAT for goods with a rate of 10 percent."""

        ten_percent_tax = [item for item in self.__name_items 
                                if self.__tax_rate.get(item, 0) == VAT_TAX_10]
        total = sum([self.__item_price.get(item, 0) for item in ten_percent_tax])
        total_with_discount =  (total * DISCOUNT 
                                if (self.__number_items > 
                                    NUMBER_ITEMS_IN_CART_WITH_DISCOUNT )
                                else total)

        return total_with_discount * VAT_TAX_10 / PERCENT_100

    def total_tax(self):
        """Total amount of taxes."""
        
        return (self.twenty_percent_tax_calculation() + 
                self.ten_percent_tax_calculation())
