"""Проверить, является ли список циклическим
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    # Если список пустой или состоит из одного элемента без связи — цикла нет
    if not head or not head.next:
        return False

    # Догонялки
    slow = head          # догоняемый
    fast = head.next     # догоняющий (на шаг вперёд)

    # Пока они не встретились
    while slow != fast:
        # Если догоняющий уткнулся в конец — цикла нет
        if not fast or not fast.next:
            return False
        # догоняемый делает 1 шаг
        slow = slow.next
        # догоняющий делает 2 шага
        fast = fast.next.next

    # Если цикл есть — они встретились
    return True


# # Создаём обычный список
# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(3)
# n1.next = n2
# n2.next = n3
# print(has_cycle(n1))  # False
#
# # Создаём циклический
# n3.next = n2
# print(has_cycle(n1))  # True


"""Развернуть односвязный список"""
def reverse_linked_list(head):
    prev = None      # до начала — никого
    current = head   # начинаем с головы

    while current is not None:
        next_node = current.next  # запоминаем следующего
        current.next = prev       # разворачиваем стрелку назад
        prev = current            # двигаем prev вперёд
        current = next_node       # двигаем current вперёд

    # Теперь prev — это новая голова
    return prev

# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(3)
# n1.next = n2
# n2.next = n3
#
# # Разворачиваем
# new_head = reverse_linked_list(n1)


"""Найти середину списка"""
def middle_node(head):
    slow = fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow


# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(3)
# n4 = ListNode(4)
# n5 = ListNode(5)
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
#
# mid = middle_node(n1)
# print(mid.val)

"""Удалить элемент из односвязного списка"""
def remove_elements(head, val):
    pass
    dumm = ListNode()
    dumm.next = head
    prev = dumm
    current = head
    while current != None:
        if current.val == val:
            prev.next = current.next
        else:
            prev = current
        current = current.next

    return dumm.next


# n1 = ListNode(1)
# n2 = ListNode(2)
# n6a = ListNode(6)
# n3 = ListNode(3)
# n4 = ListNode(4)
# n5 = ListNode(5)
# n6b = ListNode(6)
#
# n1.next = n2
# n2.next = n6a
# n6a.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6b
#
# def print_list(head):
#     res = []
#     while head:
#         res.append(head.val)
#         head = head.next
#     return res

# print(print_list(n1))
# new_head = remove_elements(n1, 6)
# print(print_list(new_head))




"""Является ли одна строка исходной для другой"""
def is_subsequence(a, b):
    i = 0
    j = 0

    while i < len(a)-1 and j < len(b)-1:
        if a[i]==b[j]:
            i+=1
        j+=1
    return i == len(a)

# print(is_subsequence("ace", "abcde"))
# print(is_subsequence("aec", "abcde"))
# print(is_subsequence("", "abc"))
# print(is_subsequence("abc", ""))



"""Является ли слово палиндромом?"""
def isPalindrome(word):
    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False
        left +=1
        right -=1

    return True

# print(isPalindrome("asddsa"))
# print(isPalindrome("asdsa"))
# print(isPalindrome("asddssa"))

"""Слияние двух отсортированных списков"""
def last_zadanie(list1, list2):
    dummy = ListNode(0)
    current = dummy
    while list1 != None and list2 != None:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    if list1 == None:
        current.next = list2
    else:
        current.next = list1
    return dummy.next

# # list1
# l1 = ListNode(3)
# l1.next = ListNode(6)
# l1.next.next = ListNode(8)
#
# # list2
# l2 = ListNode(4)
# l2.next = ListNode(7)
# l2.next.next = ListNode(9)
# l2.next.next.next = ListNode(11)
#
# res = last_zadanie(l1, l2)
#
# def print_list(head):
#     res = []
#     while head:
#         res.append(head.val)
#         head = head.next
#     return res
#
# print(print_list(res))