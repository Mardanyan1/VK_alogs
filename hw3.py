from collections import defaultdict, Counter

# 1. Найти корень числа (ближайшее целое)
def binary_search_sqrt(target: int) -> int:
    if target < 0:
        raise ValueError("target must be non-negative")
    if target == 0 or target == 1:
        return target
    l, r = 0, target
    while l <= r:
        mid = (l + r) // 2
        sq = mid * mid
        if sq == target:
            return mid
        elif sq > target:
            r = mid - 1
        else:
            l = mid + 1
    return r  # ближайшее целое снизу

# 2. Очень лёгкая задача — копирование на двух ксероксах
def copy_time(n: int, x: int, y: int) -> int:
    if n == 1:
        return min(x, y)
    l = 0
    r = (n - 1) * max(x, y)
    while l + 1 < r:
        mid = (l + r) // 2
        total_copies = mid // x + mid // y
        if total_copies < n - 1:
            l = mid
        else:
            r = mid
    return r + min(x, y)

# 3. Накормить животных
def feed_animals(animals, food):
    if not animals or not food:
        return 0
    animals_sorted = sorted(animals)
    food_sorted = sorted(food)
    count = 0
    for f in food_sorted:
        if count < len(animals_sorted) and f >= animals_sorted[count]:
            count += 1
        if count == len(animals_sorted):
            break
    return count

# 4. Найти лишнюю букву
def extra_letter(a: str, b: str) -> str:
    count_b = Counter(b)
    count_a = Counter(a)
    for char in count_b:
        if count_b[char] != count_a.get(char, 0):
            return char
    return ""

# 5. Сумма двух элементов массива (Two Sum)
def two_sum(data, target):
    cache = {}
    for i, num in enumerate(data):
        diff = target - num
        if diff in cache:
            return [cache[diff], i]
        cache[num] = i
    return []

# 6. Сортировка Шелла
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for current_position in range(gap, n):
            m_gap = current_position
            while m_gap >= gap and arr[m_gap] < arr[m_gap - gap]:
                arr[m_gap], arr[m_gap - gap] = arr[m_gap - gap], arr[m_gap]
                m_gap -= gap
        gap //= 2
    return arr

# 7. Массив анаграмм
def group_anagrams(strs):
    anagram_groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        anagram_groups[key].append(s)
    return list(anagram_groups.values())


# --- Примеры вызовов функций ---
print("1. Корень числа:")
print(binary_search_sqrt(10))  # 3 (3^2 = 9 <= 10, 4^2 = 16 > 10)
print(binary_search_sqrt(16))  # 4

print("\n2. Копирование:")
print(copy_time(5, 1, 2))  # пример из условия: 5 копий, x=1, y=2 → ожидаем 4 + 1 = 5 сек?
print(copy_time(1, 1, 2))  # 1

print("\n3. Накормить животных:")
print(feed_animals([3, 4, 7], [8, 1, 2]))
print(feed_animals([3, 8, 1, 4], [1, 1, 2]))
print(feed_animals([1, 2, 2], [7, 1]))
print(feed_animals([8, 2, 3, 2], [1, 4, 3, 8]))

print("\n4. Лишняя буква:")
print(repr(extra_letter("uio", "oeiu")))
print(repr(extra_letter("fe", "efo")))
print(repr(extra_letter("ab", "ab")))
print(repr(extra_letter("bbb", "bbbb")))

print("\n5. Сумма двух чисел:")
print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
print(two_sum([1, 2, 3], 7))

print("\n6. Сортировка Шелла:")
arr = [64, 34, 25, 12, 22, 11, 90]
print("Было:", [64, 34, 25, 12, 22, 11, 90])
print("Стало:", shell_sort(arr.copy()))

print("\n7. Группировка анаграмм:")
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams(["won", "now", "aaa", "ooo", "ooo"]))
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))