# Задача 1
# Напишите функцию с именем add_excitement, которая
# берет список строк и добавляет восклицательный знак
# (!) в конец каждой строки в списке. Программа должна
# изменить исходный список и ничего не возвращать.
# 2. (а)
# (b) Напишите ту же функцию, за исключением того,
# что она не должна изменять исходный список и вместо
# этого должна возвращать новый список.

def add_excitement(replace):
    for index in range(len(replace)):
        replace[index] = replace[index] + '!'

insert_list = ['apple', 'banana', 'orange']
add_excitement(insert_list)
print(insert_list)



def change_excitement(replace):
    new_list = []
    for index in range(len(replace)):
        add = replace[index] + '!'
        new_list.append(add)
    return new_list

country_list = ['usa', 'chine', 'germany']
new_lst = change_excitement(country_list)
print(country_list)
print(new_lst)



# Задача 2
# Напишите функцию match, которая принимает две
# строки в качестве аргументов и возвращает количество
# совпадений между строками. Совпадение — это когда две
# строки имеют один и тот же символ с одним и тем же
# индексом. Например, «python» и «path» совпадают в
# первом, третьем и четвертом символах, поэтому функция
# должна вернуть 3.

def match(first, second):
    count = 0
    for i in enumerate(first):
        for j in enumerate(second):
            if i[0] == j[0] and i[1] == j[1]:
                count += 1
    if count == 0:
        return 'совпадений отсуствует'
    return count

print(match('python','path'))
print(match('Poland', 'Danmark'))


# Задача 3
# Напомним, что если s является строкой, то s.find('a')
# найдет расположение первого символа a в s. Проблема в
# том, что он не находит местоположение каждого a. Напишите
# функцию findall, которая по заданной строке и одному символу
# возвращает список, содержащий все местоположения этого
# символа в строке. Он должен возвращать пустой список, если
# в строке нет вхождений символа.


def findall(word:str, substring:str) -> list:
    result_list = []
    for index, element in enumerate(word):
        if substring == element:
            result_list.append(index)
    return result_list

print(findall('Canada','a'))


