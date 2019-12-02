import maths
from copy import copy
import clean_string


class Result:
    def __init__(self, n1, n2):
        self.n1 = copy(n1)
        self.n2 = copy(n2)
        self.calculate()

    def calculate(self):
        self.same_fraction()
        printable_fraction = ''
        if not self.n1.real:
            char1_real = 'i'
        else:
            char1_real = ''
        if not self.n2.real:
            char2_real = 'i'
        else:
            char2_real = ''
        if (self.n1.numerator_square == self.n2.numerator_square and self.n1.real == self.n2.real) \
                or self.n1.numerator == 0 or self.n2.numerator == 0:
            self.n1.numerator += self.n2.numerator
            self.n1.reduce_fraction()
            char1_real += char2_real
            if self.n1.numerator < 0:
                printable_fraction += '-'
            printable_fraction += clean_string.get_string(self.n1.numerator, self.n1.numerator_square, char1_real)
        else:
            common = maths.find_gcd_euclide(self.n1.numerator, self.n2.numerator)
            if common != 1:
                self.n1.numerator /= common
                self.n2.numerator /= common
                if self.n1.denominator < 0:
                    common *= -1
                    self.n1.denominator *= -1
                if common == -1:
                    printable_fraction += '-'
                else:
                    printable_fraction += str(clean_string.change_number_to_int(common))
            if self.n1.numerator < 0 < self.n2.numerator:
                tmp = self.n1
                self.n1 = self.n2
                self.n2 = tmp
                tmp = char1_real
                char1_real = char2_real
                char2_real = tmp
            if not (self.n1.denominator == 1 and self.n1.denominator_square) or not common == '':
                printable_fraction += '('
            printable_fraction += clean_string.get_string(self.n1.numerator, self.n1.numerator_square, char1_real)
            if self.n2.numerator < 0:
                printable_fraction += " - "
            else:
                printable_fraction += " + "
            printable_fraction += clean_string.get_string(self.n2.numerator, self.n2.numerator_square, char2_real)
            if not (self.n1.denominator == 1 and self.n1.denominator_square) or not common == '':
                printable_fraction += ')'
        if not (self.n1.denominator == 1 and self.n1.denominator_square == 1):
            printable_fraction += '/' + str(clean_string.change_number_to_int(self.n1.denominator))
        if not self.n1.denominator_square == 1:
            printable_fraction += u"\u221A" + str(clean_string.change_number_to_int(self.n1.denominator_square))
        self.display_result(printable_fraction)

    @staticmethod
    def display_result(result):
        print(result)

    def same_fraction(self):
        self.n1.numerator, self.n1.denominator, self.n2.numerator, self.n2.denominator = \
            maths.same_denominator(self.n1.numerator, self.n1.denominator, self.n2.numerator, self.n2.denominator)
        self.n1.numerator_square *= self.n2.denominator_square
        self.n2.numerator_square *= self.n1.denominator_square
        self.n1.denominator_square *= self.n2.denominator_square
        self.n2.denominator_square = self.n1.denominator_square
        self.n1.reduce_squares()
        self.n1.reduce_squares()


class Number:
    def __init__(self, numerator=1, denominator=1, numerator_square=1, denominator_square=1, real=1):
        self.numerator = numerator
        self.denominator = denominator
        self.numerator_square = numerator_square
        self.denominator_square = denominator_square
        self.reduce_squares()
        self.reduce_fraction()
        self.real = real
        if self.denominator < 0:
            self.denominator *= -1
            self.numerator *= -1
        pass

    def reduce_fraction(self):
        self.numerator, self.denominator = maths.irreducible_fraction(self.numerator, self.denominator)

    def reduce_squares(self):
        self.numerator_square, self.denominator_square = maths.irreducible_fraction(self.numerator_square,
                                                                                    self.denominator_square)
        self.numerator_square, f1 = maths.square(self.numerator_square)
        self.denominator_square, f2 = maths.square(self.denominator_square)
        self.numerator *= f1
        self.denominator *= f2

        if self.denominator_square != 1:
            self.denominator *= self.denominator_square
            self.numerator_square *= self.denominator_square
            self.denominator_square = 1
