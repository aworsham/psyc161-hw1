#!/usr/bin/env python

"""Module for estimation of factorial (Homework #1)

Note:  this is just a skeleton for you to work with.  But it already
       has some "bugs" you need to catch and fix.
"""

from nose.tools import assert_equal

def factorial_recursive(n):
    # For all positive numbers, function recursively multiplies n by n-1
    if n <= 1:
        return 1
    else:
        result = n * factorial_recursive(n - 1)
        return result

def test_factorial():
    assert_equal(factorial_recursive(1), 1, "Incorrect")
    assert_equal(factorial_recursive(3), 6, "Incorrect")
    assert_equal(factorial_recursive(3), 9, "You passed the test!")

if __name__ == '__main__':
    # This is a way to determine either file was "executed", so if it was
    # imported (by e.g. nose) as a library, we should not run code
    # below

    nconditions = int(raw_input("Please enter number of conditions: "))
    norders = factorial_recursive(nconditions)
    print("Number of possible trial orders: " + str(norders))
