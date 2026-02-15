import pytest
from triangle_class import Triangle, IncorrectTriangleSides


# Позитивные тесты
def test_equilateral_triangle():
    """Тест создания равностороннего треугольника"""
    triangle = Triangle(5, 5, 5)
    assert triangle.triangle_type() == "equilateral"
    assert triangle.perimeter() == 15


def test_equilateral_triangle_float():
    """Тест создания равностороннего треугольника с дробными сторонами"""
    triangle = Triangle(3.3, 3.3, 3.3)
    assert triangle.triangle_type() == "equilateral"
    assert round(triangle.perimeter(),2) == 9.9


def test_isosceles_triangle():
    """Тест создания равнобедренного треугольника"""
    triangle = Triangle(4, 4, 6)
    assert triangle.triangle_type() == "isosceles"
    assert triangle.perimeter() == 14


def test_isosceles_triangle_different_order():
    """Тест равнобедренного треугольника с разным порядком сторон"""
    t1 = Triangle(4, 6, 4)
    t2 = Triangle(6, 4, 4)
    assert t1.triangle_type() == "isosceles"
    assert t2.triangle_type() == "isosceles"
    assert t1.perimeter() == 14
    assert t2.perimeter() == 14


def test_isosceles_triangle_float():
    """Тест равнобедренного треугольника с дробными сторонами"""
    triangle = Triangle(5.5, 5.5, 7.2)
    assert triangle.triangle_type() == "isosceles"
    assert abs(triangle.perimeter() - 18.2) < 1e-10


def test_nonequilateral_triangle():
    """Тест создания разностороннего треугольника"""
    triangle = Triangle(3, 4, 5)
    assert triangle.triangle_type() == "nonequilateral"
    assert triangle.perimeter() == 12


def test_nonequilateral_triangle_float():
    """Тест разностороннего треугольника с дробными сторонами"""
    triangle = Triangle(2.5, 3.5, 4.5)
    assert triangle.triangle_type() == "nonequilateral"
    assert triangle.perimeter() == 10.5


def test_large_numbers():
    """Тест с большими числами"""
    triangle = Triangle(1000000, 1000000, 1000000)
    assert triangle.triangle_type() == "equilateral"
    assert triangle.perimeter() == 3000000


def test_small_numbers():
    """Тест с очень маленькими числами"""
    triangle = Triangle(0.000001, 0.000001, 0.000001)
    assert triangle.triangle_type() == "equilateral"
    assert triangle.perimeter() == 0.000003


# Негативные тесты
def test_negative_side():
    """Тест с отрицательной стороной"""
    with pytest.raises(IncorrectTriangleSides) as exc_info:
        Triangle(-1, 2, 3)
    assert "положительными" in str(exc_info.value).lower()


def test_negative_side_other_position():
    """Тест с отрицательной стороной на разных позициях"""
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, -2, 3)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, -3)


def test_zero_side():
    """Тест с нулевой стороной"""
    with pytest.raises(IncorrectTriangleSides) as exc_info:
        Triangle(0, 4, 5)
    assert "положительными" in str(exc_info.value).lower()


def test_zero_side_other_position():
    """Тест с нулевой стороной на разных позициях"""
    with pytest.raises(IncorrectTriangleSides):
        Triangle(4, 0, 5)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(4, 5, 0)


def test_all_sides_zero():
    """Тест со всеми нулевыми сторонами"""
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 0, 0)


def test_two_sides_negative():
    """Тест с двумя отрицательными сторонами"""
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-5, -5, 3)


def test_triangle_inequality_equal():
    """Тест нарушения неравенства (сумма двух равна третьей)"""
    with pytest.raises(IncorrectTriangleSides) as exc_info:
        Triangle(2, 3, 5)
    assert "не существует" in str(exc_info.value).lower()


def test_triangle_inequality_equal_different_order():
    """Тест нарушения неравенства на разных позициях"""
    with pytest.raises(IncorrectTriangleSides):
        Triangle(5, 2, 3)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(2, 5, 3)


def test_triangle_inequality_less():
    """Тест нарушения неравенства (сумма двух меньше третьей)"""
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 10)


def test_triangle_inequality_very_unequal():
    """Тест с очень большим неравенством"""
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 1, 1000)


def test_two_sides_sum_less_than_third():
    """Тест с разными комбинациями неравенства"""
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 10, 2)  # 1 + 2 < 10
    with pytest.raises(IncorrectTriangleSides):
        Triangle(10, 1, 2)  # 1 + 2 < 10


# Тесты на граничные значения
def test_perimeter_consistency():
    """Тест соответствия периметра сумме сторон"""
    a, b, c = 3, 4, 5
    triangle = Triangle(a, b, c)
    assert triangle.perimeter() == a + b + c


def test_multiple_triangles():
    """Тест работы с несколькими треугольниками"""
    t1 = Triangle(5, 5, 5)
    t2 = Triangle(4, 4, 6)
    t3 = Triangle(3, 4, 5)
    
    assert t1.triangle_type() == "equilateral"
    assert t2.triangle_type() == "isosceles"
    assert t3.triangle_type() == "nonequilateral"
    
    assert t1.perimeter() == 15
    assert t2.perimeter() == 14
    assert t3.perimeter() == 12


# Параметризованные тесты (более продвинутый способ)
@pytest.mark.parametrize("a, b, c, expected_type, expected_perimeter", [
    (5, 5, 5, "equilateral", 15),
    (4, 4, 6, "isosceles", 14),
    (3, 4, 5, "nonequilateral", 12),
    (5.5, 5.5, 5.5, "equilateral", 16.5),
    (3.5, 3.5, 5.0, "isosceles", 12.0),
])
def test_triangle_parametrized(a, b, c, expected_type, expected_perimeter):
    """Параметризованный тест для разных типов треугольников"""
    triangle = Triangle(a, b, c)
    assert triangle.triangle_type() == expected_type
    assert triangle.perimeter() == expected_perimeter


@pytest.mark.parametrize("a, b, c", [
    (-1, 2, 3),
    (1, -2, 3),
    (1, 2, -3),
    (0, 4, 5),
    (4, 0, 5),
    (4, 5, 0),
    (2, 3, 5),
    (5, 2, 3),
    (1, 2, 10),
    (0, 0, 0),
    (-5, -5, 3),
])
def test_invalid_triangles_parametrized(a, b, c):
    """Параметризованный тест для некорректных треугольников"""
    with pytest.raises(IncorrectTriangleSides):
        Triangle(a, b, c)


# Тест на неизменяемость сторон
def test_sides_are_accessible():
    """Тест доступа к сторонам треугольника"""
    triangle = Triangle(3, 4, 5)
    assert triangle.a == 3
    assert triangle.b == 4
    assert triangle.c == 5


# Тест на создание треугольника после проверки исключений
def test_exception_doesnt_create_triangle():
    """Тест, что при исключении объект не создается"""
    with pytest.raises(IncorrectTriangleSides):
        triangle = Triangle(1, 2, 10)
        assert False, "Треугольник не должен был создаться"