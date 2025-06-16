#прошел
def solution(arr, x):
    """
    Возвращает наименьший индекс, по которому нужно вставить x в
    отсортированный список arr, чтобы сохранить порядок.
    """
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left
