import sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer

text ="""Sumy is a Python library designed for Natural Language Processing (NLP) tasks, primarily focused on automatic summarization of text using various algorithms. It offers different summarizers based on techniques like Luhn, Edmundson, LSA, LexRank, and KL-summarization. The following sections will provide a detailed exploration of each algorithm. Sumy enables users to create summaries with minimal coding effort and can be seamlessly integrated with other NLP tasks, making it ideal for summarizing extensive documents.Tokenization is one of the most important task in text preprocessing. In tokenization, we divide a paragraph into sentences and then breakdown those sentences into individual words. By tokenizing the text, Sumy can better understand its structure and meaning, which improves the accuracy and quality of the summaries generated."""

print ("---------Text---------")
print(text)

# For Strings
parser = PlaintextParser.from_string(text,Tokenizer("english"))

# Using Luhn
summarizer_luhn = LuhnSummarizer()
#Summarize the document with 2 sentences
summary =summarizer_luhn(parser.document,2)


print ("---------Summary---------")
for sentence in summary:
    print(sentence)

    
## ResearchGate: http://www.researchgate.net/profile/Murtaza_Khan2/
## LinkedIn: https://www.linkedin.com/in/dr-murtaza-ali-khan-3b368019
## Google Scholar: https://scholar.google.com/citations?user=n0JDQ0sAAAAJ
## Scopus: https://www.scopus.com/authid/detail.uri?authorId=7410318323
## GitHub: https://github.com/drmurtazakhan







