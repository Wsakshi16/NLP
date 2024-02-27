# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 15:21:42 2023

@author: adity
"""


import re 
sentence5="sharat twitted , Wittnessing 70th republic day india from Rajpath,\new dehli Memorizing performance for indian Army!"
re.sub(r"([^\s\w]|_)+"," ",sentence5).split()
## extracting n_grams
# n_grms can be extracted using three techniques
#1.custom defined function
#2.NLTK
#3.TextBlob
###########################################

# extracting n_grams using custom defind function
import re
def n_gram_extarctor(input_str,n):
    tokens=re.sub(r'([^\s\w]|_)+',' ',input_str).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])
        
n_gram_extarctor("the cute little boy is playing with kitten",2)
n_gram_extarctor("the cute little boy is playing with kitten",3)

###########################################

from nltk import ngrams
# extraction n_grams with nltk
list(ngrams("the cute little boy is playing with kitten".split(),2))
list(ngrams("the cute little boy is playing with kitten".split(),3))

###########################################

from textblob import TextBlob
blob=TextBlob("The cute little boy is playing with kitten.")
blob.ngrams(n=2)
blob.ngrams(n=3)

##########################################
#Tokenization using Keras,
sentence5
from keras.preprocessing.text import text_to_word_sequence
text_to_word_sequence(sentence5)
blob.words
##########################################################################################
#Tweet Tokenizer
from nltk.tokenize import TweetTokenizer
tweet_tokenizer=TweetTokenizer()
tweet_tokenizer.tokenize(sentence5)
#############################################################
#Multi-Word_Expression
from nltk.tokenize import MWETokenizer
sentence5 
mwe_tokenizer=MWETokenizer([('republic','day')])
mwe_tokenizer.tokenize(sentence5.split())
mwe_tokenizer.tokenize(sentence5.replace('/',' ').split())
########################################################
#Regular Expression Tokenizer
from nltk.tokenize import RegexpTokenizer
reg_tokenizer=RegexpTokenizer('\w+/\$[\d\.]+|\s+')
reg_tokenizer.tokenize(sentence5)
#########################################
#White space Tokenizer
from nltk.tokenize import WhitespaceTokenizer
wh_tokenizer=WhitespaceTokenizer()
wh_tokenizer.tokenize(sentence5)
##########################################################
from nltk.tokenize import WordPunctTokenizer
wp_tokenizer=WordPunctTokenizer()
wp_tokenizer.tokenize(sentence5)
#####################################################################
sentence6="I love playing criket.Cricket players practices hard in their inning"
from nltk.stem import RegexpStemmer
regex_stemmer=RegexpStemmer('ing$')
' '.join(regex_stemmer.stem(wd) for wd in sentence6.split())
#it removes '-ing' and '-ed'
######################################################################
sentence7="Before eating .it would be nice to sanitize your hands with a sanitizer"
from nltk.stem.porter import PorterStemmer
ps_stemmer=PorterStemmer()
words=sentence7.split()
" ".join([ps_stemmer.stem(wd) for wd in words])
#####################################################################
#Lemmatization
import nltk
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
nltk.download('wordnet')
lemmatizer=WordNetLemmatizer()
sentence8="The codes executed today are for better than what we execute generally"
words=word_tokenize(sentence8)
" ".join([lemmatizer.lemmatize(word) for word in words])
#########################################################################
#singularize and Pluralization
from textblob import TextBlob
sentence9=TextBlob("She sells seashells on the seashore")
words=sentence9.words
#We want to make word[2] i.e. swashells in singular form
sentence9.words[2].singularize()
#We want to make word[5] i.e seashore in plural form
sentence9.words[5].pluralize()
################################################
#Language tranlzation from spanish to English
from  textblob import TextBlob
en_blob=TextBlob(u'muy bien')
en_blob.translate(from_lang='es', to='en')
#es:spanish en:English
###########################################################
##custom stopwords removal
from nltk import word_tokenize
sentence9="She sells seashells on the seashore"
custom_stop_word_list = ['she','on','the','am','is']
words=word_tokenize(sentence9)
" ".join([word for word in words if word.lower() not in custom_stop_word_list])
#select words which are not in defined list
####################################################################
#extracting general features from raw text
#number of words
#detect presense of wh word
#polarity
#subjectivity
#language identification
############################################
#To identify the number of words
import pandas as pd
df = pd.DataFrame([['The vaccine for covid-19 will be announced on 1st August'],['Do you know how much expectation the world population is having from this research'],['The risk of virus will come to an end on 31st July']])
df.columns=['text']
df
#Now let us measure the number of words
from textblob import TextBlob 
df['number_of_words']=df['text'].apply(lambda x:len(TextBlob(x).words))
df['number_of_words']
###################################################################
#Detect presence of words
wh_words=set(['why','who','which','who','where','when','how'])
df['is_wh_words_present']=df['text'].apply(lambda x:True if len(set(TextBlob(str(x)).words).intersection(wh_words))>0 else False)
df['is_wh_words_present']
###################################################################
#Polarity  of the sentence 
df['polarity']=df['text'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']
sentence10="I like this example very much"
pol=TextBlob(sentence10).sentiment.polarity
pol
sentence10="This is fantastic example and I like it very much"
pol=TextBlob(sentence10).sentiment.polarity
pol
sentence10="This was helpful example but I would have prefer another one "
pol=TextBlob(sentence10).sentiment.polarityxd
pol
sentence10="This is my personal opinion that it was helpful example but I would prefer another one"
pol=TextBlob(sentence10).sentiment.polarity
pol

sentence10="This is very bad example"
pol=TextBlob(sentence10).sentiment.polarity
pol
##################################################################################
#Subjectivity of the dataframe df and check whether there ispersonal opinion
df['subjectivity']=df['text'].apply(lambda x:TextBlob(str(x)).sentiment.subjectivity)
df['subjectivity']
#############################################
#To find language of the snetence, this part of code will get http error
df['language']=df['text'].apply(lambda x:TextBlob(str(x)).detect_language())
##################################################################
#################################################
## bag of words

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
corpus=["At least seven indian pharma companies are working to develop vaccine against the coronna virus.",'The deadly virus that has already infected more than 14 million globally.','Bharat biotech is the among the domestic pharma firm working on the corona virus vaccine in india']
bag_of_word_model=CountVectorizer()
print(bag_of_word_model.fit_transform(corpus).todense())
bag_of_word_df=pd.DataFrame(bag_of_word_model.fit_transform(corpus).todense())
# this will create df

bag_of_word_df.columns=sorted(bag_of_word_model.vocabulary_)
bag_of_word_df.head()

################################################

# bag of words model small

bag_of_word_model_small=CountVectorizer(max_features=5)
bag_of_word_small_df=pd.DataFrame(bag_of_word_model_small.fit_transform(corpus).todense())
# this will create df

bag_of_word_small_df.columns=sorted(bag_of_word_model_small.vocabulary_)
bag_of_word_small_df.head()




