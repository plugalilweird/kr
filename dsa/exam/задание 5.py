#прошёл
class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

def solution(root):
    """
    Считает число «тупиковых» (dead‐end) листьев в BST, где тупиковый лист
    — это такой лист, у которого НЕЛЬЗЯ вставить ни левого, ни правого ребёнка,
    не нарушив свойство BST. В дереве считается, что ключи — это целые числа
    без верхней/нижней границы (−∞ … +∞), но при этом ребенок должен сохранять
    порядок: left < parent < right.

    Идея: при рекурсивном обходе мы передаем вниз текущие границы (low, high)
    для узлов: все ключи в поддереве должны лежать строго между low < key < high.
    Если в какой‐то момент наткнулись на лист L с ключом v и одновременно
      (v – low == 1) и (high – v == 1),
    то именно для этого листа нет НИ ОДНОГО целого x, которое low < x < v или v < x < high.
    Следовательно, L — мёртвый (dead‐end) узел.

    Пояснение на примерах из задачи:

      1) Дерево 2
                 / \
                1   3

         - Для листа 1: (low, high) = (−∞, 2).
           Между −∞ и 1 есть «достаточно» чисел (… 0, −1, −2 …), значит левого/правого
           ребенка добавить можно. v−low != 1 (скажем, 1−(−∞) ≠ 1). => не dead‐end.
         - Для листа 3: (low, high) = (2, +∞).
           Между 3 и +∞ — «много» чисел (4, 5, …), значит вставить ребёнка вправо возможно.
           => не dead‐end. Ответ = 0.

      2) Дерево 2
                 / \
                1   4
                   /
                  3

         - Лист 1: (low, high) = (−∞, 2).
           Между −∞ и 1 есть целые (… 0…), значит не тупик.
         - Лист 3: (low, high) = (2, 4).
           Между 2 и 3 нет других целых (2 < x < 3) и между 3 и 4 тоже нет (3 < x < 4).
           => тупиковый лист. Ответ = 1.

    Сложность: O(n) по времени, O(h) по стеку рекурсии (h — высота дерева).

    """
    def dfs(node, low, high):
        if node is None:
            return 0

        # Если это лист: проверяем, нельзя ли туда вставить ни слева, ни справа.
        if node.left is None and node.right is None:
            dead = False
            # Проверяем левую «дыру»: нужно v−low == 1 (и low != None),
            # иначе есть по крайней мере одно целое между low и v.
            if low is not None and node.data - low == 1:
                left_impossible = True
            else:
                left_impossible = False

            # Проверяем правую «дыру»: нужно high−v == 1 (и high != None),
            # иначе есть целое между v и high.
            if high is not None and high - node.data == 1:
                right_impossible = True
            else:
                right_impossible = False

            # Leaf тупиковый, если НИ левого, НИ правого дочернего значения вставить нельзя:
            if left_impossible and right_impossible:
                dead = True

            return 1 if dead else 0

        # Иначе рекурсивно спускаемся в поддеревья, обновляем границы:
        cnt = 0
        # В левое поддерево: все ключи < node.data, > low
        cnt += dfs(node.left, low, node.data)
        # В правое поддерево: все ключи > node.data, < high
        cnt += dfs(node.right, node.data, high)
        return cnt

    # Начальные границы: no lower bound (None), no upper bound (None)
    return dfs(root, None, None)


# Пример 1 из условия:
root1 = TreeNode(2, TreeNode(1), TreeNode(3))
print(solution(root1))  # 0

# Пример 2 из условия:
#     2
#    / \
#   1   4
#      /
#     3
root2 = TreeNode(2,
                 TreeNode(1),
                 TreeNode(4, TreeNode(3)))
print(solution(root2))  # 1
