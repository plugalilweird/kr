#Вычисляем A * BmodC для всмех B от 0 до C-1
#Обратным числом для AmodC будет являться такое число B, для которого A * BmodC = 1
#обратите внимание, что BmodC может принимать значения от 0 до C-1, поэтому нет смысла проверять числа больше, чем B.

def reverse_modulus(a, c):
    for b in range(c):
        if a*b%c == 1:
            return b
x = reverse_modulus(5,3)
print(x)