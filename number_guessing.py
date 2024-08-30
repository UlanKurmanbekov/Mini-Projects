from random import randint

random_num = randint(1, 100)
print('Добро пожаловать в числовую угадайку')

def is_valid(num):
    if num.isdigit():
        num = int(num)
        if 1 <= num <= 100:
            return True
        else:
            return False
    else:
        return False

count = 0

while True:
    response = input('Введите число от 1 до 100: ')
    if not is_valid(response):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    response = int(response)
    count += 1
    if response < random_num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif response > random_num:
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print(f'Вы угадали, поздравляем! Количество попыток {count}')
        break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')