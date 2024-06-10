"""
Metoda compress kompresuje listę całkowitych v do ciągu bajtów o długości slen.
Każdy współczynnik v jest kodowany w następujący sposób:

 - Znak (dodatni lub ujemny) jest kodowany na 1 bicie.
 - 7 najmniej znaczących bitów współczynnika jest kodowanych binarnie.
 - Najbardziej znaczące bity są kodowane w kodowaniu unarnym (jeden bit 1 na końcu).

Jeśli skompresowany ciąg jest dłuższy niż slen bajtów, funkcja zwraca False.
"""

def compress(v, slen):
    u = ""
    for coef in v:
        # Kodowanie znaku
        s = "1" if coef < 0 else "0"
        # Kodowanie niskich bitów
        s += format((abs(coef) % (1 << 7)), '#09b')[2:]
        # Kodowanie wysokich bitów
        s += "0" * (abs(coef) >> 7) + "1"
        u += s
    if len(u) > 8 * slen:
        return False
    u += "0" * (8 * slen - len(u))
    w = [int(u[8 * i: 8 * i + 8], 2) for i in range(len(u) // 8)]
    x = bytes(w)
    return x

"""
Metoda decompress dekompresuje ciąg bajtów x do listy całkowitych v o długości n.
Przyjmuje jako argumenty kodowanie x, długość w bajtach slen i długość n oczekiwanego wyniku.
Jeśli długość x przekracza slen lub dekompresja nie jest możliwa, funkcja zwraca False.
"""
def decompress(x, slen, n):
    # Sprawdzenie, czy długość x przekracza slen
    if (len(x) > slen):
        print("Za długie")
        return False
    w = list(x)
    u = ""
    for elt in w:
        u += bin((1 << 8) ^ elt)[3:]
    v = []

    # Usuń ostatnie bity
    while u[-1] == "0":
        u = u[:-1]

    try:
        while (u != "") and (len(v) < n):
            # Odzyskaj znak współczynnika
            sign = -1 if u[0] == "1" else 1
            # Odzyskaj 7 niskich bitów abs(coef)
            low = int(u[1:8], 2)
            i, high = 8, 0
            # Odzyskaj wysokie bity abs(coef)
            while (u[i] == "0"):
                i += 1
                high += 1
            # Oblicz współczynnik
            coef = sign * (low + (high << 7))
            # Wymuś unikalne kodowanie dla coef = 0
            if (coef == 0) and (sign == -1):
                return False
            # Przechowaj wyniki pośrednie
            v += [coef]
            u = u[i + 1:]
        # W tym przypadku kodowanie jest nieprawidłowe
        if (len(v) != n):
            return False
        return v
    # IndexError jest zgłaszany, gdy indeksy są poza zakresem tablicy
    except IndexError:
        return False
