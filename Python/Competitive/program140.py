import numpy as np

feature_map = np.array([
[3, 3, 3],
[0, 0, 0],
[-3, -3, -3]
])

relu_output = np.maximum(0,feature_map)
print(relu_output)

