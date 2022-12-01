# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.

def new_lst (lst):
    new_lst = []
    for i in lst:
        new_lst.append(round((i%1),2))
    return new_lst

lst = [1.1, 1.2, 3.1, 5.1, 10.01]

print(f'Исходный список {lst}\n')
new_lst = new_lst(lst)
print (f'Разница между максимальным {max(new_lst)} и минимальным {min(new_lst)} равна {max(new_lst) - min(new_lst)} ')