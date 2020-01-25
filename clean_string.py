import re
import maths


def reduce_form(coefficients):
    lst = coefficients.copy()
    del lst['max']
    lst = sorted(lst)
    string = ''
    for degree in lst:
        if coefficients[degree] != 0:
            string += maths.sign_number(coefficients[degree]) + \
                      ' ' + str(maths.absolute(coefficients[degree])) + 'X^' + str(degree) + ' '
            coefficients['max'] = degree
    string = re.sub(r"X\^0", '', string)
    string = re.sub(r" 1X", ' X', string)
    string = re.sub(r"\^1", '', string)
    if not string:
        return '0'
    if string[0] == '+':
        return string[2:]
    return '-' + string[2:]


def get_string(rational, square, char_real):
    printable_fraction = ''
    rational = maths.absolute(rational)
    if rational != 1 or (square == 1 and char_real == ''):
        printable_fraction += str(change_number_to_int(rational))
    printable_fraction += char_real
    if square != 1 and rational != 0:
        printable_fraction += u"\u221a" + str(change_number_to_int(square))
    return printable_fraction


def change_number_to_int(number):
    if type(number) is float and number.is_integer():
        return int(number)
    else:
        return number


def change_coefficients_to_int(coefficients):
    for degree in coefficients:
        if type(coefficients[degree]) is float and coefficients[degree].is_integer():
            coefficients[degree] = change_number_to_int(coefficients[degree])


def division(numerator, denominator):
    numerator, denominator = maths.irreducible_fraction(numerator, denominator)
    if denominator == 1:
        return str(numerator)
    else:
        return str(numerator) + '/' + str(denominator)


def entry(parts_equation):
    parts_equation[0] = parts_equation[0].strip()
    parts_equation[0] = re.sub(r" +", r" ", parts_equation[0])
    parts_equation[1] = parts_equation[1].strip()
    parts_equation[1] = re.sub(r" +", r" ", parts_equation[1])
