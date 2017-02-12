#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 23:47:25 2016

@author: kevin
"""

# Librairies

# Math Helper
import numpy

# plot Helper
import matplotlib.pyplot

# Import/Manage dataset
# import pandas as pd
import pandas

# Dataset
dataset = pandas.read_csv('Data.csv')

# Matrix of features: Independant variables
# iloc --> first argument is lines, second is columns.
# : means we are taking all the lines
# :-1 means we exclude the last one which is a dependant variable
X = dataset.iloc[:, :-1].values

# DEPENDANT Variables Vector
# storing the last column.
Y = dataset.iloc[:, 3].values


# Taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)

# fit to colum at index 1 and 2 age and salary -> Upperbound not included
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

from sklearn.preprocessing import LabelEncoder, OneHotEncoder


#Country
# Encode country column into numbers
labelEncoder_x = LabelEncoder()
X[:, 0] = labelEncoder_x.fit_transform(X[:, 0])

# Make a specific column for each entry in the column with boolean value
# so there is order in categorical variables
oneHotEncoder = OneHotEncoder(categorical_features=[0])
X = oneHotEncoder.fit_transform(X).toarray()


#Purchased
labelEncoder_y = LabelEncoder()
Y = labelEncoder_y.fit_transform(Y)

print(X)