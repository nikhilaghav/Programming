import numpy as np
import matplotlib.pyplot as plt

input = np.array([-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,
                  1,2,3,4,5,6,7,8,9,10])

def Sigmoid(x):
    return 1 / (1 + np.exp(-x))

y = Sigmoid(input)

def Relu(y):
    return np.maximum(0,y)

z = Relu(input)

def tanh(a):
    return np.tanh(a)

b=tanh(input)

plt.plot(input,y)
plt.xlabel("input")
plt.ylabel("output")
plt.title("Sigmoid curve")
plt.grid()
plt.show()

plt.plot(input,z)
plt.xlabel("input")
plt.ylabel("output")
plt.title("Relu curve")
plt.grid()
plt.show()

plt.plot(input,b)
plt.xlabel("input")
plt.ylabel("output")
plt.title("tanh curve")
plt.grid()
plt.show()




