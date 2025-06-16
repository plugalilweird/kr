class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


def solution(root, min_val=1, max_val=100):
    def dfs(node, low, high):
        if node is None:
            return 0

        # Если лист
        if node.left is None and node.right is None:
            # Проверяем, можно ли добавить потомка слева
            can_add_left = (low is None or node.data > low + 1)
            # Проверяем, можно ли добавить потомка справа
            can_add_right = (high is None or node.data < high - 1)
            # Если нельзя добавить ни слева, ни справа — тупиковый лист
            if not can_add_left and not can_add_right:
                return 1
            else:
                return 0

        # Рекурсивно считаем в левом и правом поддеревьях с обновлёнными границами
        left_count = dfs(node.left, low, node.data)
        right_count = dfs(node.right, node.data, high)
        return left_count + right_count

    return dfs(root, None, None)
