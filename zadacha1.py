# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

num_list=[4,3,4,8,1,9,2]

def sum(numbers):
    odd_list=[]
    count=0
    for i in range(0,len(numbers)):
        if i%2!=0:
            odd_list.append(numbers[i])
            count+=numbers[i]
    return odd_list,count

odd_numbers, sum_elem = sum(num_list)
print(f'{num_list} -> на нечётных позициях элементы {odd_numbers}, ответ: {sum_elem}')