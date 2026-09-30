import numpy as np

image = np.array([
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[1, 1, 1, 1, 1],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0]
])

kernel = np.array([
[-1, -1, -1],
[ 0, 0, 0],
[ 1, 1, 1]
])

feature_map = np.zeros((3,3))

for i in range(3):
    for j in range(3):
        portion = image[i:i+3,j:j+3]
        result = np.sum(kernel * portion)

        print(result)

        feature_map[i][j] = result

print("feature map:")
print(feature_map)