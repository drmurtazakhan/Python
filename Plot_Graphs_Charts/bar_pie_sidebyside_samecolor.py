import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('C:/0MAK/RW\PythonKhan/Plot/scores.csv')
cat_vars = ['Borough', 'SAT Section']

for var in list(cat_vars):
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    counts_df = df[var].value_counts()
    counts_df.plot(kind='pie', autopct=lambda v: f'{v:.2f}%', ax=ax[0])
    sns.barplot(x=counts_df.index, y=counts_df.values, saturation=1, ax=ax[1])
    ax[1].bar_label(ax[1].containers[0])