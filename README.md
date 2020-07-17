# Text Summariser

Install NLTK module

```bash
pip install nltk
```

1. Importing required libraries 

```python
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
```
There are two NLTK libraries that will be necessary for building an efficient feedback summarizer.

- **Corpus**
Corpus means a collection of text. It could be data sets of anything containing texts be it poems by a certain poet, bodies of work by a certain author, etc. In this case, we are going to use a data set of pre-determined stop words.

- **Tokenizers**
it divides a text into a series of tokens. There are three main tokenizers – word, sentence, and regex tokenizer. We will only use the word and sentence tokenizer

2. Download stopwords and punkt

```python
nltk.download('stopwords')
nltk.download('punkt')
```
3. Frequency tables
A python dictionary that’ll keep a record of how many times each word appears in the feedback after removing the stop words.we can use the dictionary over every sentence to know which sentences have the most relevant content in the overall text.

```python
stopWords = set(stopwords.words("english")) 
words = word_tokenize(text) 
freqTable = dict() 
```

4. Assign score to each sentence depending on the words it contains and the frequency table

```python
sentences = sent_tokenize(text) 
sentenceValue = dict()
```

5. Assign a certain score to compare the sentences within the feedback.
A simple approach to compare our scores would be to find the average score of a sentence. The average itself can be a good threshold.

```python
sumValues = 0
for sentence in sentenceValue: 
    sumValues += sentenceValue[sentence] 
average = int(sumValues / len(sentenceValue)) 
```
Apply the threshold value and store sentences in order into the summary.

Check the complete code in [app.py](https://github.com/kamaravichow/text-summariser-python/blob/master/app.py)

Peace !



 
