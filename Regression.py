"""
Directly Copy Pasted from 
=> https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
Because I don't wanted to spend my precious time by
figuring out what this sh*t even do!!

(But I have spent my time for searching , copying , pasting and writing this comment though😎😎)
"""

import numpy as np
from sklearn.linear_model import LinearRegression
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
# y = 1 * x_0 + 2 * x_1 + 3
y = np.dot(X, np.array([1, 2])) + 3
reg = LinearRegression().fit(X, y)
print(reg.score(X, y))

print(reg.coef_)

print(reg.intercept_)

print(reg.predict(np.array([[3, 5]])))