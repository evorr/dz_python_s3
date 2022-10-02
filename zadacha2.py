# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

num_list=[4,3,4,8,1,9,2]

def mult(numbers):
    new_nums=[]
    for i in range(0,round(len(numbers)/2)):
        new_nums.append(numbers[i]*numbers[-i-1])
    return new_nums
new_num_list=mult(num_list)
print(f'{num_list} -> {new_num_list}')