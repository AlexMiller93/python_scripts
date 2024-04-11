from functions import unique_items, display_numbers, sort_list
from geopoint import Point

numbers = [1, 3, 5, 3, 3, 4, 9, 0, 23]
words = 'I like Python and also I want to be backend developer'

p1 = Point()
p2 = Point()
p1.set_coordinates(1, 5)
p2.set_coordinates(2, 7)


if __name__ == '__main__':
    print(unique_items(numbers))
    print(display_numbers(2, 10))
    
    print(p1.get_distance(p2))
    print(p1.update_coordinates(2, 4))
    print(p1.get_coordinates())
    
    print(sort_list(words.split()))
    print(sort_list(words.split(), reverse=True))