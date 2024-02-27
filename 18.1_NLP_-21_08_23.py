#DATE ==> 21/08/2023
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
import re 
line='asdf fjdk; afed, fjek,asdf,foo'
re.split(r'(?:,|;|\s)\s*',line)

#---------------------------------
pattern=r'(?:,|;|\s)\s*'
x=re.split(pattern,text)
print(x)

#-----------------------------------------------
#Matching text at the start or end of string
filename='spam.txt'
filename.endswith('.txt')
#---------------------------------
area_name='6 th lanr west Andheri'
area_name.endswith('west Andheri')
#-----------------------------------
choises=('http:','ftp:')
url='http://www.python.org'
url.startswith(choises)
#------------------------------------------
#Slicing of string
S='ABCDEFGHI'
print(S[2:7])

#Positive indexing and negative indexing

S='ABCDEFGHI'
print(S[2:-5])

S='ABCDEFGHI'
print(S[2:7:2])

print(S[4:1:2])

#slice last 3 character 
print(S[3:])
print(S[:3])

#----------------------------------
#similar oprations can be one with slices
filename='spam.txt'
filename[-4:]=='.txt'

#----------------------------------------
url='http://www.python.org'
url[:5]=='http:' or url[:6]=='https:' or url[:4]=='ftp:'
#---------------------------------------------------
from fnmatch import fnmatch,fnmatchcase
names=['Dat.csv','Dat.csv','config.int','foo.py']
[name for name in names if fnmatch(name,'Dat*.csv')]

#-----------------------------------------------------
   # IMPORTANT 
from fnmatch import fnmatch,fnmatchcase
names = ['Andheri east','parle east','dadar west']
[name for name in names if fnmatch(name,'* east')]

addresses=[
'5412 N CLARK ST',
'1060 W ADISON ST',
'1039 W GRANVILLE AVE',
'2122 N CLARK ST',
'4802 N BROADWAT',
]

#list comprehention
from fnmatch import fnmatchcase
[addr for addr in addresses if fnmatch(addr,'* ST')]

#####################3

text = 'yeah, but no, but yeah, but no, but yeah'
#Exact match
text == 'yeah'
# False
# Match start or end
text.startswith('yeah')
text.startswith('no')
#True
text.endswith('yeah')
text.endswith('no')
#False

#--------------------

# Search for the location of the first occurance
text.find('no')
#10


########################################
text1 = '11/27/2012'
text2 = 'Nov 27,2012'

import re
#Simple matching : \d+ means match one or more digits

if re.match(r'\d+/\d+/\d+',text1):
    print('yes')
else:
    print('no')
# yes

if re.match(r'\d+/\d+/\d+',text2):
    print('yes')
else:
    print('no')
#no

if re.match(r'[A-Za-z]+ \d+,\d+',text2):
    print('yes')
else:
    print('no')
#yes

####################################################
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')


if re.match(datepat,text1):
    print('yes')
else:
    print('no')
#yes

if re.match(datepat,text2):
    print('yes')
else:
    print('no')
#no

datepat2 = re.compile(r'([A-Za-z]+) (\d+),(\d+)')

if re.match(datepat2,text2):
    print('yes')
else:
    print('no')
#yes

######################################################3

# Searching and replacing text
text = 'yeah, but no, but yeah, but no, but yeah'
text.replace('yeah','yep')

##################################################



#if ypu have dates in format 11/27/2012 to convert 2012-11-27
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text) 
#\3 3 rd group, \1 st group
#--> 'Today is 2012-11-27. PyCon starts 2013-3-13.'

##############################################
#if you want to know how many substtutions are made in text then
# you can use subn() method
newtext,n = datepat.subn(r'\3-\1-\2',text)
newtext
n

#################################################

text = 'UPPER PYTHON, lower python, Mixed Python'
re.findall('python',text,flags=re.IGNORECASE)
# to substitute
re.sub('python','snake',text,flags = re.IGNORECASE)
#'UPPER snake, lower snake, Mixed snake'

############

''' The last example reveals a limitation that
replacing text won't match the case of the
matched text. If you need to fix this
you might have to use a support function,as in the following.
'''
import re
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
text3 = re.sub('python',matchcase('snake'),text,flags=re.IGNORECASE)
text3

#######################@@@@@@@@@@@@@@@@@@@@@@@@@@
'''
You're trying to match a text pattern using regular expression
but it is identifying the
longest possible matches of a pattern.
instead you like to change it to find the 
shortest possible match.
This problem often arises in pattern
that try to match text enclosed inside a pair of
starting and ending delimiters (eg: a quoted string)
# To illustrate ,consider this example
'''
#
str_pat = re.compile(r'\"(.*)"')
text1 = 'Computer says "no."'
str_pat.findall(text1)
#['no.']    
    
#However if we have text as below
text2= 'Computer says "no."Phone says "yes."'
str_pat.findall(text2)
#['no."Phone says "yes.']
   
    
#
str_pat = re.compile(r'\"(.*?)\"')
str_pat.findall(text2)    

####################################
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
comment.findall(text1)
#[' this is a comment ']
text2 = '''/* this is a 
            multiline comment */
            '''
comment.findall(text2)     
# --> It will give error => as it is multiline comment

comment = re.compile(r'/\*((?:.|\n)*?)\*/')      
comment.findall(text2)


comment = re.compile(r'/\*(.*?)\*/',re.DOTALL)
comment.findall(text2)
    
##################################################
#################################################
'''
#Normalizing with Unicode Text to standard representation
you will working with Unicode Strings, but need to make sure 
that all of the strings have 
the same underlying representation.
'''
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
s1==s2
#False


######################
'''
installation -->   pip install unicodedata
'''

import unicodedata
t1 = unicodedata.normalize('NFC',s1)
t2 = unicodedata.normalize('NFC',s2)
t1 == t2
#True




    
    
    
    
    
    
    
    
    
    