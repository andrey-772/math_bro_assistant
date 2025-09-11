from .laba_case import Task1, Task2, Task3


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
    for el in wide_form: print("wide form: ", el)
    for el in narrow_form: print("narrow_form: ", el)
    for el in absolute_error: print("absolute_error: ", el)


def task_3():
    task3 = Task3()
    wide_form = task3.get_wide_form()
    narrow_form = task3.get_narrow_form()
    relative_error = task3.get_relative_error()
    absolute_error = task3.get_absolute_error()
    print(task3)
    print(task3.number1, ";", task3.number2)
    print("Рішення:")
    for el in wide_form: print("wide form: ", el)
    for el in narrow_form: print("narrow_form: ", el)
    for el in relative_error: print("relative_error: ", el)
    for el in absolute_error: print("absolute_error: ", el)


if __name__ == "__main__":
    task_1()
    task_2()
    task_3()  
