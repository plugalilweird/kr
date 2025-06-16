#проход
def solution(arr):
    MOD = 1_000_000_007
    n = len(arr)

    if n == 0:
        return 0
    if n == 1:
        return arr[0] % MOD

    digits = sorted(arr) # если честно я не уверен, что так можно делать

    num1 = 0
    num2 = 0

    for i, d in enumerate(digits):
        if i & 1 == 0:
            num1 = (num1 * 10 + d) % MOD
        else:
            num2 = (num2 * 10 + d) % MOD

    return (num1 + num2) % MOD
