import math
class Operations:
    def absolute_error(self, number: float) -> float:
        s = str(number)
        if '.' in s:
            decimal_places = len(s.split('.')[1])  
            delta = 10 ** (-decimal_places)  
        else:
            delta = 1 
        return delta


    def max_absolute_error(self, number: float, max_relative_error) -> float:
        return number * max_relative_error


    def max_relative_error(self, number: float, error:float=1.0) -> float:
        delta = error / abs(number)
        return delta


class Equation:
    def __init__(self, number_a: float, number_b: float, for_output: str):
        self.number_a = number_a
        self.number_b = number_b        
        self.for_output = for_output

       
    def get_accuracy(self) -> float:
        not_absolute_error = abs(self.number_a - self.number_b) / abs(self.number_b)
        return not_absolute_error
        

class FloatNumber:
    def __init__(self, number: float, error: float=0.001):
        self.number = number
        self.error = error

   
    def get_narrow(self) -> float:
        order = -int(math.floor(math.log10(self.error))) 
        return round(self.number, order)

    
    def get_wide(self) -> float:
        order = -int(math.floor(math.log10(self.error)))
        return round(self.number, order - 1)



###calculate first example from shell /make interface - convert into app as soon as it possible

