import os
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
os.system('cls')


df = pd.read_csv('C:/0MAK/RW/PythonKhan/AI/Diabetes/diabetes_prediction_dataset.csv')

print(df.head())
print ("--------------------------------------------")
df.info()
print ("--------------------------------------------")

