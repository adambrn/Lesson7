# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# При достижении конца более короткого файла,
# возвращайтесь в его начало.

def process_files(file1, file2, result_file):
    with open(file1, 'r') as names_file, open(file2, 'r') as numbers_file, open(result_file, 'w') as result:
        lines_names_file = names_file.readlines()
        lines_numbers_file = numbers_file.readlines()

        max_lines = max(len(lines_names_file), len(lines_numbers_file))

        for i in range(max_lines):
            name = lines_names_file[i % len(lines_names_file)].strip()
            numbers = lines_numbers_file[i % len(lines_numbers_file)].split('|')
            num1 = int(numbers[0])
            num2 = float(numbers[1])

            product = num1 * num2

            if product < 0:
                result.write(f"{name.lower()}|{abs(product)}\n")
            else:
                result.write(f"{name.upper()}|{round(product)}\n")

if __name__=='main':
    process_files("pseudo_names.txt","numbers.txt", "result.txt")
