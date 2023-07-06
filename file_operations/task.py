""" Напишите функцию группового переименования файлов. Она должна:
* принимать в качестве аргумента желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
* принимать в качестве аргумента расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
* принимать в качестве аргумента расширение конечного файла.
Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention> """

from pathlib import Path

def group_rename_files(new_name, source_extension, new_extension):
    directory = Path.cwd()
    files = list(directory.glob(f"*{source_extension}"))
    #print(files)
    renamed_count = 0
    for index, file in enumerate(files, start=1):
        new_file_name = f"{new_name}_{index}.{new_extension}"
        file.rename(directory / new_file_name)
        renamed_count += 1

        print(f"Переименован файл: {file.name} -> {new_file_name}")

    if renamed_count == 0:
        print("Нет файлов с указанным расширением.")
        return

    print(f"Переименовано файлов: {renamed_count}")

if __name__ == '__main__':
    group_rename_files("new_name", "txt", "md")

