import clean_string


def num_after_point(x):
    s = str(x)
    if not '.' in s:
        return 0
    return len(s) - s.index('.') - 1


def modulo(a, b):
    return a - (int(a) / int(b)) * b


def is_prime(nbr, prime_numbers):
    if nbr == 0 or nbr == 1:
        return 0
    for i in prime_numbers:
        if not modulo(nbr, i):
            return 0
    return 1


def get_next_prime(nbr, prime_numbers):
    if is_prime(nbr, prime_numbers):
        return nbr
    return get_next_prime(nbr + 1, prime_numbers)


def same_denominator(num1, denom, num2, denom2):
    gcd = find_gcd_euclide(denom, denom2)
    num1 *= denom2 / gcd
    num2 *= denom / gcd
    denom = denom * denom2 / gcd
    return num1, denom, num2, denom


def square(nbr):
    i = 2
    prime_numbers = [2]
    coef = 1
    while i * i <= nbr:
        if not modulo(nbr, i * i):
            coef *= i
            nbr /= i * i
        else:
            i = get_next_prime(i + 1, prime_numbers)
            prime_numbers += [i]
    return nbr, coef


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
