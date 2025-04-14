import random

comp_num = random.randint(1, 100)
user_num = int(input('Угадайте число от 1 до 100: '))
while user_num != comp_num:
    if user_num > comp_num:
        print('ввы ввели слишком большое число.')
    else:
        print('вы ввели слишком маленькое число.')
    user_num = int(input('Угадайте число от 1 до 100: '))
print('Поздравляю! Вы выиграли!')