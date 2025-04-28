def eratosthenes(n):
    primes = [True] * (n+1)
    primes[:2] = False, False

    for i in range (2, n+1):
        if primes[i]:
                primes[i*i:n+1:i] = [False] * len(primes[i*i:n+1:i])
    return [i for i in range(n+1) if primes[i]]

def prime_factor(a):
    primes = eratosthenes(a) # если мы считаем, что число изначально не должно быть простым, то int((a**0.5)+1)
    factors = dict()
    for i in range(len(primes)):
       while a % primes[i] == 0:
           factors[primes[i]] = factors.get(primes[i], 0) + 1
           a //= primes[i]
       if a == 1:
            break
    return factors





def gcd(a, b):
    fa = prime_factor(a)
    fb = prime_factor(b)
    nod = 1
    for i in fa:
        if i in fb:
            nod *= i**min(fa[i], fb[i])
    return nod
x=gcd(2600, 13)

print(x)
def mcd(a, b):
    fa = prime_factor(a)
    fb = prime_factor(b)
    prost = set(fa.keys()) | set(fb.keys())
    nod = 1
    for i in prost:
            nod *= i**max(fa.get(i, 0), fb.get(i, 0))
    return nod

x=mcd(121, 11)

print(x)