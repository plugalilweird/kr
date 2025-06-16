#прошёл
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


def solution(root):
    result = []

    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append(node.data)
        inorder(node.right)

    inorder(root)
    return result


print(solution(TreeNode(2, TreeNode(3), TreeNode(5))))
