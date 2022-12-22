import doctest


class CoffeMaker:
    """Класс описывает некоторые характеристики и содержимое кофеварки"""
    def __init__(self, number_of_filters: int, capacity_volume: float, temperature: int):# TODO Написать 3 класса с документацией и аннотацией типов
        """Инициализация экземпляра класса
        :param number_of_filters: количество фильтров в кофеварке
        :param capacity_volume: объем кофеварки
        :param temperature: температура нагревания кофеварки
        """
        self.number_of_filter = number_of_filters
        self.capacity_volume = capacity_volume
        self.temperature = temperature
        ...

    def check_filter(self, number_of_filters: int):
        """ Проверка наличия фильтра в кофварке
        :param number_of_filters: количество фильтров в кофеварке
        """
        ...

    def get_temperature(self, temperature: int):
        """ Метод помогает получить нужную для варки кофе температуру
         :param temperature: температура нагревания кофеварки
         """
        ...

    def is_empty(self, ):
        """ Метод проверяет пустая ли кофеварка
        :param capacity_volume: объем кофеварки
        """
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

    def is_able_to_turn_on(self, charge: int) -> None:
        """
        Метод проверяет возможность включения телефона

        Примеры
        >>> phone = Phone("белый", 0)"""
        if not isinstance(charge, int):
            raise TypeError("Заряд телефона должен быть типа int")
        if charge <= 0:
            raise ValueError("Заряд телефона должен быть положительным числом, иначе телефон невозможно включить")
        ...

    def look_color_phone(self, color: str):
        """
        Метод указывает на цвет телефона
        :param color: цвет устройства
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

    def adjust_work(self, adjustments: str) -> None:
        """
        Изменение текста работы
        :param adjustments: текст курсовой работы
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
