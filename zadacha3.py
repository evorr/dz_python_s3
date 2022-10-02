# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
#*Пример:*
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

#num_list=[4.56,3.9,4.1,8,1.01,9]
num_list=[1.1, 1.2, 3.1, 5, 10.01]

def max_min(numbers):
    max=numbers[0]%1
    min=numbers[0]%1
    for i in range(1,len(numbers)):
        if numbers[i]%1 > max:
            max=numbers[i]%1
        elif numbers[i]%1 < min:
            min=numbers[i]%1

    result=max-min
    return result

print(f"{num_list} => {max_min(num_list)}")