# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 16:25:49 2023

@author: adity
"""
# =============================================================================
# ##############################Text Mining######################################
# =============================================================================
sentence="we are learning TextMining from Sanjivani AI"
###If we want to know position of learning
sentence.index('learning') #It will show the position of character
#It will show learning is at position 7
#This is going to show character position from 0 including
###############################################################################
#we want to know position TextMining word
sentence.split().index("TextMining") #it will show Position of words
#It will split the words in list and count the position
#If you want to see the list select sentence.split() and
#It will show at 3
###############################################################################
#Suppose we want to print any word in reverse order
sentence.split()[2][::-1] 
#[start:end end:-1(start)] will start from -1,-2,-3 till the end
#learning will be printed as gninrael
###############################################################################
#Suppose we want to print 1st and last word of the sentence
words=sentence.split()
first_word=words[0]
first_word
last_word=words[-1]
last_word
#Now we want to concate the first and last word
concat_word=first_word+" "+last_word
concat_word
###############################################################################
#We want to print even words from the sentence
[words[i] for i in range(len(words)) if i%2==0]
###############################################################################
sentence
#now we want to display only AI
sentence[-3:]
###############################################################################
#If we want to display entire sentence  in reverse order
sentence[::-1]
#IA inavijnaS morf gniniMtxeT gninrael era ew
###############################################################################
#Suppose we want to select each word and print in reversed order
words
print( " ".join(word[::-1]for word in words))
#ew era gninrael gniniMtxeT morf inavijnaS IA
###############################################################################
#tokenization
import nltk
nltk.download("punkt")
from nltk import word_tokenize
words=word_tokenize("I am reading NLP Fundamentals")
print(words)
###############################################################################
#Parts of speech (PoS) tagging
nltk.download('averaged_perceptron_tagger')
nltk.pos_tag(words)
###It is going mention parts of speech 
###############################################################################
#Stop words from nltk library
from nltk.corpus import stopwords
from nltk import word_tokenize
stop_words=stopwords.words('English')
#you can verify 179 stop words in veriable explorer 
print(stop_words)
sentence1="I am learning NLP:It is one of the most popular library in Python"
#First we will tokenize the sentence
sentence_words=word_tokenize(sentence1)
print(sentence_words)
#Now let us filter the sentence1 using stop_words
sentence_no_stops=" ".join([words for words in sentence_words if words not in stop_words])
print(sentence_no_stops)
sentence1
#you can notice that am,is,of,the most,popular,in are missing
###############################################################################
#suppose we want to replace words in string
sentence2="I visited MY from IND on 14-02-19"
normalized_sentence=sentence2.replace("MY","Malaysia").replace("IND","India")
normalized_sentence=normalized_sentence.replace("-19","-2020")
print(normalized_sentence)
###############################################################################
#Suppose we want auto correction in the sentence
#pip install autocorrect
from autocorrect import Speller
#declare the function Speller defined for English
spell=Speller(lang='en')
spell("Engilish")
spell("senteencee")
###############################################################################
#Suppose we want to correct whole sentence
sentence3="Ntural lanagage processin deals withh the aart of ectracting sentiiiments"
#let us first tokemnize this sentence
sentence3=word_tokenize(sentence3)
corrected_sentence=" ".join([spell(word) for word in sentence3])
print(corrected_sentence)
###############################################################################
#Stemming
stemmer=nltk.stem.PorterStemmer()
stemmer.stem("programming")
stemmer.stem("programmed")
stemmer.stem("Jumping")
stemmer.stem("Jumped")
###############################################################################
##Lematizer
#lematizer looks into dictionary words
nltk.download("wordnet")
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lemmatizer.lemmatize("programed")
lemmatizer.lemmatize("programs")

lemmatizer.lemmatize("battling")

lemmatizer.lemmatize("amazing")
###############################################################################
import spacy
nlp=spacy.load("en_core_web_sm")
nlp.pipe_names

doc=nlp("Tesla Inc is going to acquire Twitter for $45 billion")
for ent in doc.ents:
  print(ent.text, "|", ent.label_, "|", spacy.explain(ent.label_))

nlp.pipe_labels['ner']

doc = nlp("Michael Bloomberg founded Bloomberg in 1982")
for ent in doc.ents:
  print(ent.text, "|", ent.label_, "|", spacy.explain(ent.label_))
###############################################################################

doc = nlp("Tesla Inc is going to acquire Twitter Inc for $45 billion")
for ent in doc.ents:
  print(ent.text, "|", ent.label_, "|", spacy.explain(ent.label_))
###############################################################################

doc = nlp("Tesla is going to acquire Twitter for $45 billion")
for ent in doc.ents:
  print(ent.text, "|", ent.label_)

# Tesla | ORG
# Twitter | PRODUCT
# $45 billion | MONEY
###############################################################################
s = doc[2:5]
s
##########################################################

from spacy.tokens import Span
s1 = Span(doc, 0, 1, label="ORG")
s2 = Span(doc, 5, 6, label="ORG")

doc.set_ents([s1, s2], default="unmodified")

for ent in doc.ents:
    print(ent.text, "|", ent.label_)
#######################################################################
# Another method to find ner
# chunking (shallow parsing) Identifying named entities

nltk.download("maxent_ne_chunker")
nltk.download("words")
sentence4="We are Learning NLP in python by SanjivaniAI based in India"
## first we will tokenize
words=word_tokenize(sentence4)
words =nltk.pos_tag(words)
i=nltk.ne_chunk(words,binary=True)
[a for a in i if len(a)==1 ]

################################################

# sentence tokenization
from nltk.tokenize import sent_tokenize
sent = sent_tokenize("We are Leraning NLP in PYthon. Delivered by SAI. do you know where is located")
sent

# ['We are Leraning NLP in PYthon.',
#  'Delivered by SAI.',
#  'do you know where is located']

################################################
from nltk.wsd import lesk
sentence1 ="keep your savings in the bank"
print(lesk(word_tokenize(sentence1),"bank"))
# output =Synset('savings_bank.n.02')
srentence2="it is so risky to drive over the bank of river"
print(lesk(word_tokenize(sentence2),"bank"))
#Synset('trust.v.01')
##### 
# Synset('trust.v.01') a slope in the turn of a road or track
# the outside is higher thena inside
# bank has different meaning in order to find correct meaning execute the following code

from nltk.corpus import wordnet as wn
for ss in wn.synsets("bankl"): print(ss,ss.definition())




