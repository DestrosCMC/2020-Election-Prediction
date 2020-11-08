import pandas as pd
import numpy as np
import seaborn as sns
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

file_name = "election_data.xlsx"

# Change path to working directory
#os.chdir()

data = pd.read_excel(file_name, header = 0, index_col='Year')

data = data.drop(columns= "Name")
#print(data.head())

X = data.iloc[:, :9]
y = data.iloc[:, 9]
#print(X)
#print(y)

# >> Heat Map <<
# sns.heatmap(data.corr())
# plt.show()

# fig = plt.figure(figsize=(12,9))
# ax = sns.heatmap(data.corr())
# plt.show()

# >> Optimizing n_neighbors <<
# for k in range(1,10):
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
#     scaler = StandardScaler()
#     X_train = scaler.fit_transform(X_train)
#     X_test = scaler.fit_transform(X_test)
#
#     knnr = KNeighborsRegressor(n_neighbors=k, p=2)
#     knnr.fit(X_train, y_train)
#     # y_pred = classifier.predict(X_test)
#     y_pred = knnr.predict(X_test)
#
#     a = mean_squared_error(y_test, y_pred)
#     print("The MSE is:", a, k)

#5 MSE = 33.529

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=0)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

knnr = KNeighborsRegressor(n_neighbors=5, p=2)
knnr.fit(X_train, y_train)
#y_pred = classifier.predict(X_test)
y_pred = knnr.predict(X_test)

a = mean_squared_error(y_test, y_pred)
print("The MSE is:",a)



# Vote share of incumbent president

fig = plt.figure(figsize=(12,9))
ax = sns.regplot(y_test, y_pred, marker = 'o', color = 'blue')
ax.set_title('KNN Regression', fontsize=20)
ax.set_xlabel('Actual Democratic Vote Share', fontsize=20)
ax.set_ylabel('Predicted Democratic Candidate Vote Share', fontsize=20)
plt.show()


#>> Final Prediction <<
#Predict out of sample data
knnr.fit(X, y)

democraticNominee2020_x = [[52387, 8.4, 1, 1, 1, 0, -0.9, -13.2, .0364]]
democraticNominee2020_pred = knnr.predict(democraticNominee2020_x)
print("Predicted 2020 Democratic Nominee Vote Share:", democraticNominee2020_pred)
