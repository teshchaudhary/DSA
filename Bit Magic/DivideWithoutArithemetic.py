import math


def func1(dividend, divisor):

    if ((dividend < 0) ^ (divisor < 0)):
        sign = -1
    else:
        sign = 1

    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    while (dividend >= divisor):
        dividend -= divisor
        quotient += 1

    if sign == -1:
        quotient = -quotient

    return quotient


def divid(dividend, divisor):

    if ((dividend < 0) ^ (divisor < 0)):
        sign = -1
    else:
        sign = 1

    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    temp = 0

    for i in range(31, -1, -1):
        if (temp + (divisor << i) <= dividend):
            temp += divisor << i
            quotient |= 1 << i

    if sign == -1:
        quotient = -quotient
    return quotient

# O(1)


def divide(dividend, divisor):
    if dividend == 0:
        return 0
    if divisor == 0:
        return math.inf

    sign = (divisor < 0) ^ (dividend < 0)

    dividend = abs(dividend)
    divisor = abs(divisor)

    if divisor == 1:
        if (sign == 0):
            return dividend
        else:
            return -dividend

    res = math.exp(math.log(abs(dividend)) - math.log(abs(divisor)))

    if (sign == 0):
        return res
    else:
        return -res
