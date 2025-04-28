def euclidius(m, n):
    r = m % n
    while r != 0:
        m, n = n,r
        r = m % n
    return n




def reverse_modulus(a,c):
    for b in range(c):
        if a*b%c == 1:
            return b



def get_keys(p, q):
    N = p*q
    fi =(p-1) * (q-1)
    e = 2
    while euclidius(fi, e) == 1:
        e += 1
    d = reverse_modulus(e, fi)
    return (e, N), (d, N)
x=get_keys(3557, 2579)
print(x)