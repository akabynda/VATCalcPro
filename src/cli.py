from vat_calculator import VATCalculator

def main():
    """
    Основная функция для взаимодействия с пользователем через командную строку.
    """
    while True:
        try:
            input_price_with_nds = float(input("Введите цену с НДС: "))
            proc_nds = int(input("Введите процент НДС: "))
            calculator = VATCalculator(input_price_with_nds, proc_nds)
            corrected_price_with_nds, corrected_price_without_nds = calculator.calculate()
            print(f"Корректированная цена с НДС: {corrected_price_with_nds:.2f}")
            print(f"Корректированная цена без НДС: {corrected_price_without_nds:.2f}")
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Непредвиденная ошибка: {e}")
        finally:
            cont = input("Хотите продолжить? (да/нет): ").strip().lower()
            if cont != 'да':
                break

if __name__ == "__main__":
    main()
