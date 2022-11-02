import string
import random
from collections import Counter
import time
from decimal import *

getcontext().prec = 1000

# Arithmetic Encoding
def ac_encode(txt):
    res = Counter(txt)

    # characters
    chars = list(res.keys())

    # frequency of characters
    freq = list(res.values())

    probability = []
    for i in freq:
        probability.append(Decimal(i / len(txt)))

    # print(chars)
    # print(probability)

    high = Decimal(1.0)
    low = Decimal(0.0)
    for c in txt:
        diff = Decimal(high) - Decimal(low)
        index = chars.index(c)
        for i in range(index):
            high = Decimal(low) + Decimal(diff) * Decimal(probability[i])
            low = Decimal(high)

        high = Decimal(low) + Decimal(diff) * Decimal(probability[index])
        # print(f'char {c} -> Low: {low}   High: {high}')

    tag = Decimal((low + high) / 2)

    # print('Input: ' + txt)
    # print(str(low) + '< codeword <' + str(high))
    # print('codeword = ' + str(tag))

    return chars, probability, tag


# Arithmetic Decoding
def ac_decode(chars, probability, tag):
    high = Decimal(1.0)
    low = Decimal(0.0)
    output = ''
    c = ''
    while c != '$':
        diff = Decimal(high) - Decimal(low)
        for i in range(len(chars)):
            high = Decimal(low) + Decimal(diff) * Decimal(probability[i])
            if low < tag < high:
                break
            else:
                low = Decimal(high)

        c = chars[i]
        output += c

    return output


def arithmetic_coding(input):
    if '$' in input:
        input = input[0:input.index('$')]
    if input[-1] != '$':
        input += '$'

    print('Input:  ' + input)

    (chars, probability, tag) = ac_encode(input)
    output = ac_decode(chars, probability, tag)

    print('Decode: ' + output)

    print('does match :  ' + str(input == output))

    return input == output


txt = """The decimal module provides support for fast correctly rounded decimal floating point arithmetic. It offers several advantages over the float datatype:
Decimal “is based on a floating-point model which was designed with people in mind, and necessarily has a paramount guiding principle – computers must provide an arithmetic that works in the same way as the arithmetic that people learn at school.” – excerpt from the decimal arithmetic specification."""
arithmetic_coding(txt)
