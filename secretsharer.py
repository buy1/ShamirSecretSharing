from fractions import Fraction
import random

def mkRandInt():
    return Fraction(random.randint(1,101),random.randint(1,101))
def split(val, n,k):
    # val is the secret (the value when x = 0).
    # n is the number of points to distribute.
    # k is the number of points needed to reconstruct the polynomial.
    # Return a list of n random points such that x != 0 for every point.
    coefficients = [val] + [mkRandInt() for i in range(k - 1)]
    points = []
    for number in range(n):
        cur_polynomial = 0
        x = mkRandInt()
        for power, coefficient in enumerate(coefficients):
            cur_polynomial += coefficient*(x**power)
        points.append((x,cur_polynomial))
    return points

def interpolate(points, x):
    # points is a list of shares.
    # x is the x-coordinate in which to compute the secret at.
    # Return the computed secret value. 
    total_val = 0
    for cur_x,cur_y in points:
        returnval = 1
        for other_x,other_y in points:
            if other_x != cur_x:
                returnval *= Fraction(x - other_x,cur_x - other_x)
        total_val += cur_y * returnval
    return total_val



