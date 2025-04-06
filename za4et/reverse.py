def reverseString(string: str, length: int):
    result_list = []
    for index in range(0, len(string), 2 * length):
        block = string[index:index + 2 * length]
        swapped_block = block[:length][::-1] + block[length:]
        result_list.append(swapped_block)
    return "".join(result_list)

print(reverseString("abcdefg", 2))
print(reverseString("abcd", 2))
print(reverseString("abc", 3))