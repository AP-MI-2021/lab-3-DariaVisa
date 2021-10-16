def citire_date():
    """
Notam numerele in lista
    :param lst: lista
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
        for i in range(2, n//2 +1):
            if n % i == 0:
                return False
    return True


def test_is_prime():
    assert is_prime(6) is False
    assert is_prime(7) is True
    assert is_prime(1095) is False


def get_longest_all_primes(lst):
    listi = []
    listf = []
    # for x in lst:
    #     if is_prime(x):
    #         listi.append(x)
    i = 0
    #  0  1   2  3  4
    # [1, 3, 5, 7, 8, 2,5]
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
                    i+=1
                    break
            if len(listi) > len(listf):
                listf = listi

        else:
            i += 1
    return listf


def get_number_of_divisors(n):
    count = 2
    for i in range(2, n):
        if n % i == 0:
            count += 1
    return count


def get_longest_same_div_count(lst):

    # [1,2,3, 4, 6, 25]

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


def has_primes_digits(n):

    # 1234 => 4 = %10 ,  1234/10 => 123, 1234/100 =>12, 1234/10%10
    # 1233 % 10 => 4,  1234 / 10 = 123   123/10 = 12 12/10 =1  1/10 =0

    while n != 0:
        if is_prime(n % 10):
            n = n // 10
        else:
            return False
    return True


def get_longest_prime_digits(lst):
    # [12, 1234, 125, 127, 123]
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


def main():
    test_is_prime()
    l = []
    while True:
        print("1. Citire date. ")
        print("2. Toate numerele sunt prime. ")
        print("3. Toate numerele au acelasi numar de divizori. ")
        print("4. Toate numerele sunt fomrate din cifre prime. ")
        print("x. Iesire")
        optiune = input("Alege optiunea: ")
        if optiune == "1":
            l = citire_date()
        elif optiune == "2":
            print(get_longest_all_primes(l))
        elif optiune == "3":
            print(get_longest_same_div_count(l))
        elif optiune == "4":
            print(get_longest_prime_digits(l))
        elif optiune == "x":
                break
        else:
            print("Reincercati")

if __name__ == "__main__":

    main()
