### it is a temporary file

import logic
from math import sqrt

class Task1():
    equation_view_1 = "7/17=0,412"
    equation_view_2 = "sqrt(33)=5,74"
    equation1 = logic.Equation(number_a=7/17, number_b=0.412, for_output=equation_view_1)
    equation2 = logic.Equation(number_a=sqrt(33), number_b=5.74, for_output=equation_view_2)

    not_absolute_error1 = equation1.get_accuracy()
    not_absolute_error2 = equation2.get_accuracy()

    def check_one(self) -> str:
        if self.not_absolute_error1 < self.not_absolute_error2:
            return f"{self.equation1.for_output} є точнішою"
        elif self.not_absolute_error1 > self.not_absolute_error2:
            return f"{self.equation2.for_output} є точнішою"
        else:
            return f"{self.equation2.for_output}, {self.equation1.for_output} є однакого точні"


    def __str__(self):
        return "Визначити, яка рівність точніша"


task1 = Task1()
print(task1)
print(task1.equation_view_1, task1.equation_view_2)
print("Рішення:")
print(task1.check_one())