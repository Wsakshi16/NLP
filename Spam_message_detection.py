# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 09:07:18 2023

@author: adity
"""

import pandas as pd
import numpy as np
#Read the csv
df = pd.read_csv("c:/0-datasets/spam.csv")
#check 1st 10 records
df.head()
#Total number of spam and ham
df.Category.value_counts()
#Create one more column comprises 0 and 1
#name of column is spam
df['spam'] = df['Category'].apply(lambda x: 1 if x=='spam' else 0)
df.shape
#######################################################################
#Train test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.Message, df.spam, test_size=0.2)
#Let us check the shape of X_train Data and X_test data
X_train.shape
X_test.shape
#Let us check the type of X_train and y_train
type(X_train)
type(y_train)
#########################################################################
#Create bag of words representation using CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer
v = CountVectorizer()
X_train_cv = v.fit_transform(X_train.values)
X_train_cv
#After creation of Bow, let us check the shape
X_train_cv.shape
###################################################################
#Train the naive bayes model
from sklearn.naive_bayes import MultinomialNB
#Initialize the model
model = MultinomialNB()
#Train the model
model.fit(X_train_cv, y_train)
##########################################################
#Create Bag of words representation usinf CountVectorizer
#of X_test
X_test_cv = v.transform(X_test)
#####################################################
#Evaluate Performance
from sklearn.metrics import classification_report
y_pred = model.predict(X_test_cv)
print(classification_report(y_test, y_pred))

############################################################################
#Bag of words model small
bag_of_word_model_small = CountVectorizer(max_features=5)
bag_of_word_model_small= pa.DataFrame(bag_of_word_model_small.fit_transform)

###############################################
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
corpus=['The mouse had a tiny little mouse','The cat saw the mouse','The cat catch the mouse','The end of mouse story']
#Step1 initialize count vector
cv=CountVectorizer()
#To count the total number of TF
word_count_vector = cv.fit_transform(corpus)
word_count_vector.shape
#Now next step is to apply IDF
tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
tfidf_transformer.fit(word_count_vector)
#This matrix is in raw matrix form, let us convert it in dataframe
df_idf=pd.DataFrame(tfidf_transformer.idf_,index=cv.get_feature_names_out(),columns=['idf_weights'])
#sort ascending
df_idf.sort_values(by=['idf_weights'])





