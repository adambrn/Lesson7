# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# Полученные имена сохраните в файл

import random
import string

def generate_pseudo_name(num_names, file_name):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    pseudo_names = []

    for _ in range(num_names):
        name_length = random.randint(4, 7)
        name = random.choice(vowels)
        while len(name) < name_length:
                name += random.choice(string.ascii_lowercase)
        #print(name)
        pseudo_names.append(''.join(random.sample(name, len(name))).title())

    with open(file_name, 'w') as file:
        for pseud_name in pseudo_names:
            file.write(pseud_name + '\n')

if __name__ == '__main__':
    generate_pseudo_name(10, "pseudo_names.txt")

