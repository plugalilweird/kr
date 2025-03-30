def fibonacci_generator(number):
    firstNumber = 0
    secondNumber = 1
    for currentIndex in range(number):
        yield firstNumber
        firstNumber, secondNumber = secondNumber, firstNumber + secondNumber

for currentNumber in fibonacci_generator(6):
    print(currentNumber)
