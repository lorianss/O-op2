class Pair:
    def __init__(self, first: float, second: int):
        """
        Инициализация объекта Pair.
        :param first: дробное число (float).
        :param second: целое число (int), показатель степени.
        """
        if not isinstance(first, (float, int)):
            raise ValueError("Поле 'first' должно быть дробным числом.")
        if not isinstance(second, int):
            raise ValueError("Поле 'second' должно быть целым числом.")

        self.first = float(first)  # Преобразуем в float для единообразия
        self.second = second

    def power(self):
        """
        Возведение числа first в степень second.
        :return: результат возведения в степень.
        """
        return self.first ** self.second

    def read(self):
        """
        Ввод значений полей с клавиатуры.
        """
        try:
            self.first = float(input("Введите дробное число (first): "))
            self.second = int(input("Введите целое число (second): "))
        except ValueError:
            print("Ошибка ввода. Проверьте, что введены корректные значения.")
            raise

    def display(self):
        """
        Вывод значений полей на экран.
        """
        print(f"Pair(first={self.first}, second={self.second})")

    # Перегрузка оператора возведения в степень (**)
    def __pow__(self, other):
        if isinstance(other, Pair):
            return self.power() ** other.power()
        elif isinstance(other, (int, float)):
            return self.power() ** other
        else:
            raise TypeError("Операнд должен быть числом или объектом класса Pair.")

    # Перегрузка операторов сравнения
    def __eq__(self, other):
        if isinstance(other, Pair):
            return self.power() == other.power()
        elif isinstance(other, (int, float)):
            return self.power() == other
        else:
            raise TypeError("Операнд должен быть числом или объектом класса Pair.")

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Pair):
            return self.power() < other.power()
        elif isinstance(other, (int, float)):
            return self.power() < other
        else:
            raise TypeError("Операнд должен быть числом или объектом класса Pair.")

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    # Перегрузка арифметических операторов
    def __add__(self, other):
        if isinstance(other, Pair):
            return self.power() + other.power()
        elif isinstance(other, (int, float)):
            return self.power() + other
        else:
            raise TypeError("Операнд должен быть числом или объектом класса Pair.")

    def __sub__(self, other):
        if isinstance(other, Pair):
            return self.power() - other.power()
        elif isinstance(other, (int, float)):
            return self.power() - other
        else:
            raise TypeError("Операнд должен быть числом или объектом класса Pair.")

    def __mul__(self, other):
        if isinstance(other, Pair):
            return self.power() * other.power()
        elif isinstance(other, (int, float)):
            return self.power() * other
        else:
            raise TypeError("Операнд должен быть числом или объектом класса Pair.")

    def __truediv__(self, other):
        if isinstance(other, Pair):
            return self.power() / other.power()
        elif isinstance(other, (int, float)):
            return self.power() / other
        else:
            raise TypeError("Операнд должен быть числом или объектом класса Pair.")


def make_pair(first: float, second: int) -> Pair:
    """
    Создание объекта Pair с проверкой параметров.
    :param first: дробное число.
    :param second: целое число.
    :return: объект Pair.
    """
    try:
        return Pair(first, second)
    except ValueError as e:
        print(f"Ошибка создания Pair: {e}")
        exit(1)


if __name__ == '__main__':
    # Демонстрация работы класса Pair
    print("Создание объекта Pair через конструктор:")
    pair1 = Pair(2.5, 3)
    pair1.display()
    print(f"Результат возведения в степень: {pair1.power()}")

    print("\nСоздание объекта Pair через функцию make_pair():")
    pair2 = make_pair(3.0, -2)
    pair2.display()
    print(f"Результат возведения в степень: {pair2.power()}")

    print("\nВвод данных с клавиатуры:")
    pair3 = Pair(0, 0)  # Создаем пустой объект
    try:
        pair3.read()
        pair3.display()
        print(f"Результат возведения в степень: {pair3.power()}")
    except ValueError:
        print("Ошибка при вводе данных.")

    print("\nПерегрузка операторов:")
    print(f"pair1 ** pair2: {pair1 ** pair2}")  # Возведение в степень
    print(f"pair1 + pair2: {pair1 + pair2}")  # Сложение
    print(f"pair1 - pair2: {pair1 - pair2}")  # Вычитание
    print(f"pair1 * pair2: {pair1 * pair2}")  # Умножение
    print(f"pair1 / pair2: {pair1 / pair2}")  # Деление
    print(f"pair1 == pair2: {pair1 == pair2}")  # Сравнение
    print(f"pair1 > pair2: {pair1 > pair2}")  # Сравнение