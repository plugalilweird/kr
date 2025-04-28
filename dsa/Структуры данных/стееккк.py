def check_parenthesis(seq):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in seq:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    return not stack



print(check_parenthesis(")"))



def check_parenthesis_1(seq):
    stack = []
    pairs = {'(': ')', '{': '}', '[': ']'}

    for i in seq:
        if i in pairs:
            stack.append(i)
        else:
            if not stack:
                return False
            j = stack.pop()
            if pairs[j] != i:
                return False
    if stack:
        return False
    return True

print(check_parenthesis_1("[}"))