import maths
import clean_string
import class_number
from decimal import Decimal


def start(coefficients):
    if coefficients['max'] == 0:
        if coefficients[0] == 0:
            print('Every real number are solution.')
        else:
            print("There is no solution.")
        exit()
    if coefficients['max'] == 1:
        print("a = " + str(coefficients[1]) + ' | b = ' + str(coefficients[0]))
        print("The formula is : -b/a")
        print('The solution is:')
        print(clean_string.division(coefficients[0] * -1, coefficients[1]))
        exit()
    discriminant = Decimal(str(coefficients[1])) * Decimal(str(coefficients[1])) \
        - Decimal(4) * Decimal(str(coefficients[2])) * Decimal(str(coefficients[0]))
    print("a = " + str(coefficients[2]) + " | b = " + str(coefficients[1]) + " | " + "c = " + str(coefficients[0]))
    print("Discriminant: " + str(discriminant))
    numerator, denominator = maths.irreducible_fraction(coefficients[1] * -1, coefficients[2] * 2)
    if discriminant == 0:
        print("Discriminant is nul, the solution is:")
        print("-b/2a")
        print(clean_string.division(numerator, denominator))
        exit()
    if discriminant < 0:
        print("Discriminant is strictly negative, the two solutions in the complex number are:")
        print("(-b + " + u"\u221A" + '-' + u"\u0394" + ")/2a\n(-b - " + u"\u221A" + '-' + u"\u0394" + ")/2a")
        square_part1 = class_number.Number(numerator_square=-discriminant, denominator=2 * coefficients[2], real=0)
        square_part2 = class_number.Number(numerator=-1, numerator_square=-discriminant,
                                           denominator=2 * coefficients[2], real=0)
    else:
        print("Discriminant is strictly positive, the two solutions are:")
        print("(-b + " + u"\u221A" + u"\u0394" + ")/2a\n(-b - " + u"\u221A" + u"\u0394" + ")/2a")
        square_part1 = class_number.Number(numerator_square=discriminant, denominator=2 * coefficients[2])
        square_part2 = class_number.Number(numerator=-1, numerator_square=discriminant, denominator=2 * coefficients[2])

    rational_part = class_number.Number(numerator=-coefficients[1], denominator=2 * coefficients[2])
    class_number.Result(rational_part, square_part1)
    class_number.Result(rational_part, square_part2)
