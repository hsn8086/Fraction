import cProfile
import math
import random
from typing import Union


class Fraction:
    def __init__(self, num: Union[int, float], precision=10):
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

    def __str__(self):
        if self.numerator:
            return f'{self.numerator}/{self.denominator}'
        else:
            return '0'



