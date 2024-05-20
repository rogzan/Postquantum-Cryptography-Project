# Postquantum-Cryptography-Project

Algorytm CFPKM (Cross-Fire Prime Key Exchange) to algorytm wymiany kluczy kryptograficznych, który wykorzystuje wielomiany jako główny mechanizm bezpieczeństwa. W skrócie, polega on na wymianie klucza publicznego między dwoma stronom i generowaniu wspólnego sekretu, który może być następnie wykorzystany do bezpiecznej komunikacji.

Algorytm CFPKM jest oparty na teorii wielomianów, a kluczową koncepcją jest ocena wielomianów przy użyciu losowych wartości oraz operacje na wielomianach. Bezpieczeństwo algorytmu opiera się na trudności rozwiązania problemu wielomianów nad ciałem skończonym.

Najważniejsze elementy algorytmu CFPKM:
•	Generowanie kluczy: Algorytm rozpoczyna się od wygenerowania pary kluczy: klucza prywatnego i klucza publicznego. Klucz prywatny jest przechowywany tylko przez jedną stronę, podczas gdy klucz publiczny jest udostępniany drugiej stronie do celów szyfrowania.
•	Szyfrowanie: Aby zaszyfrować wiadomość dla drugiej strony, strona wysyłająca używa klucza publicznego drugiej strony do przekształcenia wiadomości. Ten proces obejmuje ocenę wielomianów na podstawie losowych wartości oraz dodanie błędów dla zwiększenia bezpieczeństwa.
•	Deszyfrowanie: Strona docelowa otrzymuje zaszyfrowaną wiadomość i używa swojego klucza prywatnego do odtworzenia wspólnego sekretu, który następnie może być wykorzystany do odszyfrowania wiadomości.

Opis funkcji:

__init__ (klasa Pol):
Inicjalizuje obiekt wielomianu z predefiniowaną strukturą. Tablica QD reprezentuje współczynniki kwadratowe, tablica L reprezentuje współczynniki liniowe, a C to stały wyraz.

randombytes(length):
Generuje sekwencję losowych bajtów o długości length za pomocą funkcji os.urandom.

polgen(f, m, n):
Generuje system wielomianów. Dla każdego wielomianu w systemie losowane są współczynniki kwadratowe, liniowe i stała, a następnie przypisywane do odpowiednich pól w obiekcie wielomianu.

pack_sk(sk, sa, seed):
Pakuje klucz prywatny. Kopiuje seed i wartość tajną sa do tablicy sk.

pack_pk(pk, b1, seed):
Pakuje klucz publiczny. Kopiuje seed do tablicy pk, a następnie współczynniki b1 w formie bajtów.

pack_ct(ct, b2, c):
Pakuje tekst zaszyfrowany. Kopiuje wektor c i współczynniki b2 do tablicy ct w formie bajtów.

unpack_sk(sa, seed, sk):
Rozpakowuje klucz prywatny. Kopiuje seed i wartość tajną sa z tablicy sk.

unpack_pk(b1, seed, pk):
Rozpakowuje klucz publiczny. Kopiuje seed z tablicy pk, a następnie odczytuje współczynniki b1 z tablicy pk.

unpack_ct(b2, c, ct):
Rozpakowuje tekst zaszyfrowany. Kopiuje wektor c z tablicy ct, a następnie odczytuje współczynniki b2 z tablicy ct.

evaluate_poly(unPoly, pValue):
Ocena wartości wielomianu. Oblicza wartość wielomianu unPoly dla wektora pValue.

eval_sys(pSyst, pValue):
Ocena systemu wielomianów. Oblicza wartości wszystkich wielomianów w systemie pSyst dla wektora pValue.

rounding(in_val):
Zaokrągla wartość in_val poprzez obliczenie reszty z dzielenia i przesunięcie bitowe.

kem_crossround1(in_val):
Zaokrągla wartość in_val poprzez przesunięcie bitowe i obliczenie reszty z dzielenia przez 2.

pack_str(S):
Pakuje tekst S do formatu bajtowego w kodowaniu UTF-8.

unpack_str(S):
Odpakowuje tekst S z formatu bajtowego do kodowania UTF-8.

generate_keypair():
Generuje parę kluczy (publiczny i prywatny). Tworzy losowe seed i sa, generuje system wielomianów, a następnie pakuje klucze do odpowiednich tablic pk i sk.

encrypt(pk, plaintext):
Szyfruje plaintext za pomocą klucza publicznego pk. Generuje losowe wartości, oblicza wartości wielomianów, dodaje błędy i pakuje zaszyfrowany tekst oraz klucz współdzielony.

decrypt(sk, ct):
Deszyfruje zaszyfrowany tekst ct za pomocą klucza prywatnego sk. Rozpakowuje zaszyfrowane wartości, oblicza wartości wielomianów, oblicza wektor błędów i zwraca klucz współdzielony.
