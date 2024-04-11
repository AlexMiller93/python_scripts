import random
from typing import List
from functions import unique_items, display_numbers, sort_list
from geopoint import Point

lst_numbers: List[int] = [1, 1, 1, 2, 3, 5, 5]
char_list = ['bac', 'as', 'asd', 'ada','asd', 'rasdasd', 'ghjdfs']


def test_unique_items_correct():
    assert unique_items(lst_numbers) == [1, 2, 3, 5]

def test_display_numbers_correct():
    assert display_numbers(1, 5) == [1, 2, 3, 4, 5]

def test_sort_list_asc():
    assert sort_list(char_list) == ['as', 'bac', 'asd', 'ada', 'asd', 'ghjdfs', 'rasdasd']
    
def test_sort_list_desc():
    assert sort_list(char_list, up=True) == ['rasdasd', 'ghjdfs', 'bac', 'asd', 'ada', 'asd', 'as']
    
p1, p2 = Point(), Point()

def test_get_coordinates():
    p1.set_coordinates(1, 5)
    assert p1.get_coordinates() == (1, 5)
    
def test_update_coordinates():
    p1.update_coordinates(2, 4)
    assert p1.get_coordinates() == (2, 4)
    
def test_get_distance_positive():
    p1.set_coordinates(1, 5)
    p2.set_coordinates(2, 4)
    assert p1.get_distance(p2) == "Расстояние между точками равно = 1.41"
    
def test_get_distance_negative():
    p1.set_coordinates(-1, -7)
    p2.set_coordinates(-2, -7)
    assert p1.get_distance(p2) == "Расстояние между точками равно = 1.0"
    
def test_get_distance_fail():
    p1.set_coordinates(1, 5)
    assert p1.get_distance(1) == None