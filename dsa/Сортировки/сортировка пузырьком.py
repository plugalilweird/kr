
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        flag = False

        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if not flag:
            break
    return arr

x=bubble_sort([3,2,5,6,4,1,8,9,0])
print(x)
