# для одного слова, c маленькой буквы


def palindrome(string: str):
    for left_index in range(len(string)):
        right_index = len(string) - 1 - left_index
        if string[left_index] != string[right_index]:
            return False
    else:
        return True

print(palindrome('анна'))



