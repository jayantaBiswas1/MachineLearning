import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDRegressor
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

data = pd.read_csv('student_scores.csv')
print(data.shape)
print(data.head())

X = data['Hours'].values.reshape(-1, 1)
Y = data['Scores'].values.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2)

clf_ = SGDRegressor()
clf_.fit(X_train, y_train)
y_pred = clf_.predict(X_test)
df_preds = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print(df_preds)

plt.scatter(y_test,y_pred)
plt.grid()
plt.xlabel('Actual y')
plt.ylabel('Predicted y')
plt.title('scatter plot between actual y and predicted y')
plt.show()
