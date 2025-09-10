import math

class Operations:
    def compare_numbers_on_accuracy(self, absolute_errora, absolute_errorb):
        pass

class Equation(Operations):
#let it be for first version
    def __init__(self, exact_valuea: float, approx_valuea: float, exact_valueb: float, approx_valueb: float, for_teachera: str=None, for_teacherb: str=None):
        self.exact_valuea = exact_valuea
        self.approx_valuea = approx_valuea
        
        self.exact_valueb = exact_valueb
        self.approx_valueb = approx_valueb
       
        self.for_teachera = for_teachera
        self.for_teacherb = for_teacherb

       
    def compare_numbers_on_accuracy(self):
        absolute_errora = abs(self.exact_valuea - self.approx_valuea)
        absolute_errorb = abs(self.exact_valueb - self.approx_valueb)
        if absolute_errorb < absolute_errora:
            return absolute_errora
        else:
            return absolute_errorb
        

class FloatNumber:
    def __test_two():
        number = 8.8612
        error = 0.0053
        for val in ((exact_valueb, absolute_errorb), (exact_valueb, absolute_errora)):
            number = val[0] 
            error = val[1]
            print(f"Початкове число: {number}")
            print(f"Вихідна абсолютна похибка: {error}")

            # --- а) У вузькому сенсі (залишаємо достовірні + 1 сумнівну) ---
            # У числі 8.8612, цифри 8, 8, 6, 1 є достовірними. Цифра 2 - сумнівна.
            # Залишаємо 8.861.
            rounded_narrow = 8.861
            # Похибка округлення (якщо б ми округлили 8.8612 до 8.861)
            rounding_error_narrow = abs(number - rounded_narrow)

            print(f"\n--- У вузькому сенсі ---")
            print(f"  Округлене число: {rounded_narrow}")
            # Ми визначаємо абсолютну похибку вже результату.
            # Вона складається з вихідної похибки та похибки округлення.
            # Тут краще просто вказати, що число тепер має такий вигляд.
            print(f"  Число після округлення: {rounded_narrow}") # Це результат

            # --- б) У широкому сенсі (округлення до певного розряду, наприклад, 3 знаки) ---
            # Округлюємо 8.8612 до 3 знаків після коми
            rounded_wide = round(number, 3)
            # Похибка округлення до 3 знаків
            rounding_error_wide = abs(number - rounded_wide)

            print(f"\n--- У широкому сенсі (до 3 знаків після коми) ---")
            print(f"  Округлене число: {rounded_wide}")
            # Тут гранична абсолютна похибка буде сумою вихідної похибки та похибки округлення
            # Гранична абсолютна похибка = вихідна похибка + (0.5 * розряд останнього знака)
            # Для 3 знаків розряд = 0.001, тому 0.5 * 0.001 = 0.0005
            # Проте, оскільки вихідна похибка вже значна, її теж враховуємо
            # Часто просто беруть максимальну з можливих похибок:
            max_possible_error = error + 0.0005 # Вихідна похибка + похибка округлення
            print(f"  Максимальна можлива абсолютна похибка результату: {max_possible_error:.4f}")


class Calculate():
    pass