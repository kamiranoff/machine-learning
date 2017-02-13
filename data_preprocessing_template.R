# Data Preprocessing

# set working directory
setwd("~/nemeacreation/sites/tutorials/machine-learning")
# Importing the dataset
dataset = read.csv('Data.csv')

# Replace missing values with the mean (the average)
#is.na = is missing..
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                        dataset$Salary)
      
# Encoding Categorical data
dataset$Country = factor(dataset$Country,
                         levels = c('France', 'Spain', 'Germany'),
                         labels = c(1,2,3))

dataset$Purchased = factor(dataset$Purchased,
                             levels = c('No', 'Yes'),
                             labels = c(0,1))

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

