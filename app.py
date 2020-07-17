# importing libraries 
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
# from collections import Counter
   

# nltk.download('stopwords')
# nltk.download('punkt')


# Input text - to summarize  
text = "Russian hackers are attempting to steal coronavirus vaccine research, the American, British and Canadian governments said Thursday, accusing the Kremlin of opening a new front in its spy battles with the West amid the worldwide competition to contain the pandemic. The National Security Agency said that a hacking group implicated in the 2016 break-ins into Democratic Party servers has been trying to steal intelligence on vaccines from universities, companies and other health care organizations. The group, associated with Russian intelligence and known as both APT29 and Cozy Bear, has sought to exploit the chaos created by the coronavirus pandemic, officials said. American intelligence officials said the Russians were aiming to steal research to develop their own vaccine more quickly, not to sabotage other countries efforts. There was likely little immediate damage to global public health, cybersecurity experts said. The Russian espionage nevertheless signals a new kind of competition between Moscow and Washington akin to Cold War spies stealing technological secrets during the space race generations ago. The Russian hackers have targeted British, Canadian and American organizations using malware and sending fraudulent emails to try to trick their employees into turning over passwords and other security credentials, all in an effort to gain access to the vaccine research as well as information about medical supply chains. The accusations against Russia were also the latest example of an increasing willingness in recent months by the United States and its closest intelligence allies to publicly accuse foreign adversaries of breaches and cyberattacks. The American government has previously warned about efforts by China and Iran to steal vaccine research. Attributing such attacks, however, is imprecise, an ambiguity that Moscow takes advantage of in denying responsibility, as it did Thursday. Still, government officials, as well as outside experts, expressed strong confidence that Cozy Bear, controlled by Russia’s elite S.V.R. intelligence agency, was responsible for the attempted intrusions into the virus vaccine research. We condemn these despicable attacks against those doing vital work to combat the coronavirus pandemic, said Paul Chichester, the director of operations for Britain’s National Cyber Security Center. The head of the center, Ciaran Martin, told NBC News that the cyberattacks were first detected in February and that no evidence had emerged that data was stolen."

# def count_words(text):
#     skips = [".", ",", ":", ";", "'", '"']
#     for ch in skips:
#         text = text.replace(ch, "")
#     word_counts = {}
#     for word in text.split(" "):
#         if word in word_counts:
#             word_counts[word] += 1
#         else:
#             word_counts[word] = 1
#     return word_counts



# Tokenizing the text 
stopWords = set(stopwords.words("english")) 
words = word_tokenize(text) 
   
# Creating a frequency table to keep the  
# score of each word 
   
freqTable = dict() 
for word in words: 
    word = word.lower() 
    if word in stopWords: 
        continue
    if word in freqTable: 
        freqTable[word] += 1
    else: 
        freqTable[word] = 1
   
# Creating a dictionary to keep the score 
# of each sentence 
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
   
# Average value of a sentence from the original text 
   
average = int(sumValues / len(sentenceValue)) 
   
# Storing sentences into our summary. 
summary = '' 
for sentence in sentences: 
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)): 
        summary += " " + sentence 
print(summary) 