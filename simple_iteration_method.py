import math
import numpy as np

def phi(x):
    return -1*np.cbrt(math.sin(x)-12*x+1)

def phi_dx(x):
    return (-1*math.cos(x)+12)/(3*np.cbrt(-1*math.sin(x)+12*x-1)**2)

def post_value(value1, value2, q):
    if abs(value2-value1) < epsilon*(1-q)/q:
        return True
    return False

a = -4
b = -3.5
z = abs((b-a)/2)
start_x = (a + b)/2
amounts = 10
epsilon = 10**(-4)
q = max(abs(phi_dx(a)), abs(phi_dx(b)))
apr_value = int(np.floor(np.log((phi(start_x)-start_x)/((1-q)*epsilon))/np.log(1/q)) + 1)

def iteration(start, amount=10):
    temp = start
    temp1 = 0
    print(f"Range of {a} and {b}, so start from {start_x}, z0 = {z}. Aprior value = {apr_value}\n\n"
          f"Start: {start}")
    # amount = apr_value(-3.75, q, epsilon)
    for i in range(amount):
        temp1 = phi(temp)
        print(f"{i+1} Iteration: {temp1}")
        if post_value(temp1, temp, q):
            return temp1
        temp = temp1
    return temp

# if(q<1 and abs(phi(start_x)-start_x)<=(1-q)*z):
#     iteration(start_x)