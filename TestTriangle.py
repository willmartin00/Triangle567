# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(6,8,10),'Right','6,8,10 is a Right triangle')

    def testRightTriangleD(self): 
        self.assertEqual(classifyTriangle(8,10,6),'Right','8,10,6 is a Right triangle')
        
    def testEquilateralTrianglesA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTrianglesB(self): 
        self.assertEqual(classifyTriangle(5,5,5),'Equilateral','5,5,5 should be equilateral')

    def testIsoscelesTrianglesA(self):
        self.assertEqual(classifyTriangle(4,4,2),'Isosceles','4,4,2 should be isosceles')

    def testIsoscelesTrianglesB(self):
        self.assertEqual(classifyTriangle(8,6,8),'Isosceles','8,6,8 should be isosceles')

    def testScaleneTrianglesA(self):
        self.assertEqual(classifyTriangle(6,7,8),'Scalene','6,7,8 should be scalene')

    def testScaleneTrianglesB(self):
        self.assertEqual(classifyTriangle(9,10,11),'Scalene','9,10,11 should be scalene')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

