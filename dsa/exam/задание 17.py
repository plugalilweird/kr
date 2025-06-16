#прошел
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


def solution(arr):
    """
    Строит бинарное дерево из массива arr длины n,
    где для узла с индексом i:
      left  = 2*i + 1,
      right = 2*i + 2.
    Элемент None означает отсутствие узла.
    Возвращает корень дерева или None, если arr пуст или arr[0] is None.
    """
    n = len(arr)
    if n == 0 or arr[0] is None:
        return None

    # Создаём список вершин (или None)
    nodes = [TreeNode(val) if val is not None else None for val in arr]

    # Связываем потомков
    for i, node in enumerate(nodes):
        if node is None:
            continue
        left_i = 2 * i + 1
        right_i = 2 * i + 2
        if left_i < n:
            node.left = nodes[left_i]
        if right_i < n:
            node.right = nodes[right_i]

    return nodes[0]