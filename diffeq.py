# import numpy
import matplotlib.pyplot as plt
# import tkinter

# t_0 = float(input("Initial time t_0 = "))
# x_0 = float(input("Initial state x(t_0) = "))
# T = float(input("Duration T = "))
# h = float(input("Step size h = "))

t_0 = 0
x_0 = 1
T = 1
h = 0.01

def f(t, x):
    return x + t

def incrementStep(t):
    if t + h > T + t_0:
        return T + t_0
    else:
        return t + h

def eulerMethod():
    x = {t_0 : x_0}
    x_n = x_0
    t_n = t_0
    N = int(T / h) + 1

    for i in range(N):
        t_n = incrementStep(t_n)
        x_n = x_n + (f(t_n, x_n) * h)
        x[t_n] = x_n

    return x

def rungeKutta():
    x = {t_0 : x_0}
    x_n = x_0
    t_n = t_0
    N = int(T / h) + 1

    for  i in range(N):
        t_n = incrementStep(t_n)
        k1 = f(t_n, x_n)
        k2 = f(t_n + (h / 2), x_n + ((h * k1) / 2))
        k3 = f(t_n + (h / 2), x_n + ((h * k2) / 2))
        k4 = f(t_n + h, x_n + (h * k3))
        x_n = x_n + (((k1 + (2 * k2) + (2 * k3) + k4) * h) / 6)
        x[t_n] = x_n

    return x

def plotData(EMdata, RKdata):
    EMxValues = list(EMdata.keys())
    EMyValues = list(EMdata.values())
    EMplot = plt.plot(EMxValues, EMyValues, 'b-')

    RKxValues = list(RKdata.keys())
    RKyValues = list(RKdata.values())
    RKplot = plt.plot(RKxValues, RKyValues, 'r-')

    plt.xlabel('t')
    plt.ylabel('x', rotation=0)

    plt.grid(True)

    plt.show()

plotData(eulerMethod(),rungeKutta())