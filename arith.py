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
    # Create a list from the given digits
    a_list = [int(i) for i in str(a)]
    b_list = [int(i) for i in str(b)]
    
    # check which operand is bigger and use is as the first one
    if a > b:
        op1 = a_list
        op2 = b_list
    else:
        op1 = b_list
        op2 = a_list

    # reverse the lists to start from right to left
    op1.reverse()
    op2.reverse()

    # Loop to the length of the largest given number + 1 (for the potential carry that has to be added in front)
    for x in range(max_length+1):
        if c > 0:
            # Try to add all the number else try to add to the main number else just add the remaining Carry
            try:
                r = op1[x] + op2[x] + c
            except:
                try:
                    r = op1[x] + c
                except:
                    r = c    
            # If there is no carry just add the two operands togheter else just add the main remaining operand else break out of the loop
        else:
            try:
                r = op1[x] + op2[x]
            except:
                try:
                    r = op1[x]
                except:
                    break
        
        # after using the carry, set it back to 0 for next upcoming use
        c = 0

        # if r is larger than 10 add 1 to carry and remove 10 from r
        if r >= 10:
            r -= 10
            c += 1
        # then add the r to the answer_list
        answer_list.append(r)
    # Reverse the answer_list(rember we reversed it in the beginning so now we reverse it back to have the true number position)
    answer_list.reverse()
    # Change the r variable into a empty string
    r = ''

    # loop through the final answe_list and create a string from it
    for x in answer_list:
        r = r + str(x)
    # return the created string as an integer
    return int(r)

'''
Calculates the subtraction of a and b.
Only supports positive integers.
'''
def sub(a, b):
    r = 0                                           # Result
    c = 0                                           # Borrow

    s = 1                                           # Sign is positive

    answer_list = []
    # Create a list of the given digits
    a_list = [int(i) for i in str(a)]
    b_list = [int(i) for i in str(b)]

    if b > a:
        s = -1
        op1 = b_list
        op2 = a_list
    else:
        op1 = a_list
        op2 = b_list

    op1.reverse()
    op2.reverse()

    length_a = arith_tools.get_number_length(a)     # Get length of number a
    length_b = arith_tools.get_number_length(b)     # Get length of number b
    max_length = max(length_a, length_b)            # Calculate maximum a if a > b, else b
    
    # Implement algorithm
    for x in range(max_length):
        try:
            r = op1[x] - op2[x] - c
        except:
            r = op1[x] - c

        c = 0

        if r < 0:
            r += 10
            c += 1
        answer_list.append(r)
    
    answer_list.reverse()
    r = ''

    for x in answer_list:
        r = r + str(x)

    return int(r) * s                                    # Note the sign

'''
Calculates the multiplication of a and b.
Only supports positive integers.
'''
def multiply(a, b):
    r = 0                                     # Result
    # Implement algorithm
    if a == 1:
        r = b
    elif b == 1:
        r = a
    else:
        r = sum(a, a)
        
        for _ in range(b-2):
            r = sum(r, a)

    return r

'''
Calculates the division of a and b.
Only supports positive integers.
'''
def divide(a, b):                       
    i = 0                                     # Result
    # Implement algorithm
    while a >= b:
        a = sub(a, b)
        i += 1

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
    for _ in range(b):
        r = multiply(r, a)
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
    while (r != a) and (r < a) :
        r = multiply(i, i)
        i += 1

    if r > a:
        i -= 1

    return sub(i, 1)                             # Subtract one from increment

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
    answer = []
    remainder = mod(a, b)
    answer.append(remainder)
    real_answer = answer[0]
    while remainder != 0:
        a = b
        b = remainder
        remainder = mod(a, b)
        answer.append(remainder)
        
    for x in range(len(answer)):
        if (answer[x] != 0):
            real_answer = answer[x]    
    return real_answer


'''
Calculates the lcm of a two integers.
Only supports positive integers.
'''
def lcm(a, b):
    try:
        r = a * b / gcd(a, b)
    except:
        r = a

    return int(r)

'''
Converts a binary string to a decimal integer.
'''
def bin(a : str):
    return