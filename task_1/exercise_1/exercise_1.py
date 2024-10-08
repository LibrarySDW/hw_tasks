"""
№1 Реализуйте функцию process_data,
которая модифицирует входные данные в зависимости от их типа.
Функция должна обрабатывать вложенные структуры данных, такие как списки, словари и множества.
"""

# проверять, что значение data относится к определнному типу можно с помощью isinstance

def modify_nested_data(data):


"""
№ 2 Реализуйте функцию reverse_with_depth,
которая выполняет реверсирование элементов в списках и кортежах на определенной глубине рекурсии.
Функция должна обрабатывать два входных параметра: список и кортеж, а также параметр глубины, определяющий уровень рекурсии.
"""

def reverse_with_depth(lst, tpl, depth):
    def reverse_recursive(obj, d):
        if d == 0:


"""
№ 3 Напишите функцию pairwise_operations,
которая принимает два списка и операцию, которую нужно применить к каждому соответствующему элементу (например, сложение, умножение и т. д.).
Она должна возвращать список результатов и индексы, по которым была выполнена операция.
Можно предположить, что оба списка имеют одинаковую длину.
"""


def pairwise_operations(lst1, lst2, operation):
    return  # решение в 1 строку используя list comprehension


"""
№ 4 Напишите три функции:

Процедура modify_external_state, которая принимает список и изменяет его на месте.
Функция compute_difference, возвращающая разность двух чисел.
Генератор infinite_sequence, который выдает последовательность, начиная с заданного числа start и до limit.
"""


def modify_external_state(lst): # добавление строки "modified"
    pass

def compute_difference(a, b):
    pass

def infinite_sequence(start, limit): # использование yield
    pass


"""
№ 5 Напишите функцию flexible_function,
которая принимает любое количество позиционных и ключевых аргументов,
суммирует позиционные аргументы и перемножает значения ключевых аргументов.
Верните сумму и произведение.
"""


"""
№ 6 Объяснить разницу между модулем, фреймворком и библиотекой в Markdown-документе, указав примеры использования в Python.
"""
