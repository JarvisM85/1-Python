#DATE ==> 17/08/2023


import re

def get_pattern_match(pattern,text):
    matches = re.findall(pattern,text)
    if matches:
        return matches[0]

#Elon Musk
text = '''Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner and CTO of Twitter
President of the Musk Foundation
Founder of the Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
'''

get_pattern_match(r'age (\d+)', text)
get_pattern_match(r'Born(.*)\n', text).strip()
get_pattern_match(r'Born.*\n(.*)\(age', text).strip()
get_pattern_match(r'\(age.*\n(.*)', text)


############################################
def extract_personal_information(text):
    age = get_pattern_match(r'age (\d+)', text)
    full_name = get_pattern_match(r'Born(.*)\n', text)
    birth_date = get_pattern_match(r'Born.*\n(.*)\(age', text)
    birth_place = get_pattern_match(r'\(age.*\n(.*)', text)
    return {
        'age': int(age),
        'name': full_name.strip(),
        'birth_date': birth_date.strip(),
        'birth_place': birth_place.strip()
        }
extract_personal_information(text)



import pandas as pd
row = ['r1']
df = pd.DataFrame(extract_personal_information(text),index=row)

##############################################
import re

def get_pattern_match(pattern,text):
    matches = re.findall(pattern,text)
    if matches:
        return matches[0]


#Ambani

text1 = '''Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 66)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Occupation(s)	Chairman and MD, Reliance Industries
Spouse	Nita Ambani ​(m. 1985)​[3]
Children	3
Parents	
Dhirubhai Ambani (father)
Kokilaben Ambani (mother)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)'''


get_pattern_match(r'age (\d+)', text1)
get_pattern_match(r'Born(.*)\n', text1).strip()
get_pattern_match(r'Born.*\n(.*)\(age', text1).strip()
get_pattern_match(r'\(age.*\n(.*)', text1)



def extract_personal_information(text1):
    age = get_pattern_match(r'age (\d+)', text1)
    full_name = get_pattern_match(r'Born(.*)\n', text1)
    birth_date = get_pattern_match(r'Born.*\n(.*)\(age', text1)
    birth_place = get_pattern_match(r'\(age.*\n(.*)', text1)
    return {
        'age': int(age),
        'name': full_name.strip(),
        'birth_date': birth_date.strip(),
        'birth_place': birth_place.strip()
        }
extract_personal_information(text1)


import pandas as pd
row1 = ['x1']
df1 = pd.DataFrame(extract_personal_information(text1),index=row1)



##########################################################
'''
 #  Tokenization
  =================
'''
txt = 'welcome to the new year 2024'
x = txt.split()
print(x)

"""
 # Removing Special Characters :=>
 ---------------------------------
 
"""
import re
def remove_special_characters(text):
    #define the pattern to keep
    pat = r'[^a-zA-Z0-9.,!?/:;\"\'\s]'
    return re.sub(pat, '',text)

# Call function
remove_special_characters("007 Not sure@ if this % was #fun! 558923 What do# you think** of it.? $500USD!")

###################################################
'''
#Removing Numbers :=>
------------------
'''
import re
def remove_numbers(text):
    #define the pattern to keep
    # from pat remove 0-9
    pat = r'[^a-zA-Z.,!?/:;\"\'\s]'
    return re.sub(pat, '',text)

# Call function
remove_numbers("007 Not sure@ if this % was #fun! 558923 What do# you think** of it.? $500USD!")



txt = 'welcome: to the, new year; 2024!'
import re
x = re.split(r'(?:,|;|\s)\s*',txt)
print(x)

#################################################

'''
# Removing Punctuations :==>
--------------------------
'''
# "string.puntuations" is used

import string
def remove_punctuation(text):
    text = ''.join([c for c in text if c not in string.punctuation])
    return text  #call function
remove_punctuation('Article: @First sentence of some, {important} article having lot of ~ punctuations. And another one;!')


###############################################