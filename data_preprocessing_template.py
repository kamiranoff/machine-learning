#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 23:47:25 2016

@author: kevin
"""

# Librairies
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Dataset
dataset = pd.read_csv('Data.csv')

# Matrix of features: Independant variables
# iloc --> first argument is lines, second is columns.
# : means we are taking all the lines
# :-1 means we exclude the last one which is a dependant variable
x = dataset.iloc[:, :-1].values

# DEPENDANT Variables Vector
# storing the last column.
y = dataset.iloc[:, 3].values


# Taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values= 'NaN', strategy='mean', axis=0)

# fit to colum at index 1 and 2 age and salary -> Upperbound not included
imputer = imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])