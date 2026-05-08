## Ref: https://www.kaggle.com/code/sasakitetsuya/how-can-we-prevent-road-rage

import os
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns


# Clearing the Screen
os.system('cls')

print ("---------WELCOME---------")

df_train = pd.read_csv('C:/0MAK/RW/PythonKhan/AI/Traffic/train_motion_data.csv')
df_test = pd.read_csv('C:/0MAK/RW/PythonKhan/AI/Traffic/test_motion_data.csv')
print ("--------------------------------------------")
print(df_train.tail())
print ("--------------------------------------------")
df_train.info()
print ("--------------------------------------------")
print(df_train.columns)
print ("--------------------------------------------")
print(df_train['Class'].unique())
print ("--------------------------------------------")

'''
# The purpose of this note book is to find the model by which we can 
classify 'Normal' or 'Not Normal'('Slow' or 'Aggressive'). 
So I replaced 'Class' by '0' or '1' for binary classification.
''' 

df_train['Class'] = df_train['Class'].replace(['NORMAL', 'SLOW', 'AGGRESSIVE'],[1, 0, 1])
df_test['Class'] = df_test['Class'].replace(['NORMAL', 'SLOW', 'AGGRESSIVE'],[1, 0, 1])

df_train.groupby('Class')['Class'].count().plot.bar()
plt.show()


sns.boxplot(x='Class', y='AccX',data=df_train)
plt.show()

sns.heatmap(df_train.corr(),annot=True, cbar=True, cmap='Blues', fmt='.1f')
plt.show()
