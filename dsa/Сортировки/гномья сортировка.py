def gnome_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr

x=gnome_sort([3,2,5,6,4,1,8,9,0])
print(x)
