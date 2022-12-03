import math


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
        elif type(num) == tuple:
            self.numerator, self.denominator = num
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
            rt = Fraction((self.numerator * other.denominator + self.denominator * other.numerator,
                           self.denominator * other.denominator))
            rt.simplify()
            return rt
        else:
            return self + Fraction(other)

    def __sub__(self, other):
        if type(other) == Fraction:
            other: Fraction
            rt = Fraction((self.numerator * other.denominator - self.denominator * other.numerator,
                           self.denominator * other.denominator))
            rt.simplify()
            return rt
        else:
            return self - Fraction(other)

    def __mul__(self, other):
        if type(other) == Fraction:
            other: Fraction
            rt = Fraction((self.numerator * other.numerator, self.denominator * other.denominator))
            rt.simplify()
            return rt
        else:
            return self * Fraction(other)

    def __truediv__(self, other):
        if type(other) == Fraction:
            other: Fraction
            rt = Fraction((self.numerator * other.denominator, self.denominator * other.numerator))
            rt.simplify()
            return rt
        else:

            return self / Fraction(other)

    def __floordiv__(self, other):

        return Fraction(int(float(self / other)))

    def __mod__(self, other):
        return Fraction(self - self // other * other)

    def __divmod__(self, other):
        return self // other, self % other

    def __pow__(self, power, modulo=None):
        rt = Fraction((self.numerator ** power, self.denominator ** power))
        return rt % modulo if modulo else rt

    def __bool__(self):
        return self.numerator != 0

    def __neg__(self):
        return Fraction((-self.numerator, self.denominator))

    def __pos__(self):
        return self

    def __abs__(self):
        return -self if self < 0 else self

    # compare
    def __lt__(self, other):
        if type(other) == Fraction:
            other: Fraction
            self.simplify()
            other.simplify()
            return self.numerator * other.denominator < self.denominator * other.numerator
        else:
            self.simplify()
            return self.numerator < self.denominator * other

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        if type(other) == Fraction:
            other: Fraction
            self.simplify()
            other.simplify()
            return self.numerator * other.denominator > self.denominator * other.numerator
        else:
            self.simplify()
            return self.numerator > self.denominator * other

    def __ge__(self, other):
        return self > other or self == other

    def __eq__(self, other):
        return (self - other).numerator == 0

    def __ne__(self, other):
        return not self == other

    # transform
    def __float__(self):
        return self.numerator / self.denominator

    def __int__(self):
        return self.numerator // self.denominator

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        if self.numerator:
            return f'{self.numerator}/{self.denominator}'
        else:
            return '0'
