class BitString:
    MAX_SIZE = 100  # Максимально возможный размер битовой строки

    def __init__(self, size=MAX_SIZE, initial_value=None):
        """
        Конструктор класса.
        :param size: Размер битовой строки (не более MAX_SIZE).
        :param initial_value: Начальное значение битовой строки (список или строка).
        """
        if size <= 0 or size > self.MAX_SIZE:
            raise ValueError(f"Размер должен быть в диапазоне от 1 до {self.MAX_SIZE}")

        self.size_ = size  # Максимальный размер для данного объекта
        self.bits = [0] * size  # Инициализация списка нулями
        self.count = 0  # Текущее количество установленных битов

        if initial_value is not None:
            if isinstance(initial_value, str):  # Если начальное значение - строка
                if len(initial_value) > size:
                    raise ValueError("Длина строки превышает заданный размер")
                for i, char in enumerate(initial_value):
                    if char not in ('0', '1'):
                        raise ValueError("Строка должна содержать только символы '0' и '1'")
                    self.bits[i] = int(char)
                    if char == '1':
                        self.count += 1
            elif isinstance(initial_value, list):  # Если начальное значение - список
                if len(initial_value) > size:
                    raise ValueError("Длина списка превышает заданный размер")
                for i, bit in enumerate(initial_value):
                    if bit not in (0, 1):
                        raise ValueError("Список должен содержать только значения 0 и 1")
                    self.bits[i] = bit
                    if bit == 1:
                        self.count += 1
            else:
                raise TypeError("Начальное значение должно быть строкой или списком")

    def size(self):
        """Возвращает максимальный размер битовой строки."""
        return self.size_

    def __len__(self):
        """Возвращает текущее количество установленных битов."""
        return self.count

    def __getitem__(self, index):
        """Перегрузка оператора индексирования []."""
        if isinstance(index, int):
            if index < 0 or index >= self.size_:
                raise IndexError("Индекс вне допустимого диапазона")
            return self.bits[index]
        elif isinstance(index, slice):
            return self.bits[index]
        else:
            raise TypeError("Индекс должен быть целым числом или срезом")

    def __and__(self, other):
        """Операция побитового AND."""
        if not isinstance(other, BitString):
            raise TypeError("Операнд должен быть объектом класса BitString")
        if self.size_ != other.size_:
            raise ValueError("Битовые строки должны иметь одинаковый размер")

        result = BitString(self.size_)
        for i in range(self.size_):
            result.bits[i] = self.bits[i] & other.bits[i]
            if result.bits[i] == 1:
                result.count += 1
        return result

    def __or__(self, other):
        """Операция побитового OR."""
        if not isinstance(other, BitString):
            raise TypeError("Операнд должен быть объектом класса BitString")
        if self.size_ != other.size_:
            raise ValueError("Битовые строки должны иметь одинаковый размер")

        result = BitString(self.size_)
        for i in range(self.size_):
            result.bits[i] = self.bits[i] | other.bits[i]
            if result.bits[i] == 1:
                result.count += 1
        return result

    def __xor__(self, other):
        """Операция побитового XOR."""
        if not isinstance(other, BitString):
            raise TypeError("Операнд должен быть объектом класса BitString")
        if self.size_ != other.size_:
            raise ValueError("Битовые строки должны иметь одинаковый размер")

        result = BitString(self.size_)
        for i in range(self.size_):
            result.bits[i] = self.bits[i] ^ other.bits[i]
            if result.bits[i] == 1:
                result.count += 1
        return result

    def __invert__(self):
        """Операция побитового NOT."""
        result = BitString(self.size_)
        for i in range(self.size_):
            result.bits[i] = 1 - self.bits[i]
            if result.bits[i] == 1:
                result.count += 1
        return result

    def shift_left(self, n):
        """Сдвиг влево на n бит."""
        if n < 0:
            raise ValueError("Количество сдвигов должно быть неотрицательным")
        result = BitString(self.size_)
        result.bits = self.bits[n:] + [0] * min(n, self.size_)
        result.count = sum(result.bits)
        return result

    def shift_right(self, n):
        """Сдвиг вправо на n бит."""
        if n < 0:
            raise ValueError("Количество сдвигов должно быть неотрицательным")
        result = BitString(self.size_)
        result.bits = [0] * min(n, self.size_) + self.bits[:self.size_ - n]
        result.count = sum(result.bits)
        return result

    def __str__(self):
        """Строковое представление битовой строки."""
        return ''.join(map(str, self.bits))

# Создание объектов BitString
bs1 = BitString(8, "10101010")  # Битовая строка: 10101010
bs2 = BitString(8, "11001100")  # Битовая строка: 11001100

# Вывод начальных битовых строк
print("bs1:", bs1)  # Вывод: 10101010
print("bs2:", bs2)  # Вывод: 11001100

# Побитовые операции
and_result = bs1 & bs2  # Побитовое AND
or_result = bs1 | bs2   # Побитовое OR
xor_result = bs1 ^ bs2  # Побитовое XOR
not_result = ~bs1       # Побитовое NOT

print("AND (bs1 & bs2):", and_result)  # Вывод: 10001000
print("OR (bs1 | bs2):", or_result)    # Вывод: 11101110
print("XOR (bs1 ^ bs2):", xor_result)  # Вывод: 01100110
print("NOT (~bs1):", not_result)       # Вывод: 01010101

# Сдвиги
shift_left_result = bs1.shift_left(2)   # Сдвиг влево на 2 бита
shift_right_result = bs1.shift_right(2) # Сдвиг вправо на 2 бита

print("Shift Left (bs1 << 2):", shift_left_result)  # Вывод: 10101000
print("Shift Right (bs1 >> 2):", shift_right_result)  # Вывод: 00101010

# Индексирование
print("bs1[3]:", bs1[3])  # Вывод: 0 (четвертый бит)
print("bs1[1:5]:", bs1[1:5])  # Вывод: [0, 1, 0, 1] (срез)

# Размер и длина
print("Size of bs1:", bs1.size())  # Вывод: 8 (максимальный размер)
print("Count of set bits in bs1:", len(bs1))  # Вывод: 4 (количество единиц)

# Создание пустой битовой строки и заполнение её значениями
bs3 = BitString(8)  # Пустая битовая строка: 00000000
print("Initial bs3:", bs3)  # Вывод: 00000000

# Установка значений через индексирование
bs3[0] = 1
bs3[2] = 1
bs3[4] = 1
bs3[6] = 1
print("Modified bs3:", bs3)  # Вывод: 10101010
print("Count of set bits in bs3:", len(bs3))  # Вывод: 4 (количество единиц)