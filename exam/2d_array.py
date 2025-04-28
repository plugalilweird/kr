def min2DArray(nums: list):
    frequency = {}
    for number in nums:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

    max_frequency = 0
    for count in frequency.values():
        if count > max_frequency:
            max_frequency = count

    result_rows = [[] for _ in range(max_frequency)]

    next_row_index = {}
    for number in frequency:
        next_row_index[number] = 0

    for number in nums:
        row_index = next_row_index[number]
        result_rows[row_index].append(number)
        next_row_index[number] += 1

    return result_rows



print(min2DArray([1, 3, 4, 1, 2, 3, 1]))  # [[1, 3, 4, 2], [1, 3], [1]]
print(min2DArray([1, 2, 3, 4]))  # [[1, 2, 3, 4]]
