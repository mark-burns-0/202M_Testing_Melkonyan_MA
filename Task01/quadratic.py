def solve_quadratic(a, b, c):
    """
    Решает квадратное уравнение ax^2 + bx + c = 0.
    
    Параметры:
    a, b, c : float - коэффициенты уравнения
    
    Возвращает:
    tuple - кортеж из двух корней в порядке возрастания
    
    Исключения:
    ValueError - если уравнение не имеет решений или имеет бесконечно много решений
    
    Примеры:
    >>> solve_quadratic(1, -3, 2)
    (1.0, 2.0)
    >>> solve_quadratic(1, -2, 1)
    (1.0, 1.0)
    >>> solve_quadratic(1, 0, 1)
    Traceback (most recent call last):
        ...
    ValueError: Нет действительных корней
    >>> solve_quadratic(0, 2, -4)
    (2.0, 2.0)
    >>> solve_quadratic(0, 0, 5)
    Traceback (most recent call last):
        ...
    ValueError: Нет решений
    >>> solve_quadratic(0, 0, 0)
    Traceback (most recent call last):
        ...
    ValueError: Бесконечно много решений
    """
    if a == 0:
        if b == 0:
            if c == 0:
                raise ValueError("Бесконечно много решений")
            else:
                raise ValueError("Нет решений")
        else:
            x = -c / b
            return (x, x)
    
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        raise ValueError("Нет действительных корней")
    elif discriminant == 0:
        x = -b / (2*a)
        return (x, x)
    else:
        sqrt_d = discriminant ** 0.5
        x1 = (-b - sqrt_d) / (2*a)
        x2 = (-b + sqrt_d) / (2*a)
        return (min(x1, x2), max(x1, x2))


def print_solution(result):
    """Красивый вывод результата"""
    if isinstance(result, tuple):
        if result[0] == result[1]:
            print(f"Один корень (кратности 2): x = {result[0]}")
        else:
            print(f"Два корня: x1 = {result[0]}, x2 = {result[1]}")
    else:
        print(result)


def main():
    """Интерактивный режим для решения квадратных уравнений"""
    print("=" * 50)
    print("РЕШЕНИЕ КВАДРАТНОГО УРАВНЕНИЯ ax² + bx + c = 0")
    print("=" * 50)
    
    while True:
        print("\nВведите коэффициенты (или 'q' для выхода):")
        
        try:
            # Ввод коэффициентов
            a_input = input("a = ").strip()
            if a_input.lower() == 'q':
                break
            
            b_input = input("b = ").strip()
            if b_input.lower() == 'q':
                break
            
            c_input = input("c = ").strip()
            if c_input.lower() == 'q':
                break
            
            a = float(a_input)
            b = float(b_input)
            c = float(c_input)
            
            print("\n" + "-" * 30)
            print(f"Уравнение: {a}x² + {b}x + {c} = 0")
            
            result = solve_quadratic(a, b, c)
            print("Результат:", end=" ")
            print_solution(result)
            print("-" * 30)
            
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Непредвиденная ошибка: {e}")


def test_all_cases():
    """Запуск всех тестовых случаев из чек-листа"""
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ВСЕХ КЕЙСОВ ИЗ ЧЕК-ЛИСТА")
    print("=" * 60)
    
    test_cases = [
        (1, -3, 2, "Два различных корня"),
        (1, -2, 1, "Один корень"),
        (1, 0, 1, "Нет действительных корней"),
        (0, 2, -4, "Линейное уравнение"),
        (0, 3, 6, "Линейное уравнение с отрицательным корнем"),
        (0, 0, 5, "Нет решений"),
        (0, 0, 0, "Бесконечно много решений"),
        (1, 0, -2, "Иррациональные корни"),
        (0.5, -1.5, 1, "Дробные коэффициенты"),
        (-1, 5, -6, "Отрицательный коэффициент a"),
    ]
    
    for i, (a, b, c, description) in enumerate(test_cases, 1):
        print(f"\n{i}. {description}")
        print(f"   Вход: a={a}, b={b}, c={c}")
        
        try:
            result = solve_quadratic(a, b, c)
            print(f"   Результат: {result}")
        except ValueError as e:
            print(f"   Результат: {e}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--test":
            test_all_cases()
        elif sys.argv[1] == "--doctest":
            import doctest
            doctest.testmod(verbose=True)
        else:
            try:
                if len(sys.argv) == 4:
                    a, b, c = map(float, sys.argv[1:4])
                    result = solve_quadratic(a, b, c)
                    print_solution(result)
                else:
                    print("Использование: python quadratic.py a b c")
                    print("   или: python quadratic.py --test")
                    print("   или: python quadratic.py --doctest")
            except ValueError as e:
                print(f"Ошибка: {e}")
    else:
        main()