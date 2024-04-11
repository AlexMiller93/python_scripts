
class Point:
    """  Класс Point для работы с точками в двумерном пространстве """
    
    def set_coordinates(self, x: int, y: int):
        """ Метод для создания точки с координатами """
        
        self.x = x
        self.y = y
    
    def get_coordinates(self):
        """ Метод для получения координат точки """
        
        return (self.x, self.y)
    
    def update_coordinates(self, x: int, y: int):
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
    
    
    
