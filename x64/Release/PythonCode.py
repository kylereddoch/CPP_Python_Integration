import re
import string


def MultiplicationTable(num): 
    """ displays multiplication table of 1-10 for a given number """
    print("\nResult:")
    for i in range(10):
        multiplier = i+1    # adding one since all ranges begin with 0
        result = num*multiplier
        print("%d X %d = %d" % (num, i+1, result))
    return 0


def DoubleValue(n):
    """ returns double of the given value """
    print("\nResult")
    print("%d X 2 = " % (n))
    return n * 2