import pandas as pd
import xgboost as xgb
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
import matplotlib.pyplot as plt

import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


df = pd.read_csv('C:/0MAK/RW/PythonKhan/AI/Diabetes/diabetes_prediction_dataset.csv')

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
pd.set_option('display.max_columns', None)
#print (df.describe().T)
#print ("--------------------------------------------")
print (df.describe())
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
## -------------------------------------------------------
   
# Diabetes Statistics 
labelsDiabetes = ['0', '1']
valuesDiabetes = df['diabetes'].value_counts(sort=False).values
dfDiabetes = pd.DataFrame({"diabetes": labelsDiabetes, "Count": valuesDiabetes})
print(dfDiabetes)

df_NoDiabetes_HighGlucose = df[ (df.blood_glucose_level>180) & (df.diabetes==0)]
print('Number Of Samples with NoDiabetes and High Glucose ', len(df_NoDiabetes_HighGlucose))


print ("--------------------------------------------")
plt.style.use('fivethirtyeight')
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
##sns.countplot(x=df['diabetes'], data=df, palette='Set2')
sns.countplot(x=df['diabetes'], data=df)
plt.subplot(1, 2, 2)
plt.pie(valuesDiabetes, labels=labelsDiabetes, autopct='%1.2f%%')
plt.savefig('Diabetes-Statistics')

## -------------------------------------------------------
# Gender Statistics 
labelsGender = ['Female', 'Male', 'Other']
valuesGender = df['gender'].value_counts(sort=False).values

dfGender = pd.DataFrame({"Gender": labelsGender, "Count": valuesGender})
print(dfGender)
print ("--------------------------------------------")
#plt.style.use('fivethirtyeight')
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
#sns.countplot(x=df['gender'], data=df, palette='Set2')
sns.countplot(x=df['gender'], data=df)
plt.subplot(1, 2, 2)
plt.pie(valuesGender, labels=labelsGender, autopct='%1.2f%%')
plt.savefig('Gender-Statistics')
plt.show(block=False)
# sys. exit()
## -------------------------------------------------------
# Smoking Statistics
labelsSmoking = ['never', 'No Info', 'current', 'former', 'ever', 'not current']
valuesSmoking = df['smoking_history'].value_counts(sort=False).values

dfSmoking = pd.DataFrame({"Smoking History": labelsSmoking, "Count": valuesSmoking})
print(dfSmoking)
print ("--------------------------------------------")
plt.style.use('fivethirtyeight')
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
sns.countplot(x=df['smoking_history'], data=df)
plt.xticks(rotation=30)

plt.subplot(1, 2, 2)
plt.pie(valuesSmoking, labels=labelsSmoking, autopct='%1.1f%%')
plt.savefig('Smoking-Statistics')
plt.show(block=False)

#fig, ax = plt.subplots()
#ax.pie(valuesSmoking, labels=labelsSmoking, autopct='%1.1f%%')
#df.smoking_history.value_counts().sort_values().plot(kind='bar')

## -------------------------------------------------------
# Plot Age, BMI, 'Blood Glucose, and HbA1c Statistics
numerical = ['age', 'bmi', 'blood_glucose_level', 'HbA1c_level']


# statstr Aggregate statistic to compute in each bin. Choose one the following:
    # count: show the number of observations in each bin
    # frequency: show the number of observations divided by the bin width
    # probability or proportion: normalize such that bar heights sum to 1
    # percent: normalize such that bar heights sum to 100
    # density: normalize such that the total area of the histogram equals 1

#AggregateStat="percent"  
AggregateStat="density"  


noOfBins = 10;

## age
plt.figure(figsize=(10, 6))
sns.histplot(df[numerical[0]], kde=True, bins=noOfBins, stat=AggregateStat)
#sns.histplot(df[numerical[0]], kde=True, bins=10)

## bmi
plt.figure(figsize=(10, 6))
sns.histplot(df[numerical[1]], kde=True, bins=noOfBins, stat=AggregateStat)

## blood_glucose_level
plt.figure(figsize=(10, 6))
sns.histplot(df[numerical[2]], kde=True, bins=noOfBins, stat=AggregateStat)

## HbA1c_level
plt.figure(figsize=(10, 6))
sns.histplot(df[numerical[3]], kde=True, bins=noOfBins, stat=AggregateStat)

plt.show(block=False)
## -------------------------------------------------------
#Categorical encoding of Non-numeric columns: gender and smoking_history)
cat_cols = ["gender", "smoking_history"]
enc = OrdinalEncoder()

df[cat_cols] = enc.fit_transform(df[cat_cols])
print ("............. df.head(): Categorical encoding of gender and smoking_history ............. ")
print(df[cat_cols])
print ("--------------------------------------------")

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    df.drop("diabetes", axis=1), df["diabetes"], test_size=0.2, random_state=6)

# Model architechure
model = XGBClassifier(
    n_estimators=400,
    eval_metric='error',    
    max_depth=3,
    learning_rate=0.1,
)

## model=xgb.XGBRegressor(n_estimators=100, eval_metric='rmse')
## model.fit(X_train,y_train, early_stopping_rounds=10, eval_set=[(X_test, y_test)], verbose=False)

# Model training
model.fit(
    X_train, y_train,
    eval_set=[(X_test, y_test)],
    #eval_metric="auc",
    #early_stopping_rounds=500,
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

## ResearchGate: http://www.researchgate.net/profile/Murtaza_Khan2/
## LinkedIn: https://www.linkedin.com/in/dr-murtaza-ali-khan-3b368019
## Google Scholar: https://scholar.google.com/citations?user=n0JDQ0sAAAAJ
## Scopus: https://www.scopus.com/authid/detail.uri?authorId=7410318323
## GitHub: https://github.com/drmurtazakhan
