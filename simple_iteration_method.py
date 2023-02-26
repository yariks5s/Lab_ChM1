import math
import numpy as np

def phi(x):
    return -1*np.cbrt(math.sin(x)-12*x+1)

def phi_dx(x):
    return -1*(math.cos(x)-12)/(3*(math.sin(x)-12*x+1)**2/3)

def apr_value(x_0, q, eps):
    return math.floor(np.log((abs(phi(x_0)-x_0)/(eps*(1-q)))/np.log(1/q)))+1

def post_value(value1, value2, q):
    if abs(value2-value1) < epsilon*(1-q)/q:
        return True
    return False

start_x = -3.75
amounts = 10
epsilon = 10**(-4)
q = 0.349

def iteration(start, amount=10):
    temp = start
    temp1 = 0
    print(f"Start: {start}")
    # amount = apr_value(-3.75, q, epsilon)
    for i in range(amount):
        temp1 = phi(temp)
        print(f"{i+1} Iteration: {temp1}")
        if post_value(temp1, temp, q):
            return temp1
        temp = temp1
    return temp
