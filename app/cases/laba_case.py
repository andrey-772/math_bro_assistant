### it is a temporary file

from logic.core import (
    Equation,
    FloatNumber,
    Operations
)
from math import sqrt

class Task1:
    equation_view_1 = "7/17=0,412"
    equation_view_2 = "sqrt(33)=5,74"
    equation1 = Equation(number_a=7/17, number_b=0.412, for_output=equation_view_1)
    equation2 = Equation(number_a=sqrt(33), number_b=5.74, for_output=equation_view_2)

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


class Task2:
    float_number_one_view = "8.8612 += 0.0053"
    float_number_two_view = "3.064 += 3.064*0.02"
    number1 = FloatNumber(number=8.8612, error=0.0053)
    number2 = FloatNumber(number=3.064, error=3.064*0.02)


    def get_narrow_form(self) -> tuple:
        self.number_1_narrow, self.number_2_narrow = self.number1.get_narrow(), self.number2.get_narrow()
        return [f"{self.float_number_one_view} -> {self.number_1_narrow}", f"{self.float_number_two_view} -> {self.number_2_narrow}"]


    def get_wide_form(self) -> tuple:
        self.number_1_wide, self.number_2_wide = self.number1.get_wide(), self.number2.get_wide()
        return [f"{self.float_number_one_view} -> {self.number_1_wide}", f"{self.float_number_two_view} -> {self.number_2_wide}"]
    

    def get_absolute_error(self) -> tuple:
        try:
            operations = Operations()
            return [f"{self.number_1_narrow} is {operations.absolute_error(number=self.number_1_narrow)}", 
                    f"{self.number_2_narrow} is {operations.absolute_error(number=self.number_2_narrow)}",
                    f"{self.number_1_wide} is {operations.absolute_error(number=self.number_1_wide)}",
                    f"{self.number_2_wide} is {operations.absolute_error(number=self.number_2_wide)}", 
            ]
        except AttributeError:
            print("/")


    def __str__(self):
        return "Округлити сумнівні цифри числа, залишивши в ньому тільки вірні знаки: а) у вузькому сенсі; б) у широкому сенсі. Визначити абсолютну похибку результату."

#-------------
def task_1():
    task1 = Task1()
    print(task1)
    print(task1.equation_view_1, task1.equation_view_2)
    print("Рішення:")
    print(task1.check_one())


#-------------
def task_2():
    task2 = Task2()
    wide_form = task2.get_wide_form()
    narrow_form = task2.get_narrow_form()
    absolute_error = task2.get_absolute_error()
    print(task2)
    print(task2.float_number_one_view, ";", task2.float_number_two_view)
    print("Рішення:")
    for el in wide_form: print("wide form:", el)
    for el in narrow_form: print("narrow_form: ", el)
    for el in absolute_error: print("absolute_error: ", el)


if __name__ == "__main__":
    task_2()  
