""" 
3. Создать класс Point, который представляет собой точку в двумерном пространстве. 
Класс должен иметь методы для инициализации координат точки, 
вычисления расстояния до другой точки, 
а также для получения и изменения координат.

"""

class Point:
    """  Класс Point для работы с точками в двумерном пространстве """
    
    def set_coordinates(self, x, y):
        """ Метод для создания точки с координатами """
        
        self.x = x
        self.y = y
    
    def get_coordinates(self):
        """ Метод для получения координат точки """
        
        return (self.x, self.y)
    
    def update_coordinates(self, x, y):
        """ Метод для обновления координат точки """
        
        self.x = x
        self.y = y
    
    def get_distance(self, p):
        """ Метод для вычисления расстояния между точками с координатами 

            Если другая точка не является экземпляром класса Point, 
            то расстояние рассчитываться не будет 
        """
        
        if isinstance(p, Point):
            distance = round(((p.x - self.x) ** 2 + (p.y - self.y) ** 2) ** 0.5, 2)
            return f"Расстояние между точками равно = {distance}"
        print("Другая точка не передана")
    
    
    
p1 = Point()
p2 = Point()
p1.set_coordinates(-1, -7)
p2.set_coordinates(-2, -7)

print(p1.get_distance(p2))
# print(p1.update_coordinates(2,4))
print(p1.get_coordinates())