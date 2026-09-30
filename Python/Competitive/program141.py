import numpy as np

matrix = np.array([
[6, 4],
[8, 6]
])

flatten_output = matrix.flatten()
print("flatten_output:",flatten_output)

weights = np.array([0.2,0.3,0.1,0.3])
bias = 0.3

weighted_sum = np.sum(flatten_output * weights) + bias

print("final output:",weighted_sum)