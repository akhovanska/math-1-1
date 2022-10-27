import numpy as np

# a = np.array([[1, 1, 0], [0, 1, 1], [0, 1, 1]])

a = np.loadtxt("20_12.txt")


def triangle():
    b = True
    for i in range(a.shape[1]):
        if np.sum(a[:, i][i + 1:]) != 0:
            b = False
    if b:
        print("матриця верхньотрикутна")
    else:
        print("матриця не є верхньотрикутною")


triangle()
