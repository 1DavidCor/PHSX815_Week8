# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 20:05:48 2021

@author: d338c921
"""

#Write code for a simple model with at least one parameter (like coin probability, normal distr. mean, etc.) and an observable related to that parameter
#Create a figure of the "Neyman Construction" (see March 23 lecture), i.e. make a 2D plot with "true" parameter value on the x-axis and "measured" value on the y-axis, sampling many random experiments for each true value 

# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# main function for our coin toss Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: \n -sample_size [Std. Normal disribution sample size] \n -Nexp [# of experiments] \n -n [binomial distribution sample size] \n -prob [probability of the binimial distribution] \n -output_file [filename]")
        print
        sys.exit(1)

  
    # default number of sample points
    sample_size = 100
    
    #default number of experiments
    Nexp = 10
    
    #default binomial distribution sample size
    n = 10
    
    #default binomial distribution probability
    prob = 0.5

    # read the user-provided values from the command line (if there)
    if '-sample_size' in sys.argv:
        p = sys.argv.index('-sample_size')
        sample_size = int(sys.argv[p+1])
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Nexp = int((sys.argv[p+1]))
    if '-n' in sys.argv:
        p = sys.argv.index('-n')
        n = int((sys.argv[p+1]))
    if '-prob' in sys.argv:
        p = sys.argv.index('-prob')
        prob = float((sys.argv[p+1]))

#Need to sample from a distribution with at least one configurable parameter (to be determined via user input) such that the output is an integer
#Generate random numbers from a binomial distribution with parameters n and p; this constructs an array of size =  sample size
    #DOF = stats.binom.rvs(n, prob, size = Nexp)
    DOF = np.around(stats.uniform.rvs(loc = 0, scale = n, size = Nexp), decimals = 0).astype(int)
    
    #create empty array to store the N chi-squared distributions
    chi_data = np.ndarray((len(DOF), sample_size))
    
    for i in range(len(DOF)):
        #create the standard normal distributions according to the specified sample size/degrees of freedom
        data_gaussian = np.random.normal(0, 1, size= (sample_size, DOF[i]))
        #create the chi_square distribution from the gaussian distributions; sum of the squares over the # of DOF
        data_chi = np.sum(data_gaussian**2, axis = 1)
        chi_data[i, :] = data_chi

    # #calculate then print: mean, variance, ...
    mean_arr = []    
    for i in range(len(DOF)):
        mean_arr = np.append(mean_arr, np.mean(chi_data[i]))

plt.figure()
plt.title("Neyman Construction")
plt.ylabel("Calculated Mean")
plt.xlabel("True Mean")
plt.hist2d(DOF, mean_arr, bins = 100, cmap = plt.cm.rainbow)
plt.colorbar()
plt.show()
    
