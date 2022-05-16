def get_input():
    """Получает значение последнего значения для кругового массива n и шаг m"""
    n = int(input('n= '))
    m = int(input('m= '))
    return n, m


def get_way(n: int, m: int):
    """Выводит путь, по которому, двигаясь интервалом длины m по заданному
    массиву, концом будет являться первый элемент.

    """
    i = 1
    way = '1'
    while True:
        i = 1 + (i + m - 2) % n
        if i == 1:
            break
        way += str(i)
    return way


if __name__ == '__main__':
    n, m = get_input()
    print(get_way(n, m))
