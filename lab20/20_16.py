import numpy as np

a = np.loadtxt("20_12.txt")

print(np.min(np.max(a, axis=0)))
