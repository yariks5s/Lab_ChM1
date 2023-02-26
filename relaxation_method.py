import math

def phi(x):
    return x-(2/59.1)*(x**3+math.sin(x)-12*x+1)

def post_value(value1, value2, q):
    if abs(value2-value1) < epsilon*(1-q)/q:
        return True
    return False


q = 0.1945
epsilon = 10**(-4)

def iteration(start, amount=10):
    temp = start
    temp1 = 0
    print(f"Start: {start}")
    for i in range(amount):
        temp1 = phi(temp)
        print(f"Iteration {i + 1}:" + str(temp1))
        if post_value(temp1, temp, q):
            return temp1
        temp = temp1
    return temp
