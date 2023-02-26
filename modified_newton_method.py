import math

def f(x):
    return x**3 + math.sin(x) - 12 * x + 1

def f_dx(x):
    return 3 * (x ** 2) + math.cos(x) - 12

def post_value(value1, value2, q):
    if abs(value2-value1) < epsilon*(1-q)/q:
        return True
    return False


start_x = -3.75
amounts = 10
epsilon = 10**(-4)
q = 0.13

# -3.5198033425380126
def iteration(start, amount=10):
    temp = start
    temp1 = 0
    print(f"Start: {start}")
    for i in range(amount):
        temp1 = temp - (f(temp)/f_dx(start))
        print(f"{i + 1} Iteration: {temp1}")
        if post_value(temp1, temp, q):
            return temp1
        temp = temp1
    return temp
