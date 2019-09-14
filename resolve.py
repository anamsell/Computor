import maths

def main(coefs):
    if coefs['max'] == 0:
        if coefs[0] == 0:
            print('Every real number are solution.')
        else:
            print("There is no solution.")
        exit()
    if coefs['max'] == 1:
        a, b = maths.irreductible_fraction(coefs[0] * -1, coefs[1])
        print('The solution is:')
        if b == 1:
            print(str(a))
        else:
            print(str(a) + '/' + str(b))
        exit()
    discriminant = coefs[1] * coefs[1] - 4 * coefs[2] * coefs[0]
    if discriminant < 0:
        print("There is no solution.")
        exit()
    if discriminant == 0:
        a, b = maths.irreductible_fraction(coefs[1] * -1, coefs[2] * 2)
        print('The solution is:')
        if b == 1:
            print(str(a))
        else:
            print(str(a) + '/' + str(b))
        exit()
    solution1 = (coefs[1] * -1 - maths.racine(discriminant)) / (2 * coefs[2])