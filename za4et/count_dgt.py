def count_digit(number):
    numberString = str(number)
    digitCount = {}
    for currentDigit in numberString:
        if currentDigit in digitCount:
            digitCount[currentDigit] += 1
        else:
            digitCount[currentDigit] = 1

    return digitCount
