import math

def f(x):
    return x**3 + math.sin(x) - 12 * x + 1

def f_dx(x):
    return 3 * (x ** 2) + math.cos(x) - 12

def f_dx2(x):
    return 6*x - math.sin(x)


a = -4
b = -3.5
z = abs((b-a)/2)
start_x = (a + b)/2
M1 = max(abs(f_dx2(a)), abs(f_dx2(b)))
m1 = min(abs(f_dx(a)), abs(f_dx(b)))
epsilon = 10**(-4)
q = (M1*z)/(2*m1)

# -3.5198033425380126
def iteration(start, amount=10):
    temp = start
    temp1 = 0
    print(f"Range of {a} and {b}, so start from {start_x}, z0 = {z}\nWe found M1 = {M1} and m1 = {m1}.\n\n"
          f"Start: {start}")
    for i in range(amount):
        temp1 = temp - (f(temp)/f_dx(start))
        print(f"{i + 1} Iteration: {temp1}")
        temp = temp1
    return temp
# if(f(a)*f(b)<0 and f(start_x)*f_dx2(start_x)>0 and q<1):
#     iteration(start_x, 10)