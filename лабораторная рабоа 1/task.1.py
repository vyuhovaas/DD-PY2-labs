import doctest


class Coffemaker:
    """Класс описывает некоторые характеристики и содержимое кофеварки"""
    def __init__(self, number_of_filters_:int, capacity_volume: float, temp: int):# TODO Написать 3 класса с документацией и аннотацией типов
        """Инициализация экземпляра класса
        :param number_of_filters_: количество фильтров в кофеварке
        :param capacity_volume: объем кофеварки
        :param temp: температура нагревания кофеварки
        """
        self.filter = number_of_filters_
        self.capacity_volume = capacity_volume
        self.temp = temp
        ...

    def check_filter(self):
        """ Проверка наличия фильтра в кофварке"""
        ...

    def get_temp(self):
        """ Метод помогает получить температуру"""
        ...

    def is_empty_maker(self):
        """ Метод проверяет пустая ли кофеварка"""
        ...


class Phone:
    """Класс описывает телефон"""
    def __init__(self, color: str, max_charge: int):
        """ Инициализация экземпляра класса
        :param color: цвет устройства
        :param max_charge: максимальный заряд устройства
        """
        self.color = color
        self.max_charge = max_charge
        ...

    def turn_on_the_phone(self, charge: int) -> None:
        """
        Метод проверяет возможность включения телефона

        Примеры
        >>> phone = Phone("белый", 0)"""
        if not isinstance(charge, int):
            raise TypeError("Заряд телефона должен быть типа int")
        if charge <= 0:
            raise ValueError("Заряд телефона должен быть положительным числом, иначе телефон невозможно включить")
        ...

    def look_color_phone(self):
        """
        Метод указывает на то что можно узнать цвет телефона
        :return: Цвет телефона
        """
        ...


class Coursework:
    """Класс рассматривает курсовую работу"""
    def __init__(self, author: str, pages: int):
        """
        Инициализация параметров класса
        :param author: указывает автора работы
        :param pages: показывает количество страниц в работе
        """
        self.author = author
        self.pages = pages
        ...

    def read(self):
        """Чтение работы"""
        ...

    def change_the_work(self, text: str) -> None:
        """
        Изменение текста работы
        :param text: текст курсовой работы
        :raise ValueError: Если данная работа не содержит текста, то выводим ошибку
        """
        if not isinstance(text, str):
            raise TypeError("Данная работа должна быть типа str")
        if len(text) == 0:
            raise ValueError("Данная работа не может быть изменена. Вы можете начать её с самого начала")
        ...


if __name__ == "__main__":
    doctest.testmod()# TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
