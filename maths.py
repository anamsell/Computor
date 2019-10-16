def num_after_point(x):
    s = str(x)
    if '.' not in s:
        return 0
    return len(s) - s.index('.') - 1


def modulo(a, b):
    return a - (int(a / b)) * b


def is_prime(nbr, prime_numbers):
    if nbr == 0 or nbr == 1:
        return 0
    for i in prime_numbers:
        if not modulo(nbr, i):
            return 0
    return 1


def get_next_prime(nbr, prime_numbers):
    while 1:
        if is_prime(nbr, prime_numbers):
            return nbr
        nbr += 1


def same_denominator(numerator1, denominator, numerator2, denominator2):
    gcd = find_gcd_euclide(denominator, denominator2)
    numerator1 *= denominator2 / gcd
    numerator2 *= denominator / gcd
    denominator = denominator * denominator2 / gcd
    return numerator1, denominator, numerator2, denominator


def square(nbr):
    i = 2
    prime_numbers = [2]
    coefficient = 1
    while i * i <= nbr:
        if not modulo(nbr, i * i):
            coefficient *= i
            nbr /= i * i
        else:
            i = get_next_prime(i + 1, prime_numbers)
            prime_numbers += [i]
    return nbr, coefficient


def find_gcd_euclide(a, b):
    if b == 0:
        return a
    return find_gcd_euclide(b, modulo(a, b))


def irreducible_fraction(numerator, denominator):
    if (float(numerator) / float(denominator)).is_integer():
        return int(numerator / denominator), 1
    multiple = num_after_point(numerator)
    tmp = num_after_point(denominator)
    if tmp > multiple:
        multiple = tmp
    tmp = 0
    while tmp < multiple:
        numerator *= 10
        denominator *= 10
        tmp += 1
    numerator = int(round(numerator))
    denominator = int(round(denominator))
    gcd = find_gcd_euclide(numerator, denominator)
    return int(numerator / gcd), int(denominator / gcd)


def get_lowest(a, b):
    if a == -1:
        return b
    if b == -1 or a <= b:
        return a
    return b


def absolute(number):
    if number > 0:
        return number
    else:
        return -number


def sign_number(number):
    if number > 0:
        return '+'
    else:
        return '-'
