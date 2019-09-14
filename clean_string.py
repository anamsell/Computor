import re
import maths

def reduce_form(coefs):
    lst = sorted(coefs)
    string = ''
    for degree in lst:
        if degree == 'max':
            break
        string += maths.signe_number(coefs[degree]) + ' ' + str(maths.absol(coefs[degree])) + 'X^' + str(degree) + ' '
        if coefs[degree] != 0:
            coefs['max'] = degree
    string = re.sub(r"X\^0", '', string)
    string = re.sub(r"(- )?0(X(\^\d+)?)? ", '', string)
    string = re.sub(r"1X", 'X', string)
    string = re.sub(r"\^1", '', string)
    if string[0] == '+':
        return string[2:]
    return '-' + string[2:]

def transform_int(coefs):
    for degree in coefs:
        if type(coefs[degree]) is float and coefs[degree].is_integer():
            coefs[degree] = int(coefs[degree])

def entry(parts_equation):
    parts_equation[0] = parts_equation[0].strip()
    parts_equation[0] = re.sub(r' +', r" ", parts_equation[0])
    parts_equation[1] = parts_equation[1].strip()
    parts_equation[1] = re.sub(r' +', r" ", parts_equation[1])
