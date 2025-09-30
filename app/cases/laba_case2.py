from logic.core import Operations


class Task1:
    example_view = "f=(Q*(e**3))/(48*E)"
    Q_number = 54.8
    e_number = 2.45
    E_number = 0.863
    Q_error = 0.02
    e_error = 0.01
    E_error = 0.004
    operations_interface = Operations()

    def __init__(self):
        self.__first_step()
        self.__second_step()
        self.__third_step()

    def __first_step(self):
        self.f_approx = (self.Q_number * (self.e_number**3)) / 48 * self.E_number

    def __second_step(self):
        self.Q_relative_max = self.operations_interface.max_relative_error(
            number=self.Q_number, error=self.Q_error
        )
        self.e_relative_max = self.operations_interface.max_relative_error(
            number=self.e_number, error=self.e_error
        )
        self.E_relative_max = self.operations_interface.max_relative_error(
            number=self.E_number, error=self.E_error
        )

    def __third_step(self):
        self.f_relative_max = (
            (self.Q_relative_max * (self.e_relative_max**3)) / 48 * self.E_relative_max
        )
        self.f_absolute_max = self.operations_interface.max_absolute_error(
            number=self.f_approx, max_relative_error=self.f_relative_max
        )

    def first_step(self) -> float:
        return self.f_approx

    def second_step(self) -> float:
        return self.Q_relative_max, self.e_relative_max, self.E_relative_max

    def third_step(self) -> float:
        return self.f_relative_max, self.f_absolute_max

    def __str__(self):
        return "Обчислити значення X та визначити абсолютну та відносну похибку результату."


class Task2:
    example_view = "Q=((2*n-1)**2)*(x+y))/(x-y)"
    x_number = 4.2
    n_number = 2.0435
    y_number = 0.82
    y_error = 0.01
    x_error = 0.05
    n_error = 0.0001
    operations = Operations()

    def __init__(self):
        self.__first_step()
        self.__second_step()
        self.__third_step()

    def __first_step(self):
        self.Q_approx = (
            ((2 * self.n_number - 1) ** 2)
            * (self.x_number + self.y_number)
            / (self.x_number - self.y_number)
        )

    def __second_step(self):
        self.x_relative_max = self.operations.max_relative_error(
            number=self.x_number, error=self.x_error
        )
        self.y_relative_max = self.operations.max_relative_error(
            number=self.y_number, error=self.y_error
        )
        self.n_relative_max = self.operations.max_relative_error(
            number=self.n_number, error=self.n_error
        )

    def __third_step(self):
        self.Q_relative_max = (
            ((2 * self.n_relative_max - 1) ** 2)
            * (self.x_relative_max + self.y_relative_max)
            / (self.x_relative_max - self.y_relative_max)
        )
        self.Q_absolute_max = self.operations.max_absolute_error(
            number=self.Q_approx, max_relative_error=self.Q_relative_max
        )

    def first_step(self) -> float:
        return self.Q_approx

    def second_step(self) -> float:
        return self.x_relative_max, self.y_relative_max, self.n_relative_max

    def third_step(self) -> float:
        return self.Q_relative_max, self.Q_absolute_max

    def __str__(self):
        return "Обчислити значення X та визначити абсолютну та відносну похибку результату."


class Task3:
    example_view = "((alpha*b - beta*a)/b**2) - (beta*(a*b - beta*a))/(b**2*(b+beta))"
    alpha = 5.27
    beta = 0.0562
    a = 158.35
    b = 61.21

    def calculate(self) -> float:
        return ((self.alpha * self.b - self.beta * self.a) / self.b**2) - (
            self.beta * (self.a * self.b - self.beta * self.a)
        ) / (self.b**2 * (self.b + self.beta))

    def __str__(self):
        return "Обчислити, користуючись правилом підрахунку цифр."
