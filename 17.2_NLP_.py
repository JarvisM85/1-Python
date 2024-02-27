#DATE ==> 17/08/2023


'''
#  Stemming :==>
------------------


Process of reducing inflected words in their word stem,
base or root form,
These mainly rely on chopping -off 's','es','ed','ing','ly' etc
from the end of the words.
and sometimes the conversion is not desirable.
But nonetheless ,stemming helps us in standardizing text. 
'''
#  Verb will converted into its BASE form

import nltk
def get_stem(text):
    stemmer = nltk.porter.PorterStemmer()
    text = ' '.join([stemmer.stem(word) for word in text.split()])
    return text
get_stem("We are eating and swimming; we have been eating and swimming ; he eats and swims ; he ate and swam ")
    
# 'ing','s' have changed to base form
# But 'ate' & 'swam' arenot changed to base form -> Disadantage
    
   
#Drawback ==>
'''
To avoid drawback 
#lemmatization is used
---------------
'''






