#0 = Loan rejected
#1 = Loan approved

from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

#----------------------------------------------------
# 1.create dataset
#----------------------------------------------------
X = pd.DataFrame([
[25000, 600, 200000, 10000, 0],
[40000, 700, 300000, 8000, 1],
[60000, 750, 500000, 12000, 1],
[20000, 550, 150000, 15000, 0],
[80000, 800, 700000, 10000, 1],
[35000, 650, 250000, 9000, 1],
[18000, 500, 100000, 12000, 0],
[90000, 850, 800000, 15000, 1],
[30000, 580, 200000, 14000, 0],
[70000, 780, 600000, 10000, 1]
], columns=['Income', 'Credit_Score', 'Loan_Amount', 'Existing_EMI', 'Employment_Status'])

Y= pd.Series([
0, 1, 1, 0, 1,
1, 0, 1, 0, 1
])

#----------------------------------------------------
#2.Preprocess categorical values
#----------------------------------------------------
print("No categorical values present")

#----------------------------------------------------
#2.split the dataset
#----------------------------------------------------
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

#----------------------------------------------------
#3.scaling
#----------------------------------------------------
scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.transform(X_test)

#----------------------------------------------------
#4.model train
#----------------------------------------------------

model = MLPClassifier(hidden_layer_sizes=(8,4),
                      activation='relu',
                      max_iter=1000,
                      random_state=42)

model = model.fit(X_train_scaled,Y_train)

#----------------------------------------------------
#5.evaluate model
#----------------------------------------------------

Y_pred = model.predict(X_test_scaled)

print("actual values:")
print(Y_test)
print("predicted values:")
print(Y_pred)


#----------------------------------------------------
#7.test input
#----------------------------------------------------
new_applicant = pd.DataFrame([[55000, 720, 400000, 10000, 1]],
                             columns=['Income', 'Credit_Score', 'Loan_Amount', 'Existing_EMI', 'Employment_Status'])
new_applicant_scaled = scalar.transform(new_applicant)

prediction =model.predict(new_applicant_scaled)

if prediction[0] == 0:
    print("Loan rejected")

else:
    print("Loan approved")





