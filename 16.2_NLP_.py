#DATE ==> 17/08/2023

'''
#    pip install PyPDF2
    --------------------
'''

from PyPDF2 import PdfFileReader

#importing required modules
from PyPDF2 import PdfReader

#creating a pdf reader object
reader = PdfReader('c:/1-Python/python_tutorial.pdf')

#printing number of pages in pdf file
print(len(reader.pages))

#getting a specific page from the pdf file
page = reader.pages[10]

#extracting text from page
text = page.extract_text()
print(text)

#####################################

import re
chat2 = 'Hi: I have a problem with my order number 412889912'
pattern ='order[^\d]*(\d*)' 
matches = re.findall(pattern,chat2)
matches

import re
chat1 = 'Hi: Hello, I am having an issue with my order # 412889912'
pattern ='order[^\d]*(\d*)' 
matches = re.findall(pattern,chat1)
matches

############

chat3 = 'Hi: My order 412889912 is having an issue, I was charged 300$ when online'
pattern ='order[^\d]*(\d*)' 
matches = re.findall(pattern,chat3)
matches

#########################################################3

def get_pattern_match(pattern,text):
    matches = re.findall(pattern,text)
    if matches:
        return matches[0]
get_pattern_match('order[^\d]* (\d*)',chat1)

########################################################
# Retrive email id and phone
chat1 = 'Hi: you ask lot of questions 1235678912, abc@xyz.com'
chat2 = 'Hi: here it is: (123)-567-8912, abc@xyz.com'
chat3 = 'Hi: yes, phone: 1235678912 email:abc@xyz.com'

get_pattern_match('[a-zA-Z0-9]*@[a-z]*\.[a-zA-Z0-9]*',chat1)

get_pattern_match('[a-zA-Z0-9]*@[a-z]*\.[a-zA-Z0-9]*',chat2)

get_pattern_match('[a-zA-Z0-9]*@[a-z]*\.[a-zA-Z0-9]*',chat3)

