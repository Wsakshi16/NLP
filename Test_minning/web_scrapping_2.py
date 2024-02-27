# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 08:36:53 2023

@author: aditya
"""

from bs4 import BeautifulSoup as bs
import requests
link = 'https://www.flipkart.com/zebronics-zeb-pixaplay-18-3800-lm-remote-controller-portable-dolby-audio-e-focus-1080p-dual-band-wifi-wireless-screen-mirroring-bluetooth-5-1-app-download-android-smart-projector/product-reviews/itm9c5698bd20f7d?pid=PROGMY7YW5GEJFUD&lid=LSTPROGMY7YW5GEJFUDKN1M0F&marketplace=FLIPKART'
page = requests.get(link)
page
page.content
soup=bs(page.content,'html.parser')
print(soup.prettify())
title=soup.find_all('p', class_="_2-N8zT")
title
review_title=[]
for i in range(0,len(title)):
    review_title.append(title[i].get_text())
review_title
len(review_title)
#we got 10 review titles
###########################################
rating = soup.find_all('div',class_='_3LWZlK _1BLPMq')
rating
rate=[]
for i in range(0,len(rating)):
    rate.append(rating[i].get_text())
rate
len(rate)
rate.remove('4')
rate.remove('5',inplace=True)
rate.append('')
rate.append('')
rate.append('')
len(rate)
#############################################################
review = soup.find_all('div',class_='t-ZTKy')
review
review_body=[]
for i in range(len(review)):
    review_body.append(review[i].get_text())    
review_body
len(review_body)

import pandas as pd
df = pd.DataFrame()

df['Title'] = review_title
df['Rating'] = rating
df['Review'] = review_body

df.head()

df.to_csv('e:/datasets/flipkart_reviews.csv')

df['Review']=review_body
df
##########################################
#To create  .csv file
df.to_csv("c:/5-NLP/Text-minning/flipkart_reviews.csv",index=True)
######################################################
#sentiment analysis
import pandas as pd
from textblob import TextBlob
sent="This is very excellent garden"
pol=TextBlob(sent).sentiment.polarity
pol
df=pd.read_csv("c:/5-NLP/Text-minning/flipkart_reviews.csv")
df.head()
df['polarity']=df['Review'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df[polarity]
