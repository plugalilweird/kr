#прошёл
def solution(n):
    if n == 0 or n == 1:
        return 1
    if n % 2 == 0:
        return solution(n // 2) + solution(n // 2 - 1)
    else:
        return solution(n // 2) - solution(n // 2 - 1)

print(solution())