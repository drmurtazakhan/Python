## Ref.
## Gradient Boosted Diabetes Prediction: 97.4% acc.
## https://www.kaggle.com/code/chriss4123/gradient-boosted-diabetes-prediction-97-4-acc

## My work on Kaggle
## Sign in using Google account khanmapk@gmail.com
## https://www.kaggle.com/code/drmurtazaakhan/notebook32833ee846/edit

import os
import sys
import numpy as np # linear algebra
import pandas as pd
import xgboost as xgb
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
import matplotlib.pyplot as plt

import seaborn as sns
from scipy import stats


import warnings
warnings.filterwarnings("ignore")

# Clearing the Screen
# os.system('cls')


#df = pd.read_csv('C:/0MAK/RW/PythonKhan/AI/Diabetes/diabetes_prediction_dataset.csv')
df = pd.read_csv('diabetes_dataset.csv')
#df = pd.read_csv(open('diabetes_dataset.csv'),sep=',',delimiter=None, index_col=0)

## to show all the columns
## pd.set_option("display.max_columns", None)

print ("............. df.head() .............")
print(df.head())
print ("............. df.info() .............")
df.info()
print ("--------------------------------------------")

#sys.exit()

samples, features = df.shape
print('Number Of Samples: ', samples)
print('Number Of Features: ', features)
print ("............. Null Count .............")

# Preprocessing and Cleaning Data (check null values of each column)
print(df.isnull().sum())


# Generate descriptive statistics.
print ("............. describe().T  (descriptive statistics).............")
print (df.describe().T)
print ("--------------------------------------------")
print ("............. unique values of each attribute .............")
# unique values
d = []
u = []
t = []
for col in df:
    d.append(col)
    u.append(df[col].nunique())
    t.append(df[col].dtype)
print(pd.DataFrame({'column':d,'type': t ,'unique value' : u}))
print ("--------------------------------------------")

# Plot Gender Statistics
labels = ['Female', 'Male', 'Other']
values = df['gender'].value_counts().values

plt.style.use('fivethirtyeight')
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
sns.countplot(x=df['gender'], data=df)
plt.subplot(1, 2, 2)
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.savefig('Gender-Statistics')
plt.show(block=False)

# Plot Smoking Statistics
labels = ['Never', 'No Info', 'Former', 'Current', 'Not current', 'Ever']
values = df['smoking_history'].value_counts().values
plt.style.use('fivethirtyeight')
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
sns.countplot(x=df['smoking_history'], data=df)
plt.subplot(1, 2, 2)
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.savefig('Smoking-Statistics')
plt.show(block=False)

# Plot Age, BMI, 'Blood Glucose, and HbA1c Statistics
numerical = ['age', 'bmi', 'blood_glucose_level', 'HbA1c_level']
i = 0

while i < 4:
  plt.figure(figsize=(10, 6))
  plt.subplot(1, 2, 1)
  sns.distplot(df[numerical[i]])
  i += 1
  if i == 4:
    break
  plt.subplot(1, 2, 2)
  sns.distplot(df[numerical[i]])
  i += 1
  plt.show(block=False)
plt.savefig('2')


#Categorical encoding of Non-numeric columns: gender and smoking_history)
cat_cols = ["gender", "smoking_history"]
enc = OrdinalEncoder()

df[cat_cols] = enc.fit_transform(df[cat_cols])
print ("............. df.head(): Categorical encoding of gender and smoking_history ............. ")
print(df.head())
print ("--------------------------------------------")

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    df.drop("diabetes", axis=1), df["diabetes"], test_size=0.2, random_state=6)

# Model architechure
model = XGBClassifier(
    n_estimators=400,
    max_depth=3,
    learning_rate=0.1,
)

# Model training
model.fit(
    X_train, y_train,
    eval_set=[(X_test, y_test)],
    eval_metric="error",
    early_stopping_rounds=500,
    verbose=10,
)
print ("--------------------------------------------")
# Model evaluation
print("Model validation accuracy: %.2f%%" % (model.score(X_test, y_test) * 100))
print ("--------------------------------------------")
# Plot the validation error
results = model.evals_result()
epochs = len(results["validation_0"]["error"])
x_axis = range(0, epochs)
plt.plot(x_axis, results["validation_0"]["error"], label="Validation error")
plt.legend()
plt.ylabel("Error")
plt.xlabel("Epochs")
plt.title("Model validation error")
plt.show(block=False)

# Feature importance
xgb.plot_importance(model)

plt.show(block=True)

print ("------  THE END   ----------")
'''
# The purpose of this note book is to find the model by which we can 
classify 'Normal' or 'Not Normal'('Slow' or 'Aggressive'). 
So I replaced 'Class' by '0' or '1' for binary classification.


df_train.groupby('Class')['Class'].count().plot.bar()
plt.show(block=False)


sns.boxplot(x='Class', y='AccX',data=df_train)
plt.show(block=False)

sns.heatmap(df_train.corr(),annot=True, cbar=True, cmap='Blues', fmt='.1f')
plt.show(block=False)
''' 