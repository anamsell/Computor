import maths
import clean_string
import class_number
from decimal import Decimal


def start(coefs):
    if coefs['max'] == 0:
        if coefs[0] == 0:
            print('Every real number are solution.')
        else:
            print("There is no solution.")
        exit()
    if coefs['max'] == 1:
        numerator, denominator = maths.irreducible_fraction(coefs[0] * -1, coefs[1])
        print("a = " + str(coefs[1]) + ' | b = ' + str(coefs[0]))
        print("The formula is : -b/a")
        print('The solution is:')
        print(clean_string.division(numerator, denominator))
        exit()
    discriminant = Decimal(str(coefs[1])) * Decimal(str(coefs[1])) - Decimal(4) * Decimal(str(coefs[2])) * Decimal(str(coefs[0]))
    print("a = " + str(coefs[2]) + " | b = " + str(coefs[1]) + " | " + "c = " + str(coefs[0]))
    print("Discriminant: " + str(discriminant))
    numerator, denominator = maths.irreducible_fraction(coefs[1] * -1, coefs[2] * 2)
    if discriminant == 0:
        print("Discriminant is nul, the solution is:")
        print("-b/2a")
        print(clean_string.division(numerator, denominator))
        exit()
    if discriminant < 0:
        print("Discriminant is strictly negative, the two solutions in the complex number are:")
        print("(-b + " + u"\u221A" + '-' + u"\u0394" + ")/2a\n(-b - " + u"\u221A" + '-' + u"\u0394" + ")/2a")
        square_part1 = class_number.Number(numerator_square=-discriminant, denominator=2*coefs[2], real=0)
        square_part2 = class_number.Number(numerator=-1, numerator_square=-discriminant, denominator=2*coefs[2], real=0)
    else:
        print("Discriminant is strictly positive, the two solutions are:")
        print("(-b + " + u"\u221A" + u"\u0394" + ")/2a\n(-b - " + u"\u221A" + u"\u0394" + ")/2a")
        square_part1 = class_number.Number(numerator_square=discriminant, denominator=2*coefs[2])
        square_part2 = class_number.Number(numerator=-1, numerator_square=discriminant, denominator=2*coefs[2])

    rational_part = class_number.Number(numerator=-coefs[1], denominator=2*coefs[2])
    class_number.Result(rational_part, square_part1)
    class_number.Result(rational_part, square_part2)
