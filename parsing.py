import re
import maths

def add_coef_to_associate_degree(value, signe, coef, coefs):
    try:
        degree = int(re.search("\^ ?\d+(\.\d+)? ?", value).group()[1:])
    except AttributeError:
        degree = 1
    try:
        coefs[degree]
    except KeyError:
        coefs[degree] = coef * signe
    else:
        coefs[degree] += coef * signe

def searching_numbers(value, signe, coefs):
    if re.search(r"^ ?\d+(\.\d+)? ?$", value):
        #print(float(value))
        #print("signe:", signe)
        coefs[0] += float(value) * signe
    elif re.search(r"^ ?X( ?\^ ?\d+)? ?$", value):
        add_coef_to_associate_degree(value, signe, 1, coefs)
    elif re.search(r"^ ?\d+(\.\d+)?( ?\* ?)?X( ?\^ ?\d+)? ?$", value) or re.search(r"^ ?X( ?\^ ?\d+)? ?\* ?\d+(\.\d+)? ?$", value):
        coef = float(re.search("(^|[^\^ ?0123456789]) ?\d+(\.\d+)?", value).group().replace('*', ''))
        if not coef:
            return
        add_coef_to_associate_degree(value, signe, coef, coefs)
    else:
        print('Error : incorrect syntax : ' + '\'' + value.strip()+ '\'.')
        exit()

def main(parts_equation, coefs):
    for idx, part in enumerate(parts_equation):
        signe = 1
        if not part:
            print("Error, each part of the equation must contain 1 number or more.")
            exit()
        if part[0] == '-' or part[0] == '+':
            if part[0] == '-':
                signe = -1
            part = part[1:]
        if idx == 1:
            side = -1
        else:
            side =  1
        while (1):
            a = part.find('+')
            b = part.find('-')
            if a == -1 and b == -1:
                searching_numbers(part, signe * side, coefs)
                break
            c = maths.get_lowest(a, b)
            value = part[:c]
            searching_numbers(value, signe * side, coefs)
            if part[c] == '-':
                signe = -1
            else:
                signe = 1
            part = part[c + 1:]