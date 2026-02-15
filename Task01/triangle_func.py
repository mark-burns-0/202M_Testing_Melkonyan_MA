class IncorrectTriangleSides(Exception):
    """Исключение, выбрасываемое при некорректных сторонах треугольника."""
    pass

def get_triangle_type(a: float, b: float, c: float) -> str:
    """
    Определяет тип треугольника по трем сторонам.
    
    Параметры:
    a, b, c : float - длины сторон треугольника
    
    Возвращает:
    str - тип треугольника: "equilateral", "isosceles" или "nonequilateral"

    Исключения:
    IncorrectTriangleSides - если стороны не образуют треугольник
    
    >>> get_triangle_type(5, 5, 5)
    'equilateral'
    >>> get_triangle_type(4, 4, 6)
    'isosceles'
    >>> get_triangle_type(3, 4, 5)
    'nonequilateral'
    >>> get_triangle_type(2, 3, 5)
    Traceback (most recent call last):
    IncorrectTriangleSides: Треугольник с такими сторонами не существует
    >>> get_triangle_type(-1, 2, 3)
    Traceback (most recent call last):
    IncorrectTriangleSides: Стороны должны быть положительными числами
    """

    if a <= 0 or b <= 0 or c <= 0:
        raise IncorrectTriangleSides("Стороны должны быть положительными числами")
    
    if a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides("Треугольник с такими сторонами не существует")
    
    if a == b == c:
        return "equilateral"

    if a == b or b == c or a == c:
        return "isosceles"

    return "nonequilateral"

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)