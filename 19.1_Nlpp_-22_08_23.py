#DATE==> 22/08/2023


# Unicode => a number which represents a charater.
# utf => unicode Transformation format



string1 = "apple"
string2 = "jeei125"
string3 = "12345"
string4 = "pre@12"

string1.encode(encoding = 'UTF-8',errors = 'strict')
string2.encode(encoding = 'UTF-8',errors = 'strict')
string3.encode(encoding = 'UTF-8',errors = 'strict')
string4.encode(encoding = 'UTF-8',errors = 'strict')

text = "one 🐘 and three 🐬"
print(text)
print(len(text))

'''
We encode the string into a byte type using the
utf-8 encoding and print the bytes.
We count the number of bytes in this encoding type.
'''

e = text.encode('utf8')
print(e)
print(len(e))

##########################
fname = 'data.txt'

with open(fname,mode='rb') as f:
    contents = f.read()
    
    print(type(contents))
    print(contents)
    print(contents.decode('utf8'))

###########################################
text
f = text.encode("utf16")
print(f)
print(len(f))
print(f.decode('utf16'))
###############################

#Normalization==>






###############################

#Striping ==> Strippig unwanted character from strings
#(for removing white space)

#  strip() method is used
#  lstrip() --> removes left side white space
#  rstrip() --> removes right side white space

#Whitespace Stripping
s = '  hello world  \n'
s
s.strip()
#
s = '  hello world  \n'
s.lstrip()
#
s = '  hello world  \n'
s.rstrip()

#####
# Character Stripping
t = '----hello====='
t.lstrip('-')

t = '----hello====='
t.rstrip('=')

t = '----hello====='
t.strip('-=')


s = ' hello world    \n'
s = s.strip()
s

s.replace(' ','')

import re
re.sub('\s+','',s)



###############################################3
#Aligning the text string
text = "Hello World"
text.ljust(20)

text.rjust(20)

text.center(20)

###################################
# All of these methods accept an optinal
text.rjust(20,'=')

text.ljust(20,'+')

text.center(20,'*')

#######################################
format(text,'>20')

format(text,'<20')

format(text,'^20')

###Here you can add characters to fill the space at left,right,center
#as above But if you want to include a fill character other
#character. 
format(text,'=>20s')

format(text,'*^20s')


# These format codes can also be used in the format()
#method will values.
# For example=>
'{:>10s} {:>10s}'.format("Hello","World")


# format() benifit that it is not specific to string
x = 1.2345
format(x,'>10')
x

format(x,'^10.2f')

##########################################

parts = ['Is','Chicago','Not','Chicago?']
' '.join(parts)

', '.join(parts)

''.join(parts)

#####################################


















