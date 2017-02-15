# Data Preprocessing

# set working directory
setwd("~/nemeacreation/sites/tutorials/machine-learning")
# Importing the dataset
dataset = read.csv('data/Data.csv')

# Select sub dataset from dataset
# dataset = dataset[, 2:3];

# Splitting the dataset into the Training set and Test set

# Run this line to install the package
#install.packages('caTools')
library(caTools)
set.seed(123)

# 20% for the test set -> 0.8 for the train set
split = sample.split(dataset$Purchased, SplitRatio = 0.8)

# Sets
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature scaling
# Process of modifing variables (Here age and salary) so they have the scale.
# training_set[,2:3] = scale(training_set[,2:3])
# test_set[,2:3] = scale(test_set[,2:3])

