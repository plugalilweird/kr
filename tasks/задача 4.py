
string_and_substring = input().split()
if len(string_and_substring) < 2:
    string = string_and_substring[0]
    substring = input()
else:
    string = string_and_substring[0]
    substring = string_and_substring[1]

if substring == "":
    print(0)
else:
    count = 0
    for i in range(len(string)):
        match = True

        for j in range(len(substring)):
            if string[i + j] != substring[j]:
                match = False
                break
        if match:
            count += 1
    print(count)
