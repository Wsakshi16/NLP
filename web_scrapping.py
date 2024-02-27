# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 08:27:21 2023

@author: adity
"""

#                   WEB SCRAPING
#₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪

#pip install BeautifulSoup
#pip install bs4

from bs4 import BeautifulSoup
soup= BeautifulSoup(open("C:/1-python/NLP/sample_doc.html"),'html.parser')
print(soup)

# it will show you only text
soup.text

# it show to all contents
soup.contents

# show all html contents extracted
soup.find('address')
soup.find_all('address')
soup.find_all('q')
soup.find_all('b')
table=soup.find('table')
table

for row in table.find_all('tr'):
    columns= row.find_all('td')
    print(columns)
    
# it show all rows expect first row
#₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪

from bs4 import BeautifulSoup as bs     
import requests    

link= "https://sanjivanicoe.org.in/index.php/contact"    
page= requests.get(link)    
page    

page.content    

soup=bs(page.content,'html.parser')    
soup    

# text is clean but not upto the expectations for that used prettify method
print(soup.prettify())    

# the text id neat and clean
list(soup.children)    

# finding all content using tab
soup.find_all('p')    
#extract content fron 1st row
soup.find_all('p')[1].get_text()   
soup.find_all('p')[2].get_text()      
# finding text using class
soup.find_all('div',class_='table')