def get_input():
    """Получает путь до файлов с исходными данными."""
    root_file1 = input('Укажите путь до file1: ')
    root_file2 = input('Укажите путь до file2: ')
    return root_file1, root_file2


def parse_file(root_file1: str, root_file2: str):
    """Получает координаты точек из файлов."""
    points = []
    with open(root_file1) as file1:
        centre = list(map(float, file1.readline().strip().split()))
        x0, y0 = centre[0], centre[1]
        rad = int(file1.readline().strip().split()[0])
    with open(root_file2) as file2:
        while True:
            point = list(map(float, file2.readline().strip().split()))
            if point:
                points.append(point)
            else:
                break
    return x0, y0, rad, points


def is_in_circle(x0: float, y0: float, rad: int, point: list):
    """Проверяет, находится ли точка на/в/вне окружности."""
    x1 = point[0]
    y1 = point[1]
    vector_length = (x1-x0) ** 2 + ((y1-y0) ** 2) ** 0.5
    if vector_length == rad:
        return 0
    elif vector_length < rad:
        return 1
    else:
        return 2


if __name__ == '__main__':
    root_file1, root_file2 = get_input()
    x0, y0, rad, points = parse_file(root_file1, root_file2)
    for point in points:
        ans = is_in_circle(x0, y0, rad, point)
        print(ans)
