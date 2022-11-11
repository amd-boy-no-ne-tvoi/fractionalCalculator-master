from fractions import Fraction

number_1 = input('Enter your first number: ')
number_2 = input('Enter your second number: ')
print('----------------------------------------')
print('+')
print(Fraction(number_1) + Fraction(number_2))
print('----------------------------------------')
print('-')
print(Fraction(number_1) - Fraction(number_2))
print('----------------------------------------')
print('*')
print(Fraction(number_1) * Fraction(number_2))
print('----------------------------------------')
print('/')
print(Fraction(number_1) / Fraction(number_2))
print('----------------------------------------')

