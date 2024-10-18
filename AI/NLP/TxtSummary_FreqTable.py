# The provided Python code performs extractive text summarization using the Natural Language Toolkit (NLTK). It begins by tokenizing an input text into words and sentences while filtering out stopwords. A frequency table is created to count occurrences of each word, which is then used to score each sentence based on the words it contains. The average sentence score is calculated, and sentences are selected for the summary if their score exceeds a specified weight multiplied by this average. Finally, the code prints both the original text and the generated summary.

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


weight = 1.2
# if a sentence score is greaterh then ( weight * avgSenScore) then it is part of summary
# avgSenScore: Average value of a sentence from the original text

# Input text - to summarize 
text = "There are many techniques available to generate extractive summarization to keep it simple, I will be using an unsupervised learning approach to find the sentences similarity and rank them. Summarization can be defined as a task of producing a concise and fluent summary while preserving key information and overall meaning. One benefit of this will be, you don’t need to train and build a model prior start using it for your project. It’s good to understand Cosine similarity to make the best use of the code you are going to see. Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them. Its measures cosine of the angle between vectors. The angle will be 0 if sentences are similar."

print ("---------Text---------")

print(text)

# Tokenizing the text
stopWords = set(stopwords.words("english"))
words = word_tokenize(text)
#print (words)


# Creating a frequency table to keep the score of each word
   
freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1

# Creating a dictionary to keep the score of each sentence
sentences = sent_tokenize(text)
sentenceValue = dict()
   
for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq

sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]
   
# avgSenScore: Average value of a sentence from the original text
avgSenScore = int(sumValues / len(sentenceValue))
   
# Storing sentences into our summary.
summary = ''
for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (weight * avgSenScore)):
        summary += " " + sentence

print ("---------Summary---------")
print(summary)


## ResearchGate: http://www.researchgate.net/profile/Murtaza_Khan2/
## LinkedIn: https://www.linkedin.com/in/dr-murtaza-ali-khan-3b368019
## Google Scholar: https://scholar.google.com/citations?user=n0JDQ0sAAAAJ
## Scopus: https://www.scopus.com/authid/detail.uri?authorId=7410318323
## GitHub: https://github.com/drmurtazakhan


