# Напишите программу, которая будет преобразовывать десятичное число
# в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

a = int(input('Введите число: '))

def bin(num):
    if num==0:
        print(num, end="")
    elif num==1:
        print(num, end="")
    else:
        bin(num // 2)
        print(num % 2, end="")

print(f'{a} ->',end="")
bin(a)