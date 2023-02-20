class Car:
    """Класс базовый, для всех автомобилей"""
    def __init__(self, name: str):
        self._name = name

    @property               #так как марка авто единая, ее невозможно будет изменить и она наследуется в дочерних классах
    def name(self) -> str:
        return self._name

    def __str__(self):
        return f"Автомобиль {self._name}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r})"


class PassengerCar(Car):
    """Класс дочерний, для легковых автомобилей"""
    def __init__(self, name: str, _body: str):
        """Инициализация экземпляра класса
                :param name: единое название марки
                :param _body: кузов"""
        super().__init__(name)
        self._body = "Легковой"

    def __str__(self):
        return f"Легковой автомобиль {self._name} " #перегружаем магический метод под Легковые автомобили

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}), (body={self._body!r})" #перегружаем под класс Легковых автомобилей


class Truck(Car):
    """Класс дочерний, для грузовых автомобилей"""
    def __init__(self, name: str, _body: str):
        """Инициализация экземпляра класса
                :param name: единое название марки
                :param _body: кузов"""
        super().__init__(name)
        self._body = "Грузовой"

    def __str__(self):
        return f"Грузовой автомобиль {self._name} "

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}), (body={self._body!r})"




if __name__ == "__main__":
    # Write your solution here# нам всегда писали эти условия в лабораторных изначально, не очень понимаю, что тут надо
    pass
