#прошел
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


def solution(root):
    def validate(node, min_val, max_val):
        if node is None:
            return True

        if node.data <= min_val or node.data >= max_val:
            return False

        return (validate(node.left, min_val, node.data) and
                validate(node.right, node.data, max_val))

    return validate(root, float('-inf'), float('inf'))
