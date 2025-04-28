#дан неупорядоченный список. необходимо вернуть k наименьших элементов списка


import heapq

def k_smallest(lst, k):
    heapq.heapify(lst)


    return [heapq.heappop(lst) for _ in range(k)]


print(k_smallest([6, 4, 2, 1, 7, 3, 8, 9, 5], 7))


#дан неупорядоченный список. необходимо вернуть k наибольших элементов списка

def k_largest(lst, k):
    lst = [ -i for i in lst]
    heapq.heapify(lst)
    return [-heapq.heappop(lst) for _ in range(k)]

print(k_largest([6, 4, 2, 1, 7, 3, 8, 9, 5], 7))


def helper(lst, root):
    max_val = root

    if 2 * root + 1 < len(lst) and lst[max_val] < lst[2*root+1]:
        max_val = 2 * root + 1
    if 2 * root + 1 < len(lst) and lst[max_val] < lst[2 * root + 2]:
        max_val = 2 * root + 2
    if root != max_val:
        lst[root], lst[max_val] = lst[max_val], lst[root]
        helper(lst, max_val)



def heapify(lst):
    for i in range(len(lst) // 2+1, -1, -1):
        helper(lst, i)

def heappop(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    res = lst.pop()

    helper(lst, 0)

    return res

lst = [6, 4, 2, 1, 7, 3, 8, 9, 5]
heapify(lst)
while lst:
    print(heappop(lst))