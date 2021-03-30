# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:35:49 2021

@author: d338c921
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

#Write a program that can find the minimum of a function that you define. The function can be any one (even very simple) as long as it actually has a minimum. 
#You are welcome to use any standard or external C++ or Python libraries (you don't need to implement the minimization routine, only the function to be minimized).
#You can also try to visualize your function and the location of the minimum (not required).

#define the function to be minimized
f = lambda x: x*x - 5*x + 1

#find the coordinates of the minimum
minimum = optimize.minimize(f, 0)

#x coordinate
x_min = minimum.x[0]
#y coordinate
y_min = minimum.fun

#set an x array for plotting
x = np.linspace(x_min - 10, x_min + 10, 2000)

plt.figure()
plt.plot(x, f(x), label = "f(x)")
plt.scatter(x_min, y_min, marker = "o", color = "r", label = "minimum")
plt.title("Minimizing Functions: min @ (" + str(np.round(x_min, decimals = 2)) + ", " + str(np.round(y_min, decimals = 2)) + ")")
plt.ylabel("f(x)")
plt.xlabel("x")
plt.legend()
