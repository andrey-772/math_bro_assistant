from . import laba_case
from . import laba_case2


def task_1():
    task1 = laba_case.Task1()
    print(task1)
    print(task1.equation_view_1, task1.equation_view_2)
    print("Результат:")
    print(task1.check_one())


# -------------
def task_2():
    task2 = laba_case.Task2()
    wide_form = task2.get_wide_form()
    narrow_form = task2.get_narrow_form()
    absolute_error = task2.get_absolute_error()
    print(task2)
    print(task2.float_number_one_view, ";", task2.float_number_two_view)
    print("Результат:")
    for el in wide_form:
        print("wide form: ", el)
    for el in narrow_form:
        print("narrow_form: ", el)
    for el in absolute_error:
        print("absolute_error: ", el)


def task_3():
    task3 = laba_case.Task3()
    wide_form = task3.get_wide_form()
    narrow_form = task3.get_narrow_form()
    relative_error = task3.get_relative_error()
    absolute_error = task3.get_absolute_error()
    print(task3)
    print(task3.number1, ";", task3.number2)
    print("Результат:")
    for el in wide_form:
        print("wide form: ", el)
    for el in narrow_form:
        print("narrow_form: ", el)
    for el in relative_error:
        print("relative_error: ", el)
    for el in absolute_error:
        print("absolute_error: ", el)


def task2_1():
    task1 = laba_case2.Task1()
    example_view = task1.example_view
    first_step_res = task1.first_step()
    second_step_res = task1.second_step()
    third_step_res = task1.third_step()
    print(task1)
    print(example_view)
    print("Результат: ")
    print(f"1 крок. f приблизне {first_step_res}")
    print(
        f"2 крок. Значення граничних відносних похибок змінних: {second_step_res[0], second_step_res[1], second_step_res[2]}"
    )
    print(
        f"3 крок. Значення f приблизне {first_step_res}, f граничне відносна похибка {third_step_res[0]},  f гранична абсолютна похибка {third_step_res[1]}"
    )


def task2_2():
    task2 = laba_case2.Task2()
    example_view = task2.example_view
    first_step_res = task2.first_step()
    second_step_res = task2.second_step()
    third_step_res = task2.third_step()
    print(task2)
    print(example_view)
    print("Результат: ")
    print(f"1 крок. Q приблизне {first_step_res}")
    print(
        f"2 крок. Значення граничних відносних похибок змінних: {second_step_res[0], second_step_res[1], second_step_res[2]}"
    )
    print(
        f"3 крок. Значення Q приблизне {first_step_res}, Q граничне відносна похибка {third_step_res[0]},  Q гранична абсолютна похибка {third_step_res[1]}"
    )


def task2_3():
    task3 = laba_case2.Task3()
    print(task3)
    print(task3.example_view)
    print("Результат: ")
    print(f"{task3.calculate()}")


if __name__ == "__main__":
    print("Завдання 1.")
    task_1()
    task_2()
    task_3()
    print("Завдання 2.")
    task2_1()
    task2_2()
    task2_3()
