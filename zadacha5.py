#Задайте число. Составьте список чисел Фибоначчи, в том числе
# для отрицательных индексов.
#*Пример:*
#- для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи] (https://ru.wikipedia.org/wiki/Негафибоначчи)

a = int(input('Введите число: '))

def fib(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    elif n==-1:
        return 1
    elif n==-2:
        return -1
    else:
        if n<0:
            return fib(n+2)-fib(n+1)
        else:
            return fib(n-1)+fib(n-2)

list=[]
for i in range(-a,a):
    list.append(fib(i))
print(list)
