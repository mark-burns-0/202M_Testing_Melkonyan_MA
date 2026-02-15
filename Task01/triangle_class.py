class IncorrectTriangleSides(Exception):
    """Исключение, выбрасываемое при некорректных сторонах треугольника."""
    pass


class Triangle:
    """
    Класс, представляющий треугольник.
    
    Атрибуты:
    a, b, c : float - длины сторон треугольника
    """
    
    def __init__(self, a, b, c):
        """
        Конструктор класса Triangle.
        
        Параметры:
        a, b, c : float - длины сторон треугольника
        
        Исключения:
        IncorrectTriangleSides - если стороны не образуют треугольник
        """
        if a <= 0 or b <= 0 or c <= 0:
            raise IncorrectTriangleSides("Стороны должны быть положительными числами")
        if a + b <= c or a + c <= b or b + c <= a:
            raise IncorrectTriangleSides("Треугольник с такими сторонами не существует")
        
        # Сохранение сторон
        self.a = a
        self.b = b
        self.c = c
    
    def triangle_type(self) -> str:
        """
        Определяет тип треугольника.
        
        Возвращает:
        str - тип треугольника: "equilateral", "isosceles" или "nonequilateral"
        """
        if self.a == self.b == self.c:
            return "equilateral"
        
        if self.a == self.b or self.b == self.c or self.a == self.c:
            return "isosceles"
        
        return "nonequilateral"
    
    def perimeter(self) -> float:
        """
        Вычисляет периметр треугольника.
        
        Возвращает:
        float - сумма длин всех сторон
        """
        return self.a + self.b + self.c
    
    def __repr__(self) -> str:
        """
        Строковое представление треугольника для отладки.
        """
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"