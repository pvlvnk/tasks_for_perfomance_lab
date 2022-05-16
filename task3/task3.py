import json
import os


def get_input():
    """Получает путь до файлов tests.json, values.json."""
    root_tests = input('Укажите путь до файла tests.json: ')
    root_values = input('Укажите путь до файла values.json: ')
    return root_tests, root_values


def parse_file(root_tests: str, root_values: str):
    """Получает из файлов json."""
    with open(root_tests) as tests:
        test_json = json.load(tests)
    with open(root_values) as values:
        values_json = json.load(values)
    return test_json, values_json


def get_values(test_list: list, values_json: dict):
    """
    Возвращает список с заполненными значениями value в словарях
    для дальнейшего создания report.json.

    """
    for test in test_list:
        if 'value' in test:
            test_id = test.get('id')
            for test_value in values_json.get('values'):
                if test_value.get('id') == test_id:
                    test['value'] = test_value['value']
        if test.get('values'):
            get_values(test.get('values'), values_json)
    return test_list


def create_report_json(report_list: list):
    """Создает файл report_json в директории с файлом task3.py
    с заполненными значениями value.

    """
    report_dict = {'reports': report_list}
    report_json = json.dumps(report_dict, indent=2)
    with (open(f'{os.path.dirname(os.path.abspath(__file__))}/report.json',
          'w') as report):
        report.write(report_json)


if __name__ == '__main__':
    root_tests, root_values = get_input()
    test_json, values_json = parse_file(root_tests, root_values)
    test_list = test_json.get('tests')
    report_list = get_values(test_list, values_json)
    create_report_json(report_list)
