# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""


def classify_triangle(a_1,b_1,c_1):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """

    valid_nums = []

    for i in range(0,201):
        valid_nums.append(i)

    # require that the input values be >= 0 and <= 200
    if ((a_1 not in valid_nums or b_1 not in valid_nums or c_1 not in valid_nums) or
        (not(isinstance(a_1,int) and isinstance(b_1,int) and isinstance(c_1,int)))):
        return 'InvalidInput'

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly MORE than the third side
    # of the specified shape is not a triangle
    if (a_1 >= (b_1 + c_1)) or (b_1 >= (a_1 + c_1)) or (c_1 >= (a_1 + b_1)):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if a_1 == b_1 and b_1 == c_1:
        return 'Equilateral'
    if (((a_1*a_1)+(b_1 * b_1))==(c_1*c_1)or
    ((c_1*c_1)+(b_1*b_1))==(a_1*a_1)or((c_1*c_1)+(a_1*a_1))==(b_1*b_1)):
        return 'Right'
    if (a_1 != b_1) and (b_1 != c_1) and (a_1 != c_1):
        return 'Scalene'
    return 'Isosceles'
