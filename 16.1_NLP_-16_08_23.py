#DATE ==> 16/08/2023

######        Python For NLP      #######
#          ====================         #

################################################
'''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
'''
import re
text = '''Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
          Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
       '''
pattern =r'\d\d\d\d\d\d\d\d\d\d'
matches = re.findall(pattern,text)
matches


text = '''Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
          Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
       '''
pattern =r'\d{10}'
matches = re.findall(pattern,text)
matches

#########3

import re
text1 = '''Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
'''
pattern =r'\(\d{3}\)-\d{3}-\d{4}'
matches = re.findall(pattern,text1)
matches



#ERROR-->
text1 = '''Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
'''
pattern =r'\(\d{3}\)-\d{3,4}'
matches = re.findall(pattern,text1)
matches

#For Both Indian and US number
text1 = '''Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
'''
pattern =r'\d{10}|\(\d{3}\)-\d{3}-\d{4}'
matches = re.findall(pattern,text1)
matches

#################################

'''
A protracted; legal battle; over a 32-carat;
 Golconda diamond-
'''
# to extraxt only text and escape all puntuation Marks
import re
text2 = "A protracted; legal battle; over a 32-carat;Golconda diamond-"
pattern =r'[^;-]'
matches = re.findall(pattern,text2)
matches

#####################
import re
text3 = "Note 1 - Summary of Significant Accounting Policies"
pattern =r'Note \d - [^\n]*'
matches = re.findall(pattern,text3)
matches




text3 = '''Note 1 - Summary of Significant Accounting Policies 
Unaudited Interim Financial Statements
The consolidated financial statements of Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”), including the consolidated balance sheet as of
June 30, 2023, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of
redeemable noncontrolling interests and equity for the three and six months ended June 30, 2023 and 2022, and the consolidated statements of cash
flows for the six months ended June 30, 2023 and 2022, as well as other information disclosed in the accompanying notes, are unaudited. The
consolidated balance sheet as of December 31, 2022 was derived from the audited consolidated financial statements as of that date. The interim
consolidated financial statements and the accompanying notes should be read in conjunction with the annual
'''
pattern =r'Note \d - [^\n]*'
matches = re.findall(pattern,text3)
matches

###################

pattern =r'Note \d - ([^\n]+)'
matches = re.findall(pattern,text3)
matches

##########################################
import re
text4 = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.'''

pattern = 'FY\d{4} Q\d'
matches = re.findall(pattern,text4) 
matches

pattern = 'FY\d{4} Q[1234]'

pattern = 'FY\d{4} Q[1-4]'

matches = re.findall(pattern,text4)
matches

#################################
text5 = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion.'''
#                      ---------
#1.But here only capital FY will print and not fy2020
pattern = 'FY\d{4} Q[1234]'
matches = re.findall(pattern,text5)
matches

#2.To solve above problem 1st option is use
#      of "IGNORECASE"
#       ----------------
pattern = 'FY\d{4} Q[1234]'
matches = re.findall(pattern,text5,re.IGNORECASE)
matches
#                    OR
#2.To solve above problem 2st option is use
#      of "OR condition"
#        ----------------
pattern1 = 'FY\d{4} Q[1-4] | fy\d{4} Q[1-4]'
matches = re.findall(pattern1,text5)
matches

#--------------------
#Now let us assume we want only 2021 Q1 and 2020 Q4, then you can get
# exact through(...)
pattern = 'FY(\d{4} Q[1234])'
matches = re.findall(pattern,text5,re.IGNORECASE)
matches


pattern = '\d{4} Q[1234]'
matches = re.findall(pattern,text5)
matches

#####################
import re
text6 = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion.
'''
#If we want dollar sign and value
# then for character give " \ " 1st then give char "$"

pattern = '\$[0-9\.]+'
matches = re.findall(pattern,text6)
matches 

# To remove the $ sign give parenthesis.
pattern = '\$([0-9\.]+)'
matches = re.findall(pattern,text6)
matches 

###########################################
######################################################





























