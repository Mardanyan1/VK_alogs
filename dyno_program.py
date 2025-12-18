# 1. Количество бинарных последовательностей длины N без двух единиц подряд
def count_sequences_no_two_ones(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 2
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# 2. Количество бинарных последовательностей без трёх единиц подряд
def count_sequences_no_three_ones(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n == 2:
        return 4
    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2] = 1, 2, 4
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]


# 3. Наибольшая непрерывная возрастающая подпоследовательность
def longest_increasing_subarray(nums):

    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            dp[i] = dp[i - 1] + 1
    return max(dp)


# 4. Треугольник Паскаля (итеративный подход)
def pascal_triangle(n):

    if n <= 0:
        return []
    triangle = [[1]]
    for row in range(1, n):
        prev_row = triangle[-1]
        current_row = [1]
        for j in range(1, row):
            current_row.append(prev_row[j - 1] + prev_row[j])
        current_row.append(1)
        triangle.append(current_row)
    return triangle


# 5. Максимальная прибыль от одной покупки и продажи акций
def max_profit(prices):

    if not prices:
        return 0
    min_price = prices[0]
    profit = 0
    for price in prices[1:]:
        profit = max(profit, price - min_price)
        min_price = min(min_price, price)
    return profit


# 6. Минимальное количество монет для сдачи (задача о размене)
def coin_change(coins, amount):

    if amount == 0:
        return 0
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


# 7. Самый длинный палиндром в строке (метод "расширение от центра")
def longest_palindrome(s):
    """
    Использует два указателя, расширяющихся от центра.
    """
    if not s:
        return ""

    start, end = 0, 0

    def expand_around_center(left, right):
        nonlocal start, end
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left > end - start:
                start, end = left, right
            left -= 1
            right += 1

    for i in range(len(s)):
        expand_around_center(i, i)  # нечётная длина
        expand_around_center(i, i + 1)  # чётная длина

    return s[start:end + 1]


# 8. Самый длинный палиндром через DP
def longest_palindrome_dp(s):

    n = len(s)
    if n == 0:
        return ""
    dp = [[False] * n for _ in range(n)]
    start, max_len = 0, 1

    # Каждая буква - палиндром длины 1
    for i in range(n):
        dp[i][i] = True

    # Проверяем подстроки длины 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Проверяем длины от 3 до n
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_len = length

    return s[start:start + max_len]
