def citire_date():
    """
Notam datele intr-o lista
    :return: lista
    """
    lst1 = []
    lst = input("Notati numerele listei si separati-le prin virgula: ")
    lista_separata = lst.split(',')
    for nr in lista_separata:
        lst1.append(int(nr))
    return lst1


def is_prime(n):
    """
Aflam daca numarul dat este prim
    :param n: numar intreg
    :return: True daca este prim, False daca nu este prim
    """
    if n < 2:
        return False
    else:
        for i in range(2, n//2 + 1):
            if n % i == 0:
                return False
    return True


def test_is_prime():
    assert is_prime(6) is False
    assert is_prime(7) is True
    assert is_prime(1095) is False


def get_longest_all_primes(lst):
    """
Determinam cea mai lunga subsecventa cu numere prime
    :param lst: lista data de user
    :return: lista cu numere prime
    """
    listi = []
    listf = []
    i = 0
    while i < len(lst):
        listi = []
        if is_prime(lst[i]):
            listi.append(lst[i])
            i += 1
            while i < len(lst):
                if is_prime(lst[i]):
                    listi.append(lst[i])
                    i += 1
                else:
                    i += 1
                    break
            if len(listi) > len(listf):
                listf = listi
        else:
            i += 1
    return listf


def test_get_longest_all_primes():
    assert get_longest_all_primes([1, 2, 3, 4, 5, 7, 11, 13, 17]) == [5, 7, 11, 13, 17]
    assert get_longest_all_primes([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 3]
    assert get_longest_all_primes([4, 5, 6, 8]) == [5]


def get_number_of_divisors(n):
    """
Determinam numarul de divizori
    :param n: un numar dat
    :return: numarul divizorilor
    """
    count = 2
    for i in range(2, n):
        if n % i == 0:
            count += 1
    return count


def test_get_number_of_divisors():
    assert get_number_of_divisors(4) == 3
    assert get_number_of_divisors(5) == 2
    assert get_number_of_divisors(6) == 4


def get_longest_same_div_count(lst):
    """
Determinam cea mai lunga subsecventa cu numere care au acealasi numar de divizori
    :param lst: lista data
    :return: lista cu numere care au acealsi numar de divizori
    """
    listi = []
    listf = []
    i = 0
    while i < len(lst):
        listi.append(lst[i])
        i += 1
        for x in range(i, len(lst)):
            if get_number_of_divisors(lst[i-1]) == get_number_of_divisors(lst[x]):
                listi.append(lst[x])
            else:
                if len(listi) > len(listf):
                    listf = listi
                listi = []
                i = x
                break
    return listf


def test_get_longest_same_div_count():
    assert get_longest_same_div_count([2, 3, 4, 5, 8]) == [2, 3]
    assert get_longest_same_div_count([12, 4, 13]) == [12]


def has_primes_digits(n):
    """
Determinam daca numarul dat are toate cifrele prime
    :param n: numarul dat
    :return: True daca are toate cifrele prime, False daca nu
    """
    while n != 0:
        if is_prime(n % 10):
            n = n // 10
        else:
            return False
    return True


def test_has_prime_digits():
    assert has_primes_digits(235) is True
    assert has_primes_digits(692) is False
    assert has_primes_digits(234) is False


def get_longest_prime_digits(lst):
    """
Determinam cea mai lunga subsecventa cu numere care au toate cifrele prime
    :param lst: lista data
    :return: lista cu numerele cu toate cifrele prime
    """
    listi = []
    listf = []
    i = 0
    while i < len(lst):
        if has_primes_digits(lst[i]):
            listi.append(lst[i])
            i += 1
            if i < len(lst):
                if has_primes_digits(lst[i]):
                    listi.append(lst[i])
                else:
                    if len(listi) > len(listf):
                        listf = listi
                    listi = []
            else:
                if len(listi) > len(listf):
                    listf = listi
        i += 1
    return listf


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([23, 25, 5, 56]) == [23, 25, 5]
    assert get_longest_prime_digits([4, 42, 2, 234, 5, 52, 57]) == [5, 52, 57]


def main():
    test_is_prime()
    test_get_longest_all_primes()
    test_get_number_of_divisors()
    test_get_longest_same_div_count()
    test_has_prime_digits()
    test_get_longest_prime_digits()
    lst = []
    while True:
        print("1. Citire date. ")
        print("2. Toate numerele sunt prime. ")
        print("3. Toate numerele au acelasi numar de divizori. ")
        print("4. Toate numerele sunt formate din cifre prime. ")
        print("x. Iesire")
        optiune = input("Alege optiunea: ")
        if optiune == "1":
            lst = citire_date()
        elif optiune == "2":
            print("Cea mai lunga subsecventa cu toate numerele prime este: ")
            print(get_longest_all_primes(lst))
        elif optiune == "3":
            print("Cea mai lunga subsecventa care are numerele cu acelasi numar de divizori este: ")
            print(get_longest_same_div_count(lst))
        elif optiune == "4":
            print("Cea mai lunga subsecventa cu numere cu cifre prime este: ")
            print(get_longest_prime_digits(lst))
        elif optiune == "x":
            break
        else:
            print("Reincercati")


if __name__ == "__main__":

    main()
