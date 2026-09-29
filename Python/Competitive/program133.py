import numpy as np
import math

inputs= np.array([2,3])
weights=np.array([0.4,0.6])

bias = 0.5

z = np.dot(inputs,weights) + bias

def Sigmoid(x):
    return 1 / (1 + math.exp(-x))

y = Sigmoid(z)

print("weighted sum:",z)
print("output:",y)

if y >0.5:
    print("output is close to 1")

else:
    print("output is close to 0")