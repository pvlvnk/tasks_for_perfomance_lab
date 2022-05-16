def get_input():
    """Получает путь до файла с исходными данными."""
    root_file = input('Укажите путь до файла с исходными данными: ')
    return root_file


def parse_file(root_file: str):
    """Получает массив целых чисел nums из файла."""
    with open(root_file) as file:
        nums = list(map(int, file.read().strip().split()))
    return nums


def min_steps_to_reduce(nums: list):
    """Принимает массив целых чисел, возвращает минимальное количество ходов,
    требуемых для приведения всех элементов к одному числу.

    """
    nums.sort()
    steps = 0
    if len(nums) % 2 == 0:
        mid2 = len(nums) // 2
        mid1 = mid2 - 1
        median = (nums[mid1] + nums[mid2]) // 2
    else:
        median = nums[len(nums) // 2]
    for num in nums:
        steps += abs(num - median)
    return steps


if __name__ == '__main__':
    root_file = get_input()
    nums = parse_file(root_file)
    print(min_steps_to_reduce(nums))
