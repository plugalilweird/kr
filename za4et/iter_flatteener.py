class FlattenIterator:
    def __init__(self, nested_list):
        self.stack = [iter(nested_list)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            try:
                currentElement = next(self.stack[-1])
            except StopIteration:
                self.stack.pop()
                continue
            if isinstance(currentElement, list):
                self.stack.append(iter(currentElement))
            else:
                return currentElement
        raise StopIteration

nested_list = [1, [2, [3, 4], 5], 6]
flat = FlattenIterator(nested_list)
for number in flat:
    print(number)
