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
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testValidInputA(self):
        self.assertEqual(classifyTriangle(201, 5, 204), "InvalidInput")

    def testValidInputB(self):
        self.assertEqual(classifyTriangle(-1, 3, 1), "InvalidInput")

    def testValidInputC(self):
        self.assertEqual(classifyTriangle('a', 2, 3), "InvalidInput")

    def testValidInputD(self):
        self.assertEqual(classifyTriangle(0.5, 1, 1), "InvalidInput")

    def testValidInputE(self):
        self.assertEqual(classifyTriangle(2, 1, 0), "InvalidInput")

    def testNotTriangle(self):
        self.assertEqual(classifyTriangle(1, 4, 2), "NotATriangle")

    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(3, 3, 4), "Isosceles")

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(5, 6, 7), "Scalene")


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

