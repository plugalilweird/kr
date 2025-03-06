def parenthless(string: str):
    stack = []
    pairs = {')' : '(','}' : '{', ']' : '['}


    for char in string:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    return not stack

x = parenthless('[]')
print(x)