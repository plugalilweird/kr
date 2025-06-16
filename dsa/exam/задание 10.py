#тесты прошёл
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


def solution(root):
    if root is None:
        return 0

    left_height = solution(root.left)
    right_height = solution(root.right)

    return max(left_height, right_height) + 1

assert solution(TreeNode(2, TreeNode(1), TreeNode(3))) == 2