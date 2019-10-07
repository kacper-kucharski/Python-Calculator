import arith_tools

from typing import List
from functools import reduce
from operator import add

'''
Calculates the sum of a and b
Only supports positive integers.
'''
def sum(a, b):
    r = 0                                     # Result
    c = 0                                     # Carry

    length_a = arith_tools.get_number_length(a)     # Get length of number a
    length_b = arith_tools.get_number_length(b)     # Get length of number b
    max_length = max(length_a, length_b)            # Calculate maximum a if a > b, else b
    
    # Implement algorithm
    answer_list = []
    # Add digits start with the most right
    a_list = [int(i) for i in str(a)]
    b_list = [int(i) for i in str(b)]
    
    if a > b:
        op1 = a_list
        op2 = b_list
    else:
        op1 = b_list
        op2 = a_list

    op1.reverse()
    op2.reverse()

    for x in range(max_length+1):
        if c > 0:
            try:
                r = op1[x] + op2[x] + c
            except:
                r = c
        else:
            try:
                r = op1[x] + op2[x]
            except:
                try:
                    r = op1[x]
                except:
                    break

        c = 0

        if r > 10:
            r -= 10
            c += 1
        answer_list.append(r)
    
    answer_list.reverse()
    r = ''

    for x in answer_list:
        r = r + str(x)

    return r

'''
Calculates the subtraction of a and b.
Only supports positive integers.
'''
def sub(a, b):
    r = 0                                           # Result
    c = 0                                           # Borrow

    s = 1                                           # Sign is positive
    if b > a:
        pass # Implement algorithm, replace pass by your own code

    length_a = arith_tools.get_number_length(a)     # Get length of number a
    length_b = arith_tools.get_number_length(b)     # Get length of number b
    max_length = max(length_a, length_b)            # Calculate maximum a if a > b, else b
    
    # Implement algorithm

    return r * s                                    # Note the sign

'''
Calculates the multiplication of a and b.
Only supports positive integers.
'''
def multiply(a, b):
    r = 0                                     # Result
    # Implement algorithm
    return r

'''
Calculates the division of a and b.
Only supports positive integers.
'''
def divide(a, b):                       
    i = 0                                     # Result
    # Implement algorithm
    return i

'''
MANDATORY WEEK 5
'''

'''
Calculates the power of a and b.
Only supports positive integers.
'''
def power(a, b):
    r = 1                                     # Result
    # Implement algorithm
    return r

'''
Calculates the square root of a and b.
Only supports positive integers.
'''
def sqrt(a):
    if a <= 1:                                      # Early escape
        return a

    i = 1                                           # Increments
    r = 1                                           # Result of multiplication with i
    
    # Implement algorithm

    return sub(i, 1)                                # Subtract one from increment

'''
Calculates the modulo of a and b.
Only supports positive integers.
'''
def mod(a, b):
    return sub(a, multiply(divide(a, b), b))        # Calculate a - ((a / b) * b)

'''
Calculates the gcd of a and b.
Only supports positive integers.
'''
def gcd(a, b):
    return

'''
Calculates the lcm of a two integers.
Only supports positive integers.
'''
def lcm(a, b):
    return

'''
Converts a binary string to a decimal integer.
'''
def bin(a : str):
    return