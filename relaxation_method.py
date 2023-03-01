import math
import numpy as np

def f(x):
    return x**3 + math.sin(x) - 12*x + 1

def f_df(x):
    return 3*(x**2) + math.cos(x) - 12

def phi(x):
    return x - tao*f(x)

def post_value(value1, value2, q):
    if abs(value2-value1) < epsilon*(1-q)/q:
        return True
    return False

a = -4
b = -3.5
z0 = abs((b-a)/2)
start_x = (a + b)/2
M1 = max(abs(f_df(a)), abs(f_df(b)))
m1 = min(abs(f_df(a)), abs(f_df(b)))
tao = 2/(M1+m1)
q = (M1-m1)/(M1+m1)
epsilon = 10**(-4)

apr_value = np.floor(np.log(z0/epsilon)/np.log(1/q)) + 1

def iteration(start, amount=10):
    temp = start
    temp1 = 0
    print(f"Range of {a} and {b}, so start from {start_x}, z0 = {z0}\nWe found M1 = {M1} and m1 = {m1}.\n"
          f"After that tao = {tao}, q = {q}. Aprior value is {apr_value}\n\n"
          f"Start: {start}")
    for i in range(amount):
        temp1 = phi(temp)
        print(f"Iteration {i + 1}:" + str(temp1))
        if post_value(temp1, temp, q):
            return temp1
        temp = temp1
    return temp

# if(q<1):
#     iteration(start_x, 10)