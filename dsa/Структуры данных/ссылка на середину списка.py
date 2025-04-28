from __future__ import annotations


class Node:
    def __init__(self, data, next: Node = None):
        self.data = data
        self.next = next
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))

n = 1
current = head
while current.next:
    n += 1
    current = current.next
current = head
for _ in range(n//2):
    current = current.next
print(current.data)
