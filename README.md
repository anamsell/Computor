The goal of this project is to make you create a program to solve simple equations.
The program will take a polynomial equation as a parameter. That is, only using
powers, no complicated functions. The program will have to display its solution(s).

Why polynomials ? Because it's one of the simplest and most powerful mathematical tool.
We use it in all areas and at all levels to simplify and express a lot of things.
For example, the sin, cos and tan functions are computed with the help of polynomials.

The idea is to make you feel more confident using basic mathematical tools, which could
be useful for a number of other projects at 42. It's not about "doing maths to do maths",
but to allow us to progressively use that for other projects where it's needed.

Write a program that solves polynomial equation of degree inferior or equal to 2.
You must at least display :
• The reduced form of the equation.
• The degree of the equation.
• Its solution(s), as well as the sign of the discriminant when it makes sense.

We'll always consider that the input in correctly formated, ie. all the terms are of the
form a * x^p. Warning, this doesn't mean that the equation is
solvable ! In your case, your program should detect it and tell it.



Installation:

git clone https://github.com/anamsell/Computor.git Computor

cd ./Computor

Example:

python3 computor.py "1.5 * X^1 + 8.3 * X^2 - 2 * X^0 = -4.1 * X^1 + 2 * X^0"
