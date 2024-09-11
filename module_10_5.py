import multiprocessing
import datetime

"""
Домашнее задание по теме "Многопроцессное программирование"
Задача "Многопроцессное считывание":
Студент Крылов Эдуард Васильевич
Дата: 11.09.2024 год.
"""


# Выполняемый код:
def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as files:
        while True:
            line_files = files.readline()
            if not line_files:
                break
            all_data.append(line_files)


filenames = [f'./file {number}.txt' for number in range(1, 5)]
if __name__ == '__main__':
    # Линейный вызов
    start_l = datetime.datetime.now()
    for line_file in filenames:
        read_info(line_file)
    end_l = datetime.datetime.now()
    print(f'Линейный вызов: \33[35m{end_l - start_l}\033[0m')

    # Многопроцессный
    start_m = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end_m = datetime.datetime.now()
    print(f'Многопроцессный: \033[31m{end_m - start_m}\033[0m')
