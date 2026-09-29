import numpy as np
import math

actual = [1,0,1,1,0]
predict =[0.7,0.4,0.6,0.9,0.6]

total_error = 0

for i in range(len(actual)):
    error = actual[i] - predict[i]
    total_error = total_error + error**2

mean_square_error = total_error / len(actual)

print("MSE is:",mean_square_error)

total_error = 0
for i in range(len(actual)):
    error = -(actual[i]*math.log(predict[i]) + (1 - actual[i])*math.log(1 - predict[i]))
    total_error = total_error + error

loss = total_error/len(actual)

print("BCE is:",loss)