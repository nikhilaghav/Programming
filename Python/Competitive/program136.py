input = 3
weight = 0.6
bias = 0.2
target = 1
learning_rate = 0.2

prediction = input * weight + bias

print("predicted value:",prediction)

error = target - prediction
print("error:",error)

gradient = (prediction - target) * input
print("gradient:",gradient)

new_weight = weight -(learning_rate * gradient)
print("new weight:",new_weight)