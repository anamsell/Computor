def racine(number):
    

def modulo(a,b):
    return a - (int(a)/int(b)) * b

def find_gcd_Euclide(a, b):
    if b == 0:
        return a
    return find_gcd_Euclide(b, modulo(a, b))

def irreductible_fraction(numerator, denominator):
    if (float(numerator)/float(denominator)).is_integer():
        return int(numerator/denominator), 1
    while not (float(numerator).is_integer() and float(denominator).is_integer()):
        numerator *= 10
        denominator *= 10
    gcd = find_gcd_Euclide(numerator, denominator)
    return int(numerator/gcd), int(denominator/gcd)

def get_lowest(a, b):
    if a == -1:
        return b
    if b == -1 or a <= b:
        return a
    return b

def absol(number):
    if number > 0:
        return number
    else:
        return -number

def signe_number(number):
    if number > 0:
        return '+'
    else:
        return '-'