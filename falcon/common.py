"""Metody i obiekty wielokrotnego użytku używane w różnych plikach."""


q = 12 * 1024 + 1 # q jest stała modulo, która jest używana w Falconie

# Podział wielomianu na dwa wielomiany
def split(f):
    n = len(f)
    f0 = [f[2 * i + 0] for i in range(n // 2)]
    f1 = [f[2 * i + 1] for i in range(n // 2)]
    return [f0, f1]

# Scalanie dwóch wielomianów w jeden
def merge(f_list):
    f0, f1 = f_list
    n = 2 * len(f0)
    f = [0] * n
    for i in range(n // 2):
        f[2 * i + 0] = f0[i]
        f[2 * i + 1] = f1[i]
    return f

# Kwadratowa norma euklidesowa wektora v
def sqnorm(v):
    res = 0
    for elt in v:
        for coef in elt:
            res += coef ** 2
    return res
