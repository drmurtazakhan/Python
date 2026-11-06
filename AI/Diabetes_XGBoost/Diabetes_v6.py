import os
import matplotlib.pyplot as plt

# 1. Clear the console
os.system('cls' if os.name == 'nt' else 'clear')

# 2. Close all open plot windows
plt.close('all')

# 3. Clear workspace variables
for name in list(globals()):
    if not name.startswith('_'):
        del globals()[name]

import matplotlib.pyplot as plt        
import numpy as np
import pandas as pd
import xgboost as xgb
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve, auc

import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


df = pd.read_csv(r'J:\Python\AI\Diabetes_XGBoost\diabetes_prediction_dataset.csv')

print ("............. df.head() .............")
print(df.head())
print ("............. df.info() .............")
df.info()
print ("--------------------------------------------")

samples, features = df.shape
print('Number Of Samples: ', samples)
print('Number Of Features: ', features)
print ("............. Null Count .............")

# Preprocessing and Cleaning Data (check null values of each column)
print(df.isnull().sum())

# Generate descriptive statistics.
print ("............. describe().T  (descriptive statistics).............")
pd.set_option('display.max_columns', None)
print (df.describe())
print ("............. unique values of each attribute .............")
d = []
u = []
t = []
for col in df:
    d.append(col)
    u.append(df[col].nunique())
    t.append(df[col].dtype)
print(pd.DataFrame({'column':d,'type': t ,'unique value' : u}))
print ("--------------------------------------------")
   
# Diabetes Statistics 
labelsDiabetes = ['0', '1']
valuesDiabetes = df['diabetes'].value_counts(sort=False).values
dfDiabetes = pd.DataFrame({"diabetes": labelsDiabetes, "Count": valuesDiabetes})
print(dfDiabetes)
print ("--------------------------------------------")

# Diabetes & bmi
count_bmi_normal = len(df[ (df.bmi < 25)])
percent_count_bmi_normal = (count_bmi_normal/samples)*100

count_bmi_overweight = len(df[ (df.bmi >= 25) & (df.bmi < 30)])
percent_count_bmi_overweight = (count_bmi_overweight/samples)*100

count_bmi_obese = len(df[ (df.bmi >= 30) & (df.bmi < 40)])
percent_count_bmi_obese = (count_bmi_obese/samples)*100

count_bmi_morbidlyObese = len(df[ (df.bmi >= 40)])
percent_count_bmi_morbidlyObese = (count_bmi_morbidlyObese/samples)*100

labelsBMI = ['Normal', 'Overweight', 'Obese', 'Morbidly-Obese']
valuesBMI =[count_bmi_normal, count_bmi_overweight, count_bmi_obese, count_bmi_morbidlyObese]
percent_valuesBMI =[percent_count_bmi_normal, 
                    percent_count_bmi_overweight,
                    percent_count_bmi_obese,
                    percent_count_bmi_morbidlyObese]

dfBMI_4Types = pd.DataFrame({"BMI": labelsBMI, "Count": valuesBMI, "PercentOfAll": percent_valuesBMI})
print(dfBMI_4Types)
print ("--------------------------------------------")

# Diabetes & blood_glucose_level
count_HighGlucose_NoDiabetes = len(df[ (df.blood_glucose_level > 180) & (df.diabetes==0)])
print('Number Of Samples with no Diabetes and High Glucose are', count_HighGlucose_NoDiabetes)

# Diabetes & Age <=65
count_AgeEqOrLess65 = len(df[ (df.age <= 65)])
percent_count_AgeEqOrLess65 = (count_AgeEqOrLess65/samples)*100
print("Number Of Samples age less than or equal 65 are %.0f (%.2f%% of %.0f) " % (count_AgeEqOrLess65, percent_count_AgeEqOrLess65, samples))

count_AgeEqOrLess65_Diabetes = len(df[ (df.age <= 65) & (df.diabetes==1)])
percent_AgeEqOrLess65_Diabetes = (count_AgeEqOrLess65_Diabetes/count_AgeEqOrLess65) * 100
print("Number Of Samples age less than or equal 65 with Diabetes are %.0f (%.2f%% of %.0f) " % (count_AgeEqOrLess65_Diabetes, percent_AgeEqOrLess65_Diabetes, count_AgeEqOrLess65))

# Diabetes & Age > 65
count_AgeAbove65 = len(df[ (df.age > 65)])
percent_count_AgeAbove65 = (count_AgeAbove65/samples)*100
print("Number Of Samples age above 65 are %.0f (%.2f%% of %.0f) " % (count_AgeAbove65, percent_count_AgeAbove65, samples))

count_AgeAbove65Diabetes = len(df[ (df.age > 65) & (df.diabetes==1)])
percent_AgeAbove65Diabetes = (count_AgeAbove65Diabetes/count_AgeAbove65)*100
print("Number Of Samples age above 65 with Diabetes are %.0f (%.2f%% of %.0f) " % (count_AgeAbove65Diabetes, percent_AgeAbove65Diabetes, count_AgeAbove65))

print ("--------------------------------------------")
plt.style.use('fivethirtyeight')
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
sns.countplot(x=df['diabetes'], data=df)
plt.subplot(1, 2, 2)
plt.pie(valuesDiabetes, labels=labelsDiabetes, autopct='%1.2f%%')
plt.savefig('distribution_diabetes.png', dpi=300)

# Gender Statistics 
labelsGender = ['Female', 'Male', 'Other']
valuesGender = df['gender'].value_counts(sort=False).values

dfGender = pd.DataFrame({"Gender": labelsGender, "Count": valuesGender})
print(dfGender)
print ("--------------------------------------------")
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
sns.countplot(x=df['gender'], data=df)
plt.subplot(1, 2, 2)
plt.pie(valuesGender, labels=labelsGender, autopct='%1.2f%%')
plt.savefig('distribution_gender.png', dpi=300)
plt.show(block=False)

# Smoking Statistics
labelsSmoking = ['never', 'No Info', 'current', 'former', 'ever', 'not current']
valuesSmoking = df['smoking_history'].value_counts(sort=False).values

print(df['smoking_history'].value_counts())

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
plt.savefig('distribution_smoking.png', dpi=300)
plt.show(block=False)

# Plot Age, BMI, Blood Glucose, and HbA1c Statistics with Exactly 10 Bins & Explicit Ticks
numerical = ['age', 'bmi', 'blood_glucose_level', 'HbA1c_level']
AggregateStat = "density"

for col in numerical:
    plt.figure(figsize=(10, 6))
    
    if col == 'age':
        bin_edges = np.linspace(0, 80, 11)
    else:
        min_val = df[col].min()
        max_val = df[col].max()
        bin_edges = np.linspace(min_val, max_val, 11)
    
    ax = sns.histplot(
        df[col], 
        kde=True, 
        bins=bin_edges, 
        stat=AggregateStat,
        color='skyblue',
        edgecolor='black',
        linewidth=1.2,
        line_kws={'color': 'darkorange', 'linewidth': 2.5}
    )
    
    tick_labels = [f"{int(val)}" for val in bin_edges]
    plt.xticks(bin_edges, tick_labels, rotation=35, fontsize=10)
    
    plt.title(f'Density Distribution of {col.replace("_", " ").title()} (10 Bins)', fontsize=14)
    plt.xlabel(col, fontsize=12)
    plt.ylabel('Density', fontsize=12)
    plt.tight_layout()
    plt.savefig(f'Density_Distribution_{col}_TenBins.png', dpi=300)

plt.show(block=False)

# Separate features and target
X = df.drop("diabetes", axis=1)
y = df["diabetes"]

# Train test split (with stratification to preserve class proportion)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=6, stratify=y
)

# Categorical encoding after split (prevents data leakage)
cat_cols = ["gender", "smoking_history"]
enc = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)

X_train[cat_cols] = enc.fit_transform(X_train[cat_cols])
X_test[cat_cols] = enc.transform(X_test[cat_cols])

print ("............. X_train.head(): Categorical encoding completed ............. ")
print(X_train[cat_cols].head())
print ("--------------------------------------------")

# Model architecture
model = XGBClassifier(
    n_estimators=400,
    eval_metric='error',    
    max_depth=3,
    learning_rate=0.1,
    scale_pos_weight=10.76
)

# Model training
model.fit(
    X_train, y_train,
    eval_set=[(X_test, y_test)],
    verbose=10,
)
print ("--------------------------------------------")

# Predictions on test set
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

# Model evaluation
print("Model validation accuracy: %.2f%%" % (model.score(X_test, y_test) * 100))
print("\n............. Confusion Matrix .............")
print(confusion_matrix(y_test, y_pred))

print("\n............. Classification Report .............")
print(classification_report(y_test, y_pred, digits=4))

print("ROC-AUC Score: %.4f" % roc_auc_score(y_test, y_proba))
print ("--------------------------------------------")

# Plot and save the validation error figure
results = model.evals_result()
epochs = len(results["validation_0"]["error"])
x_axis = range(0, epochs)
plt.figure(figsize=(8, 5))
plt.plot(x_axis, results["validation_0"]["error"], label="Validation error", color='crimson', linewidth=2)
plt.legend()
plt.ylabel("Error Rate")
plt.xlabel("Number of Trees (n_estimators)")
plt.title("Model Validation Error")
plt.tight_layout()
plt.savefig('Model_Validation_Error.png', dpi=300)
plt.show(block=False)

# Plot and save Feature Importance figure
plt.figure(figsize=(10, 6))
xgb.plot_importance(model)
plt.tight_layout()
plt.savefig('Feature_Importance.png', dpi=300)
plt.show(block=False)

# NEW: Plot and save ROC Curve figure
fpr, tpr, thresholds = roc_curve(y_test, y_proba)
roc_auc = auc(fpr, tpr)
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.4f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate', fontsize=12)
plt.ylabel('True Positive Rate', fontsize=12)
plt.title('Receiver Operating Characteristic (ROC) Curve', fontsize=14)
plt.legend(loc='lower right', fontsize=11)
plt.tight_layout()
plt.savefig('ROC_Curve.png', dpi=300)
plt.show(block=False)

# NEW: Plot and save Confusion Matrix Heatmap figure
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=['Non-Diabetic (0)', 'Diabetic (1)'],
            yticklabels=['Non-Diabetic (0)', 'Diabetic (1)'])
plt.title('Confusion Matrix Heatmap', fontsize=14)
plt.xlabel('Predicted Label', fontsize=12)
plt.ylabel('True Label', fontsize=12)
plt.tight_layout()
plt.savefig('Confusion_Matrix_Heatmap.png', dpi=300)
plt.show(block=True)

print ("------  THE END   ----------")