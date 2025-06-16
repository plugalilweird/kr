#проходит
def solution(root):
    result = []
    def preorder(node):
        if node:
            result.append(node.data)
            preorder(node.left)
            preorder(node.right)

    preorder(root)
    return result

