def is_triangle(a, b, c):
    return True if a + b > c and a + c > b and b + c > a else False


if __name__ == '__main__':
    print(is_triangle(1, 2, 3))
    print(is_triangle(1, 2, 2))
    print(is_triangle(-1, 2, 3))
    print(is_triangle(1, 2, -3))
    print(is_triangle(2, 5, 1))
    print(is_triangle(5, 1, 5))
    print(is_triangle(2, 2, 2))
    print(is_triangle(0, 2, 3))
