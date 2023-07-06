""" Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
расширение
минимальная длина случайно сгенерированного имени, по умолчанию 6
максимальная длина случайно сгенерированного имени, по умолчанию 30
минимальное число случайных байт, записанных в файл, по умолчанию 256
максимальное число случайных байт, записанных в файл, по умолчанию 4096
количество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона. """

import os
import random
import string

def create_files(extension, min_name_length=6, max_name_length=30, min_bytes=256, max_bytes=4096, num_files=42):
    for i in range(num_files):
        name_length = random.randint(min_name_length, max_name_length)
        name = ''.join(random.choice(string.ascii_lowercase) for _ in range(name_length))
        file_size = random.randint(min_bytes, max_bytes)

        file_name = f"{name}.{extension}"

        with open(file_name, 'wb') as file:
            random_bytes = os.urandom(file_size)
            file.write(random_bytes)

        print(f"Создан файл: {file_name} (Размер: {file_size} байт)")

def create_files_with_extensions(extensions_and_counts, min_name_length=6, max_name_length=30, min_bytes=256, max_bytes=4096):
    ''' Доработаем предыдущую задачу.
        Создайте новую функцию которая генерирует файлы с разными расширениями.
        Расширения и количество файлов функция принимает в качестве параметров.
        Количество переданных расширений может быть любым.
        Количество файлов для каждого расширения различно.
        Внутри используйте вызов функции из прошлой задачи. '''
    
    for extension, num_files in extensions_and_counts:
        create_files(extension, min_name_length=min_name_length, max_name_length=max_name_length, min_bytes=min_bytes, max_bytes=max_bytes, num_files=num_files)


if __name__ == '__main__':
    extensions_and_counts = [
        ("txt", 2),
        ("docx", 5),
        ("csv", 3)
    ]

    create_files_with_extensions(extensions_and_counts)
