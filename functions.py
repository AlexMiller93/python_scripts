from typing import List

def unique_items(lst:List[int]) -> List[int]:
    """ Функция принимает список целых чисел и возвращает новый список уникальных элементов """
    
    return list(set(lst))

def display_numbers(a: int, b: int) -> List[int]:
    """ Функция принимает два целых числа и возвращает список простых между этими числами """
    
    return [num for num in range(a, b + 1)]

def sort_list(char_list: List[str], up: bool=None) -> List[str]:
    """ Функция принимает список строк и необязательный аргумент булевого типа, 
        а возвращает список простых между этими числами """
    
    if up:
        char_list.sort(key=lambda x: len(x), reverse=True)
    else:
        char_list.sort(key=lambda x: len(x))

    return char_list

