class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Задание 1
"""
def build_tree(arr, i=0):
    if i >= len(arr):
        return None
    root = TreeNode(arr[i])
    root.left = build_tree(arr, 2 * i + 1)
    root.right = build_tree(arr, 2 * i + 2)
    return root



"""
Задание 2
"""
def is_symmetric(root):
    if not root:
        return True
    return is_mirror(root.left, root.right)

def is_mirror(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    return (left.val == right.val and
            is_mirror(left.left, right.right) and
            is_mirror(left.right, right.left))


"""
Задание 3
"""
def min_depth(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    if not root.left:
        return 1 + min_depth(root.right)
    if not root.right:
        return 1 + min_depth(root.left)
    return 1 + min(min_depth(root.left), min_depth(root.right))



"""
Задание 4
"""
def max_min_multiplication(arr):
    if len(arr) < 3:
        return -1

    # Находим самый левый лист (всегда идём влево)
    i = 1
    while 2 * i + 1 < len(arr):
        i = 2 * i + 1
    min_val = arr[i]

    # Находим самый правый лист (всегда идём вправо)
    i = 2
    while 2 * i + 2 < len(arr):
        i = 2 * i + 2
    max_val = arr[i]

    return min_val * max_val



"""
Задание 5
"""
def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)




# Пример массива
arr = [8, 9, 11, 7, 16, 3, 1]

# 1. Восстановление дерева
tree = build_tree(arr)

# 2. Симметричность
print("Симметрично?", is_symmetric(tree))  # True

# 3. Минимальная глубина
print("Мин. глубина:", min_depth(tree))   # 3

# 4. Произведение левого и правого листа
print("Произведение:", max_min_multiplication(arr))  # 81

# 5. Сравнение с копией
tree2 = build_tree(arr)
print("Деревья одинаковы?", is_same_tree(tree, tree2))  # True