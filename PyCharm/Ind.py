import math
from multiprocessing import Process, Queue

eps = 10 ** (-7)  # точность вычисления


# Функция проверки суммы
def check_sum(x, out):
    result = (math.e ** x - math.e ** (-x)) / 2

    out.put(result)


# Функция вычисления бесконечной суммы
def inf_sum(x, out):
    a = (x ** 2) / 20
    S = a
    n = 1

    while math.fabs(a) > eps:
        a *= (x ** 2) / ((2 * n + 2) * (2 * n + 3))
        S += a
        n += 1

    out.put(S)


if __name__ == '__main__':
    x = 2  # значение аргумента

    # Создание очередей для передачи результатов между процессами
    out1 = Queue()
    out2 = Queue()

    # Создание процессов для вызова функций
    process_1 = Process(target=inf_sum, args=(x, out1))
    process_2 = Process(target=check_sum, args=(x, out2))

    # Запуск процессов
    process_1.start()
    process_2.start()

    # Получение результатов из очередей
    result1 = out1.get()
    result2 = out2.get()

    # Печать результатов
    print(f"The sum is: {result1}")
    print(f"The check is: {result2}")
