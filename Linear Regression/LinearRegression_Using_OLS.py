import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('student_scores.csv')
print(data.shape)
print(data.head())

X = data['Hours'].values.reshape(-1, 1)
Y = data['Scores'].values.reshape(-1, 1)
print(X)
print(Y)

plt.scatter(X,Y)
plt.legend(["Data Points"])
plt.title("Scatter Graph for Visualizing Hours vs Scores")
plt.xlabel("Hours")
plt.ylabel("Scores")
plt.show()

reg = LinearRegression()
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2)
reg = reg.fit(X_train, y_train)
print(reg.intercept_)
print(reg.coef_)

y_pred = reg.predict(X_test)
df_preds = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print(df_preds)