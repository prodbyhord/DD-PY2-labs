import doctest


class Vehicle:
    """
    Класс, представляющий транспортное средство.
    """
    def __init__(self, brand: str, speed: float):
        """
        Инициализация объекта "Транспортное средство".

        :param brand: Бренд транспортного средства
        :param speed: Максимальная скорость транспортного средства в км/ч

        Примеры:
        >>> car = Vehicle("Tesla", 250.0)
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        if not brand:
            raise ValueError("Бренд не может быть пустым")
        self.brand = brand

        if not isinstance(speed, (int, float)):
            raise TypeError("Скорость должна быть числом")
        if speed <= 0:
            raise ValueError("Скорость должна быть положительным числом")
        self.speed = speed

    def accelerate(self, amount: float) -> None:
        """
        Увеличивает скорость транспортного средства.

        :param amount: Величина увеличения скорости
        :raise ValueError: Если скорость превышает максимально допустимую

        Примеры:
        >>> car = Vehicle("Tesla", 250.0)
        >>> car.accelerate(30.0)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Величина увеличения скорости должна быть числом")
        if amount < 0:
            raise ValueError("Величина увеличения скорости должна быть положительной")
        ...

    def brake(self) -> None:
        """
        Останавливает транспортное средство.

        Примеры:
        >>> car = Vehicle("Tesla", 250.0)
        >>> car.brake()
        """
        ...


class Appliance:
    """
    Класс, представляющий бытовую технику.
    """
    def __init__(self, model: str, power: float):
        """
        Инициализация объекта "Бытовая техника".

        :param model: Модель бытовой техники
        :param power: Потребляемая мощность в ваттах

        Примеры:
        >>> fridge = Appliance("LG CoolTech", 150.0)
        """
        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if not model:
            raise ValueError("Модель не может быть пустой")
        self.model = model

        if not isinstance(power, (int, float)):
            raise TypeError("Мощность должна быть числом")
        if power <= 0:
            raise ValueError("Мощность должна быть положительным числом")
        self.power = power

    def turn_on(self) -> None:
        """
        Включает бытовую технику.

        Примеры:
        >>> fridge = Appliance("LG CoolTech", 150.0)
        >>> fridge.turn_on()
        """
        ...

    def turn_off(self) -> None:
        """
        Выключает бытовую технику.

        Примеры:
        >>> fridge = Appliance("LG CoolTech", 150.0)
        >>> fridge.turn_off()
        """
        ...


class Book:
    """
    Класс, представляющий книгу.
    """
    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация объекта "Книга".

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if not title:
            raise ValueError("Название книги не может быть пустым")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть строкой")
        if not author:
            raise ValueError("Автор книги не может быть пустым")
        self.author = author

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def read(self, start_page: int, end_page: int) -> None:
        """
        Чтение книги с указанной страницы по указанную.

        :param start_page: Номер начальной страницы
        :param end_page: Номер конечной страницы
        :raise ValueError: Если указанные страницы выходят за пределы книги

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.read(10, 20)
        """
        if not (1 <= start_page <= self.pages) or not (1 <= end_page <= self.pages):
            raise ValueError("Указанные страницы выходят за пределы книги")
        if start_page > end_page:
            raise ValueError("Начальная страница не может быть больше конечной")
        ...

    def get_description(self) -> str:
        """
        Возвращает описание книги.

        :return: Строка с названием и автором

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.get_description()
        '1984 by George Orwell'
        """
        return f"{self.title} by {self.author}"


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров
