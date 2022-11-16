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
            # 取标准化进度值
            precision_normal = pow(10, precision)
            precision_int = int(precision_normal)

            # 取未化简分子
            num_int = int(num * precision_int)

            # 取最大公约数
            hcf = math.gcd(num_int, precision_int)

            # 写入
            self.denominator = int(precision_int / hcf)
            self.numerator = int(num_int / hcf)
            # 注:分母为1*precision_int

