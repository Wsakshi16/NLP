# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 09:12:06 2023

@author: adity
"""

from sklearn.feature_extraction.text import TfidfVectorizer

corpus = ['Thor eating pizza, Loki is eating pizza, Ironman ate pizza already',
          'Apple is announcing new iphone tommorow',
          'Tesla is announcing new model-3 tomorrow',
          'Google is announcing new pixe-6 tomorrow',
          'Microsoft is announcing new surface tomorrow',
          'Amazon is announcing new eco-dot tomorrow',
          'I am eating biryani and you re eating grapes']
#let's create the vectorizer and fit the corpus and transform them accordingly
v = TfidfVectorizer()
v.fit(corpus)
transform_output = v.transform(corpus)
#Let's print the vecabulary

print(v.vocabulary_)
#Let's print the idf of each word

all_feature_names = v.get_feature_names_out()

for word in all_feature_names:
    
    #Let's get the index in the vocabulary
    indx = v.vocabulary_.get(word)
    #get the score
    idf_score = v.idf_[indx]
    print(f"{word} : {idf_score}")
    
##############################################################################
import pandas as pd

#Read the data into pandas dataframe
df = pd.read_csv("c:/0-datasets/Ecommerce_data.csv")
print(df.shape)
df.head(5)
#Check the distribution of labels
df['label'].value_counts()
#Add a new column which gives a unique number to each of these label

df['label_num'] = df['label'].map({
    'Household': 0,
    'Books': 1,
    'Electronics': 2,
    'Clothing & Accessories':3
    })

#checking the results
df.head(5)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    df.Text,
    df.label_num,
    test_size=0.2, #20% samples will go to test dataset
    random_state=2022,
    stratify = df.label_num
    )
print("Shape of X_train:", X_train.shape)
print("Shape of X_test:", X_test.shape)
y_train.value_counts()
y_test.value_counts()
############################################################################
#Apply to classifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
#1. create a pipeline object
clf = Pipeline([
    ('vectorizer_tfidf', TfidfVectorizer()),
     ('KNN', KNeighborsClassifier())])

#2. fit the X_train and y_train
clf.fit(X_train, y_train)

#3. get the predictions for X_test and store it in y_pred
y_pred= clf.predict(X_test) 










