# DATE --> 28/07/2023

#1.Write a python script to add a key to a dictionary.
#sample Dictionary : {0: 10,1: 20}
#Expected output : {0: 10,1: 20,2: 30}
#1-->
d={0: 10,1: 20}
print(d)
d.update({2: 30})
print(d)

#2-->
d={0: 10,1: 20}
print(d)
d[2]=30
print(d)

#########################################
'''
#2. Write python script to concatenate the following 
#dictionaries
#sample :
    dic1={1:10,2:20}
    dic2={3:30,4:40}
    dic3={5:50,6:60}
# expected:{1:10,2:20,3:30,4:40,5:50,6:60}
'''
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={}
for d in (dic1,dic2,dic3):dic4.update(d)
print(dic4)

#########################################
'''
3. Write Python script to check whether a given key 
already exists in dictionary .
'''
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
    if x in d:
        print(f'{x} Key is present in the dictionary')
    else:
        print(f'{x} Key is NOT present in the dictionary')
is_key_present(5)
is_key_present(9)   

###################################################
'''
4. Write Python program to iterate over dictionaries
using for loops .
'''
d = {'x':10,'y':20,'z':30}
for dict_key,dict_value in d.items():
    print(dict_key,':',dict_value)
    
###################################################
'''
5. Write Python program to  .
'''
    
    
    