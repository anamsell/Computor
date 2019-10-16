import re
import maths


def add_coef_to_associate_degree(value, signe, coef, coefs):
    try:
        degree = int(re.search(r"\^ ?\d+(\.\d+)? ?", value).group()[1:])
    except AttributeError:
        degree = 1
    try:
        coefs[degree]
    except KeyError:
        coefs[degree] = coef * signe
    else:
        coefs[degree] += coef * signe


def searching_numbers(value, sine, coefs):
    if re.search(r"^ ?\d+(\.\d+)? ?$", value):
        coefs[0] += float(value) * sine
    elif re.search(r"^ ?X( ?\^ ?\d+)? ?$", value):
        add_coef_to_associate_degree(value, sine, 1, coefs)
    elif re.search(r"^ ?\d+(\.\d+)?( ?\* ?)?X( ?\^ ?\d+)? ?$", value)\
            or re.search(r"^ ?X( ?\^ ?\d+)? ?\* ?\d+(\.\d+)? ?$", value):
        coef = float(re.search(r"(^|[^\^ ?0123456789]) ?\d+(\.\d+)?", value).group().replace('*', ''))
        if not coef:
            return
        add_coef_to_associate_degree(value, sine, coef, coefs)
    else:
        print('Error : incorrect syntax : ' + '\'' + value.strip() + '\'.')
        exit()


def start(parts_equation, coefs):
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
                searching_numbers(part, sine * side, coefs)
                break
            c = maths.get_lowest(a, b)
            value = part[:c]
            searching_numbers(value, sine * side, coefs)
            if part[c] == '-':
                sine = -1
            else:
                sine = 1
            part = part[c + 1:]
