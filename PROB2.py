from scipy.optimize import fsolve
import numpy as np

"""function found via this 
https://pythonnumericalmethods.berkeley.edu/notebooks/chapter19.05-Root-Finding-in-Python.html
https://glowingpython.blogspot.com/2011/05/hot-to-find-intersection-of-two.html"""

#function 1
def f1(x):
    return x - 3 * np.cos(x)

#function 2
def f2(x):
    return np.cos(2 * x) - x[0] ** 3

#finds possible points of interactions.
def intersection(x):
    return f1(x) - f2(x)

"""Initial guesses closer to the expected roots. i used an online calculator
and they said there was 3 possible values. so i tried to make a range that could atleast get three values"""
initial_guess_intersection = [-3, 0, 3]
#solves the roots for equation 1
roots1 = fsolve(f1, initial_guess_intersection)
print("Roots of the first equation:", roots1)
#solves the roots for equation 2
roots2 = fsolve(f2, initial_guess_intersection)
print("Roots of the second equation:", roots2)

"""tries to find the intersaction, unsure if this actually works.the website i found says the intersection
point is right, however unsure if the fsolve does the right thing. most examples 
use something called pylab, and chatgpt doesn't feel right"""
intersection_points = fsolve(intersection, initial_guess_intersection)
print("Intersection points:", intersection_points)
#sorry for errors, its caused by the intersection_guess_points for the equations.