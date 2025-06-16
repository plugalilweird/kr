#прошел
def solution(s1, s2):
    """
    Возвращает длину наибольшей общей подпоследовательности двух строк s1 и s2.
    """
    n, m = len(s1), len(s2)
    if n == 0 or m == 0:
        return 0

    # Двухстрочный буфер размера m+1 для оптимизации памяти
    prev = [0] * (m + 1)
    curr = [0] * (m + 1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j-1])
        prev, curr = curr, prev

    return prev[m]
