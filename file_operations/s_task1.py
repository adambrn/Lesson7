# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции

import random
START, END = -1000, 1000

def fill_file_with_random_pairs(file_name, num_lines):
    with open(file_name, 'a') as file:
        for _ in range(num_lines):
            file.write(f"{random.randint(START, END)}|{random.uniform(START, END)}\n")

if __name__ == '__main__':
    fill_file_with_random_pairs("numbers.txt", 10)