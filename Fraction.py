from Fraction import Fraction

class Calculator:
    def __init__(self, fraction_a: Fraction, fraction_b: Fraction):
        self.fraction_a = fraction_a
        self.fraction_b = fraction_b
        self.result = str(self.num)+"/"+str(self.den)



    def multiplication(self) -> Fraction:
        numerator = self.fraction_a.numerator * self.fraction_b.numerator
        denominator = self.fraction_a.denominator * self.fraction_b.denominator
        self.result.initialize_with_num_den(str(self.num)+"/"+str(self.den))
        return self.result

    def division(self) -> Fraction:
        numerator = self.fraction_a.numerator * self.fraction_b.denominator
        denominator = self.fraction_a.denominator * self.fraction_b.numerator
        self.result.initialize_with_num_den(str(self.num)+"/"+str(self.den))
        return self.result

    def addition(self) -> Fraction:
        if self.fraction_a.denominator == self.fraction_b.denominator:
            numerator = self.fraction_a.numerator + self.fraction_b.numerator
            self.result.initialize_with_num_den(numerator, self.fraction_a.denominator)
            return self.result
        numerator = (self.fraction_a.numerator * self.fraction_b.denominator) + (self.fraction_a.denominator * self.fraction_b.numerator)
        den = self.fraction_a.denominator * self.fraction_b.denominator
        self.result.initialize_with_num_den(str(self.num)+"/"+str(self.den))
        return self.result

    def subtraction(self) -> Fraction:
        if self.fraction_a.denominator == self.fraction_b.denominator:
            numerator = self.fraction_a.numerator - self.fraction_b.numerator
            self.result.initialize_with_num_den(numerator, self.fraction_a.denominator)
            return self.result
        numerator = (self.fraction_a.numerator * self.fraction_b.denominator) - (self.fraction_a.denominator * self.fraction_b.numerator)
        denominator = self.fraction_a.denominator * self.fraction_b.denominator
        self.result.initialize_with_num_den(str(self.num)+"/"+str(self.den))
        return self.result



