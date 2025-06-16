#прошёл
def solution(arr1, arr2):
    """
    Сливает два отсортированных массива в один отсортированный массив.

    Args:
        arr1: первый отсортированный массив
        arr2: второй отсортированный массив

    Returns:
        новый отсортированный массив, содержащий все элементы из arr1 и arr2
    """
    result = []
    i, j = 0, 0

    # Сравниваем элементы и добавляем меньший в результат
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # Добавляем оставшиеся элементы из arr1
    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    # Добавляем оставшиеся элементы из arr2
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result