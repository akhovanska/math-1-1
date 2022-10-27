import numpy as np

a = np.loadtxt("20_12.txt")

def norm_b(a):
    return np.max(np.sum(a, axis = 0))

print(norm_b(a))
