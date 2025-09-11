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


class Task3():
    operations_interface = Operations()
    number1_view = "73,065"
    number2_view = "9,21"
    number1 = 73.065
    number2 = 9.21
    number1_obj = FloatNumber(number=number1)
    number2_obj = FloatNumber(number=number2)


    def get_narrow_form(self) -> tuple:
        self.number_1_narrow, self.number_2_narrow = self.number1_obj.get_narrow(), self.number2_obj.get_narrow()
        return [f"{self.number1} -> {self.number_1_narrow}", f"{self.number2} -> {self.number_2_narrow}"]


    def get_wide_form(self) -> tuple:
        self.number_1_wide, self.number_2_wide = self.number1_obj.get_wide(), self.number2_obj.get_wide()
        return [f"{self.number1} -> {self.number_1_wide}", f"{self.number2} -> {self.number_2_wide}"]
    

    def get_relative_error(self) -> tuple:
       try:
           self.number1_wide_relative = self.operations_interface.relative_error(number=self.number_1_wide)
           self.number1_narrow_relative = self.operations_interface.relative_error(number=self.number_1_narrow)
           self.number2_wide_relative = self.operations_interface.relative_error(number=self.number_2_wide)
           self.number2_narrow_relative = self.operations_interface.relative_error(number=self.number_2_narrow)
           print("!!")
           return [f"{self.number_1_wide} -> {self.number1_wide_relative}", f"{self.number_1_narrow} -> {self.number1_narrow_relative}", f"{self.number_2_wide} -> {self.number2_wide_relative}", f"{self.number_2_narrow} -> {self.number2_narrow_relative}"] 
       except AttributeError as w:
            print(w)


    def get_absolute_error(self) -> tuple:
       try:
           self.number1_wide_absolute = self.operations_interface.absolute_error(number=self.number_1_narrow)
           self.number1_narrow_absolute = self.operations_interface.absolute_error(number=self.number_1_wide)
           self.number2_wide_absolute = self.operations_interface.absolute_error(number=self.number_2_narrow)
           self.number2_narrow_absolute = self.operations_interface.absolute_error(number=self.number_2_wide)
           return [f"{self.number_1_wide} -> {self.number1_wide_absolute}", f"{self.number_1_narrow} -> {self.number1_narrow_absolute}", f"{self.number_2_wide} -> {self.number2_wide_absolute}", f"{self.number_2_narrow} -> {self.number2_narrow_absolute}"]       
       except AttributeError:
            print("/")

    


    def __str__(self):
        return "Знайти граничні абсолютні та відносні похибки чисел, якщо вони мають тільки вірні цифри: а) у вузькому сенсі; б) у широкому сенсі."


#-------------
