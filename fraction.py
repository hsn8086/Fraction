import cProfile
import math
import random
from typing import Union


class Fraction:
    def __init__(self, num, precision=10):
        self.denominator = 1
        self.numerator = 1
        if type(num) == int:
            self.denominator = 1
            self.numerator = num
        elif type(num) == float:
            # 取标准化精度值
            precision_int = int(10 ** precision)

            # 写入
            self.denominator = precision_int

            # 取未化简分子
            self.numerator = int(num * precision_int)

            # 化简
            self.simplify()
            # 注:分母为1*precision_int
        elif type(num) == Fraction:
            self.denominator = num.denominator
            self.numerator = num.numerator
            self.simplify()
        else:
            self.__init__(float(num), precision)

    def simplify(self):
        hcf = math.gcd(self.denominator, self.numerator)
        if hcf:
            self.numerator = int(self.numerator / hcf)
            self.denominator = int(self.denominator / hcf)
        if self.denominator < 0:
            self.denominator = -self.denominator
            self.numerator = -self.numerator

    def __add__(self, other):
        if type(other) == Fraction:
            other: Fraction
            rt = Fraction(1)
            rt.numerator = self.numerator * other.denominator + self.denominator * other.numerator
            rt.denominator = self.denominator * other.denominator
            rt.simplify()
            return rt
        else:
            return self + Fraction(other)

    def __sub__(self, other):
        if type(other) == Fraction:
            other: Fraction
            rt = Fraction(1)
            rt.numerator = self.numerator * other.denominator - self.denominator * other.numerator
            rt.denominator = self.denominator * other.denominator
            rt.simplify()
            return rt
        else:
            return self - Fraction(other)

    def __mul__(self, other):
        if type(other) == Fraction:
            other: Fraction
            rt = Fraction(1)
            rt.numerator = self.numerator * other.numerator
            rt.denominator = self.denominator * other.denominator
            rt.simplify()
            return rt
        else:
            return self * Fraction(other)

    def __truediv__(self, other):
        if type(other) == Fraction:
            other: Fraction
            rt = Fraction(1)
            rt.numerator = self.numerator * other.denominator
            rt.denominator = self.denominator * other.numerator
            rt.simplify()
            return rt
        else:
            return self / Fraction(other)

    def __floordiv__(self, other):
        return Fraction(float(self) // float(other))

    def __mod__(self, other):
        return Fraction(self - self // other * other)

    def __divmod__(self, other):
        return self // other, self % other

    def __float__(self):
        return self.numerator / self.denominator

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        if self.numerator:
            return f'{self.numerator}/{self.denominator}'
        else:
            return '0'


print(Fraction(6) % 10)
