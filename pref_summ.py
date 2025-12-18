from collections import defaultdict

# 1. Максимальная сумма подмассива длины k
def max_subarray_sum(arr, k):
    """
    Возвращает максимальную сумму подмассива длины k
    """
    if len(arr) < k:
        return None
    current_sum = sum(arr[:k])
    max_sum = current_sum
    for i in range(k, len(arr)):
        current_sum = current_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, current_sum)
    return max_sum


# 2. Количество подмассивов с суммой, равной k
def subarray_sum(nums, k):
    """
    Возвращает количество непрерывных подмассивов, сумма которых равна k
    """
    prefix_sum = 0
    count = 0
    prefix_count = defaultdict(int)
    prefix_count[0] = 1

    for num in nums:
        prefix_sum += num
        count += prefix_count[prefix_sum - k]
        prefix_count[prefix_sum] += 1

    return count


# 3. Максимальная длина подмассива с равным количеством 0 и 1
def find_max_length(nums):
    """
    Возвращает максимальную длину подмассива с равным количеством 0 и 1
    Заменяем 0 на -1, тогда задача сводится к поиску подмассива с суммой 0
    """
    prefix_sum = 0
    max_len = 0
    index_map = {0: -1}

    for i, num in enumerate(nums):
        prefix_sum += 1 if num == 1 else -1
        if prefix_sum in index_map:
            max_len = max(max_len, i - index_map[prefix_sum])
        else:
            index_map[prefix_sum] = i

    return max_len


# 4. Индекс поворота массива (pivot index)
def pivot_index(nums):
    """
    Возвращает индекс, где сумма слева равна сумме справа
    Если такого нет - возвращает -1
    """
    total_sum = sum(nums)
    left_sum = 0
    for i, num in enumerate(nums):
        if left_sum == total_sum - left_sum - num:
            return i
        left_sum += num
    return -1


# 5. Баланс скобок с возможностью удалить до k символов
def can_make_valid_with_deletions(s, k):

    balance = 0  # текущий баланс -  '(' = +1, ')' = -1
    extra_closed = 0 # количество ')' без пары

    for char in s:
        if char == '(':
            balance += 1
        else:
            if balance > 0:
                balance -= 1
            else:
                extra_closed += 1

    # Удалить все лишние закрывающие и оставшиеся открывающие
    total_needed = extra_closed + balance
    return total_needed <= k