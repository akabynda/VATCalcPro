class VATCalculator:
    """
    Класс для вычисления цен с НДС и без НДС.
    """

    def __init__(self, input_price_with_nds, proc_nds):
        """
        Инициализация объекта класса VATCalculator.

        Параметры:
        input_price_with_nds (float): Входная цена с НДС.
        proc_nds (int): Процент НДС.
        """
        self.input_price_with_nds = input_price_with_nds
        self.proc_nds = proc_nds
        self.validate_parameters()

    def validate_parameters(self):
        """
        Валидация входных параметров.

        Выбрасывает исключение ValueError, если процент НДС не в диапазоне 0-99
        или если входная цена с НДС отрицательная.
        """
        if not (0 <= self.proc_nds <= 99):
            raise ValueError("Процент НДС должен быть в диапазоне от 0 до 99.")
        if self.input_price_with_nds < 0:
            raise ValueError("Входная цена с НДС должна быть неотрицательной.")

    def calculate(self):
        """
        Вычисление цен с НДС и без НДС.

        Возвращает:
        tuple: цена с НДС, цена без НДС.
        """
        # Вычисление цены без НДС
        corrected_price_without_nds = self.input_price_with_nds / (1 + self.proc_nds / 100)

        # Вычисление цены с НДС
        corrected_price_with_nds = corrected_price_without_nds * (1 + self.proc_nds / 100)

        # Обрезка до двух знаков после запятой без округления
        corrected_price_with_nds = int(corrected_price_with_nds * 100) / 100
        corrected_price_without_nds = int(corrected_price_without_nds * 100) / 100

        return corrected_price_with_nds, corrected_price_without_nds