#прошло
def solution(s):
    n = len(s)
    z = [0] * n

    for i in range(1, n):
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

    return z