import pickle
import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

os.chdir(r'/Users/macbook/Downloads')

# importing the csv file using pandas
df = pd.read_csv('Salary_Data.csv')

x = df['YearsExperience']
y = df['Salary']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

x_train = np.array(x_train).reshape(-1, 1)

regressor = LinearRegression()
regressor.fit(x_train, y_train)

# Saving model to disk aka pickling
pickle.dump(regressor, open('model.pkl', 'wb'))
