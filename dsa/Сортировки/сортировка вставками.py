
def insertion_sort(arr):
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1

        while arr[j] > x and j >= 0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = x
    return arr
x=insertion_sort([3,2,5,6,4,1,8,9,0])
print(x)





def insertion_sort_1(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1]>arr[i]:
            j -=1
        a = arr[i]
        for k in range(i-1, j-1, -1):
            arr[k+1]=arr[k]
        arr[j]=a
    return arr

z=insertion_sort_1([3,2,5,6,4,1,8,9,0])
print(z)



def insertion_sort_2(arr): # вариант зернова // без бинарного поиска
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1]>arr[i]:
            j -=1
        arr[j], arr[j+1 : i + 1] = arr[i], arr[j:i]
    return arr


y=insertion_sort_2([3,2,5,6,4,1,8,9,0])
print(y)



def binary_search(arr, x):
    l = 0
    u = len(arr)
    while u > l:
        i = (l+u)//2
        if arr[i] == x:
            return i
        elif arr[i] < x:
            l = i + 1
        elif arr[i] > x:
            u = i - 1
    return
zz=binary_search([3,2,5,6,4,1,8,9,0], 2)
print(zz)