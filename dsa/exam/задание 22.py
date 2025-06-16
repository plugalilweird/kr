#прошёл
def solution(s: str) -> list[int]:
    """
    Вычисляет префикс‑функцию (π) для строки s.
    Возвращает массив pi длины len(s), где
    pi[i] = длина наибольшего собственного префикса,
            совпадающего с суффиксом, оканчивающимся в i.
    """
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi
