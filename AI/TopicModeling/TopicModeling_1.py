import re

import pandas as pd
#import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import spacy

#import pyLDAvis.gensim_models

import en_core_web_md



#from gensim.corpora.dictionary import Dictionary
#from gensim.models import LdaMulticore
#from gensim.models import CoherenceModel



#df = pd.read_csv('R:\PythonKhan\DataFiles\CSV\IWD_20Tweets.csv', encoding = "utf-8", skipinitialspace = True)

df = pd.read_csv('Tweets20.csv', encoding = "utf-8", skipinitialspace = True)

print(df)

print ("------------------------")
row, col = df.shape

print ("Number of rows: " + str(row))
print ("Number of cols: " + str(col))
print ("------------------------")
# apply the dtype attribute to find types of columns
dfType = df.dtypes
print("Types of dataframe columns:")
print(dfType)
print ("------------------------")

# remove non ASCII characters
df.text.replace({r'[^\x00-\x7F]+':''}, regex=True, inplace=True)

# Remove URLs
df['text'] = df['text'].apply(lambda x: re.split('https:\/\/.*', str(x))[0])

# Define the regular expression pattern
pattern = r'[^\w\s]'

# Remove special characters from the 'text' column
df['text'] = df['text'].apply(lambda x: re.sub(pattern, '', x))

print(df.head())

# Our spaCy model:
nlp = en_core_web_md.load()

# Tags I want to remove from the text
removal= ['ADV','PRON','CCONJ','PUNCT','PART','DET','ADP','SPACE', 'NUM', 'SYM']
tokens = []
