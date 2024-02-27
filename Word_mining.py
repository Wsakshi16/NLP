# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 16:25:49 2023

@author: adity
"""

#####################Text Mining#########################
sentence="we are learning TextMining from Sanjivani AI"
###If we want to know position of learning
sentence.index('learning') #It will show the position of character
#It will show learning is at position 7
#This is going to show character position from 0 including
#############################################################
#we want to know position TextMining word
sentence.split().index("TextMining") #it will show Position of words
#It will split the words in list and count the position
#If you want to see the list select sentence.split() and
#It will show at 3
############################################################
#Suppose we want to print any word in reverse order
sentence.split()[2][::-1]
#[start:end end:-1(start)] will start from -1,-2,-3 till the end
#learning will be printed as gninrael
##########################################################
#Suppose we want to print 1st and last word of tghe sentence
words=sentence.split()
first_word=words[0]
first_word
last_word=words[-1]
last_word
#Now we want to concate the first and last word
concat_word=first_word+" "+last_word
concat_word
######################################################################
#We want to print even words from the sentence
[words[i] for i in range(len(words)) if i%2==0]
####################################################
sentence
#now we want to display only AI
sentence[-3:]
##########################################
#If we want to display entire sentence  in reverse order
sentence[::-1]
#IA inavijnaS morf gniniMtxeT gninrael era ew
##############################################################
#Suppose we want to select eact word and print in reversed order
words
print( " ".join(word[::-1]for word in words))
#ew era gninrael gniniMtxeT morf inavijnaS IA
#############################################################
#tokenization
import nltk
nltk.download("punkt")
from nltk import word_tokenize
words=word_tokenize("I am reading NLP Fundamentals")
print(words)
##############################################












