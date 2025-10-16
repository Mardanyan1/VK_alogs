
"""
Two sum
"""
def two_sum(mas, target):
    i = 0
    j = len(mas) - 1
    while i != j:
        if mas[i] + mas[j] == target:
            return i, j
        elif mas[i] + mas[j] < target:
            i = i + 1
        else:
            j = j - 1

mas = [2, 7, 11, 15]
target = 13
print(two_sum(mas, target))


"""
Развернуть массив
"""
def reverse_massive(mas):
    j = len(mas) - 1
    i = 0
    while True:
        if i > j or i == j:
            break
        temp_el = mas[i]
        mas[i] = mas[j]
        mas[j] = temp_el
        i += 1
        j -= 1
    # while i <= j:
    #     temp_mas.append(mas[j])
    #     j = j - 1
    # return temp_mas
    return mas

mas = [2, 7, 11, 15, 23, 27, 34, 41]
print(reverse_massive(mas))





# def reverse_part_massive(mas, start, end):
#     j = end
#     i = start
#     while True:
#         if i > j or i == j:
#             break
#         temp_el = mas[i]
#         mas[i] = mas[j]
#         mas[j] = temp_el
#         i += 1
#         j -= 1
#     return mas


"""
Развернуть часть массива
"""
def reverse_part_massive(mas, param):
    for el in range(param):
        temp_el = mas[0]
        mas.append(temp_el)
        mas.pop(0)
    reverse_massive(mas) #применяем функцию разворота из предыдущего задания
    return mas

print(reverse_part_massive(mas, 5))




"""
Слияние двух сортированных массива без аллокации:
"""
def summ_2_massives(mas1, mas2):
    i = 0
    j = 0
    res_mas = []
    while i < len(mas1) and j < len(mas2):
        if mas1[i] < mas2[j]:
            res_mas.append(mas1[i])
            i = i + 1
        else:
            res_mas.append(mas2[j])
            j = j + 1
    if i < len(mas1):
        res_mas.extend(mas1[i:])
    if j < len(mas2):
        res_mas.extend(mas2[j:])

    return res_mas


mas1 = [2, 7, 11, 15, 23, 27, 34, 41]
mas2 = [0, 14, 33, 57, 88]
print(summ_2_massives(mas1, mas2))


"""
Сортировка массива 0 и 1
"""
def sort_0_and_1(mas):
    left = 0
    right = len(mas) - 1
    while left < right:
        if mas[left] > mas[right]:
            temp_el = mas[left]
            mas[left] = mas[right]
            mas[right] = temp_el
            right-=1
            left+=1
        elif mas[left] == 0 and mas[right] == 0:
            left+=1
        elif mas[left] == 1 and mas[right] == 1:
            right-=1
        else:
            right -= 1
            left += 1
    return mas

mas = [0,1,0,0,1,0,1,1,1,0,1,0,1,1,0,0]
print(sort_0_and_1(mas))




#остались нидерланды, Перевернуть четные числа вперед, Нули в конец

"""
Задача флага Нидерландов
"""
def netherlands(mas):
    low = 0
    mid = 0
    high = len(mas) - 1

    while mid <= high:
        if mas[mid] == 0:
            mas[low], mas[mid] = mas[mid], mas[low]
            low += 1
            mid += 1
        elif mas[mid] == 1:
            mid += 1
        else:
            mas[mid], mas[high] = mas[high], mas[mid]
            high -= 1
    return mas

mas = [0, 2, 0, 2, 1, 0, 1, 2, 1, 0, 1, 2, 2, 1, 0, 0]
print(netherlands(mas))





"""
Перевернуть четные числа вперед
"""
def even_numbers(mas):
    i = 0
    j = len(mas)
    mas = reverse_massive(mas) #применяем функцию разворота reverse_massive

    while i < j:
        if mas[i] % 2 == 0:
            mas.append(mas[i])
            mas.pop(i)

            j -= 1
        else:
            i += 1

    mas = reverse_massive(mas) #применяем функцию разворота reverse_massive
    return mas


mas = [0, 33, 57, 88, 60, 0, 0, 80, 99]
print(even_numbers(mas))



"""
Нули в конец
"""
def null_in_end(mas):
    i = 0
    n = len(mas)
    while i < n:
        if mas[i] == 0:
            mas.pop(i)
            mas.append(0)
            n -= 1
        else:
            i += 1
    return mas


mas = [0, 33, 57, 88, 60, 0, 0, 80, 99]
print(null_in_end(mas))


