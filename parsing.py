import re
import maths


def add_coefficient_to_associate_degree(value, sign, coefficient, coefficients):
    try:
        degree = int(re.search(r"\^ ?\d+(\.\d+)? ?", value).group()[1:])
    except AttributeError:
        degree = 1
    try:
        coefficients[degree]
    except KeyError:
        coefficients[degree] = coefficient * sign
    else:
        coefficients[degree] += coefficient * sign


def searching_numbers(value, sine, coefficients):
    if re.search(r"^ ?\d+(\.\d+)? ?$", value):
        coefficients[0] += float(value) * sine
    elif re.search(r"^ ?X( ?\^ ?\d+)? ?$", value):
        add_coefficient_to_associate_degree(value, sine, 1, coefficients)
    elif re.search(r"^ ?\d+(\.\d+)?( ?\* ?)?X( ?\^ ?\d+)? ?$", value)\
            or re.search(r"^ ?X( ?\^ ?\d+)? ?\* ?\d+(\.\d+)? ?$", value):
        coefficient = float(re.search(r"(^|[^\^ ?0123456789]) ?\d+(\.\d+)?", value).group().replace('*', ''))
        if not coefficient:
            return
        add_coefficient_to_associate_degree(value, sine, coefficient, coefficients)
    else:
        print('Error : incorrect syntax : ' + '\'' + value.strip() + '\'.')
        exit()


def start(parts_equation, coefficients):
    for idx, part in enumerate(parts_equation):
        sine = 1
        if not part:
            print("Error, each part of the equation must contain 1 number or more.")
            exit()
        if part[0] == '-' or part[0] == '+':
            if part[0] == '-':
                sine = -1
            part = part[1:]
        if idx == 1:
            side = -1
        else:
            side = 1
        while 1:
            a = part.find('+')
            b = part.find('-')
            if a == -1 and b == -1:
                searching_numbers(part, sine * side, coefficients)
                break
            c = maths.get_lowest(a, b)
            value = part[:c]
            searching_numbers(value, sine * side, coefficients)
            if part[c] == '-':
                sine = -1
            else:
                sine = 1
            part = part[c + 1:]
