import sys
import parsing
import clean_string
import resolve

if len(sys.argv) == 1:
    print('Error, no parameter.')
    exit()
string = ""
for a in sys.argv[1:]:
    string += a
    string += ' '
if string.find('=') == -1:
    print('Error, no \"=\' in the equation.')
    exit()
parts_equation = string.split('=')
if len(parts_equation) != 2:
    print('Too much \'=\' in the equation, can only have 1.')
    exit()
coefficients = {0: 0, 1: 0, 2: 0, 'max': 0}
clean_string.entry(parts_equation)
parsing.start(parts_equation, coefficients)
clean_string.change_coefficients_to_int(coefficients)
print("Reduced form: " + clean_string.reduce_form(coefficients) + "= 0")
print("Polynomial degree: " + str(coefficients['max']))
if coefficients['max'] > 2:
    print("The polynomial degree is strictly greater than 2, I can\'t solve.")
    exit()
resolve.start(coefficients)
