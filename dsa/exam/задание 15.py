#прошел
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


def solution(root):
    if root is None:
        return []

    result = []

    result.extend(solution(root.left))
    result.extend(solution(root.right))
    result.append(root.data)

    return result