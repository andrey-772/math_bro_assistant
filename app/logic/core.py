import math
class Operations:
    def absolute_error(self, number: float) -> float:
        s = str(number)
        if '.' in s:
            decimal_places = len(s.split('.')[1])  # количество знаков после запятой
            self.delta = 10 ** (-decimal_places)       # погрешность = 1 последней цифры
        else:
            self.delta = 1  # если целое число, последняя цифра единица
        return self.delta


    def __absolute_error(self, number: float) -> float:
        s = str(number)
        if '.' in s:
            decimal_places = len(s.split('.')[1])  # количество знаков после запятой
            self.delta = 10 ** (-decimal_places)       # погрешность = 1 последней цифры
        else:
            self.delta = 1  # если целое число, последняя цифра единица
        return self.delta


    def relative_error(self, number: float) -> float:
        self.__absolute_error(number)
        return self.delta / abs(number)


class Equation:
    def __init__(self, number_a: float, number_b: float, for_output: str):
        self.number_a = number_a
        self.number_b = number_b        
        self.for_output = for_output

       
    def get_accuracy(self) -> float:
        not_absolute_error = abs(self.number_a - self.number_b) / abs(self.number_b)
        return not_absolute_error
        

class FloatNumber:
    def __init__(self, number: float | int, error: float=0.001):
        self.number = number
        self.error = error

   
    def get_narrow(self) -> float:
        order = -int(math.floor(math.log10(self.error))) 
        return round(self.number, order)

    
    def get_wide(self) -> float:
        order = -int(math.floor(math.log10(self.error)))
        return round(self.number, order - 1)



###calculate first example from shell /make interface - convert into app as soon as it possible

