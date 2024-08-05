import unittest
from src.vat_calculator import VATCalculator

class TestVATCalculator(unittest.TestCase):
    """
    Класс для тестирования класса VATCalculator.
    """

    def test_calc_prices(self):
        """
        Тестирование корректных вычислений цен с НДС и без НДС.
        """
        calculator = VATCalculator(1.81, 20)
        self.assertEqual(calculator.calculate(), (1.81, 1.5))

        calculator = VATCalculator(1.81, 18)
        self.assertEqual(calculator.calculate(), (1.81, 1.53))

        calculator = VATCalculator(5.05, 27)
        self.assertEqual(calculator.calculate(), (5.05, 3.97))

    def test_invalid_proc_nds(self):
        """
        Тестирование выброса исключения для некорректного процента НДС.
        """
        with self.assertRaises(ValueError):
            VATCalculator(1.81, 100)
        with self.assertRaises(ValueError):
            VATCalculator(1.81, -1)

    def test_negative_price(self):
        """
        Тестирование выброса исключения для отрицательной входной цены с НДС.
        """
        with self.assertRaises(ValueError):
            VATCalculator(-1.81, 20)

if __name__ == "__main__":
    unittest.main()
