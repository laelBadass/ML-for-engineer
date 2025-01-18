# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 09:48:14 2025

@author: ella
"""

import numpy as np

#this function is implementing how the gradient descent algorithm work using cost function.
def gradient_descent(x,y):
    #m_curr and b_curr are the current value of m(the slope) and b(the intercept) 
    m_curr = b_curr = 0
    iterations = 1000
    n = len(x)
    #the learning rate is an important value that show the step size as the learning is progressing. It should be chosen careful in order to get the right result.
    learning_rate = 0.08
    
    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        #the cost function is the mean squared error which evaluate if the learning is going well. A too big cost function value is undesired while a value close to 0 is desired.
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        md = -(2/n) * sum(x*(y-y_predicted))
        bd = -(2/n) * sum(y-y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print("m {}, b {}, cost {} iteration {}".format(m_curr,b_curr,cost,i))
        
        
x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x, y)

#A good way to choose the right learning rate and number of iterations is to:
    #1- put the iteration number low(for example 10) and the learning_rate very low (around 0.0001 more or less based on the situation)
    #2- compile and see if the cost(mse) is decrasing as the iterations goes.
    #3- keep increasing the learning rate if the mse value keep decreasing with the iteration.
    #4- if the mse start increasing that's mean the learning rate is to big so it should be decreased
    #5- when you reached the right learning rate, increase the number of iteration to get the right slope and intercept value