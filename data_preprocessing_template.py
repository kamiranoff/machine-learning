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
dataset = pandas.read_csv('./data/Data.csv')

# Matrix of features: Independant variables
# iloc --> first argument is lines, second is columns.
# : means we are taking all the lines
# :-1 means we exclude the last one which is a dependant variable
X = dataset.iloc[:, :-1].values

# DEPENDANT Variables Vector
# storing the last column.
Y = dataset.iloc[:, 3].values


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split

# 20% are going in the test set
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

# Feature scaling
# Process of modifing variables (Here age and salary) so they have the scale.
#from sklearn.preprocessing import StandardScaler
#sc_X = StandardScaler()
#X_train = sc_X.fit_transform(X_train)
#X_test = sc_X.transform(X_test)

