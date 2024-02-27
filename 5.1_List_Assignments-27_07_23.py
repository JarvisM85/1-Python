#DATE ==> 27/07/2023

#########################################################
#1.write py program to add all the items in the list
def sum_list(num):
    sum=0
    for i in num:
        sum=sum + i
    return sum
lst=[1,2,3,4,5]
print(sum_list(lst))
# or we can write directly >> print(sum_list([1,2,3,4,5]))

#########################
#2.Write a py program to multiply all the items in the list
def mul_num(num):
    tot=1
    for i in num:
        tot=tot*i
    return tot
lst2=[1,2,3,4,5]
print(mul_num(lst2))

################
#3.Write py program to get largest number from the list.
lst3=[12,42,53,15,49]
print(max(lst3))



def max_value(values):
    max = values[0]
    for i in values:
        if i > max:
            max = i
    return max     
lst3=[12,42,53,15,49]
print(max_value(lst3))

#######################################3
#4. for minimun number
lst3=[12,42,53,15,49]
print(min(lst3))

def min_value(values):
    min = values[0]
    for i in values:
        if i < min:
            min = i
    return min     
lst3=[12,42,53,15,49]
print(min_value(lst3))

#
#######################################3
#5. code to count the number of strings which satisfies
#the condition that the string length is 2 or more and the 1st and last 
#character are the same from the given list of strings.
def match_word(words):
    count=0
    for i in words:
        if len(i)>=2 and i[0]==i[-1]:
            count+=1
    return count
lst5=['abc','xyz','aba','1221']
print(match_word(lst5))

########################
#6. code to get a list,sorted in incresing order by the last element in each
#tuple from a given list of non-empty tuples
sam_list=[(2,5),(1,2),(4,4),(2,3),(2,1)]
#expected=[(2,1),(1,2),(2,3),(4,4),(2,5)] list1.sort()

def sort_tup(sorted_tup):
    soted=[]
    for i in sorted_tup:
        if i[1]< i+1[1]:
            soted.append(i[1])
        else:
            soted.append(i+1[1])
            
    return soted       
sam_list=[(2,5),(1,2),(4,4),(2,3),(2,1)]
print(sort_tup(sam_list))

#####
lst1=[(2,5),(1,2),(4,4),(2,3),(2,1)]
def last(n):
    return n[-1]
def sort_list(tuples):
    result=sorted(tuples,key=last)
    return result
print(sort_list(lst1))

######
#7.write a code  to remove duplicates from a list
a=[10,20,30,20,10,50,60,40,80,50,40]
dup_items=set()
uniq_items=[]
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)  
print(dup_items)



lst4=[10,20,30,20,10,50,60,40,80,50,40]
unique=[]
duplicate=[]
for i in lst4:
    if i not in unique:
        unique.append(i)
    elif i not in duplicate:
        duplicate.append(i)  
print(unique)



a=[10,20,30,20,10,50,60,40,80,50,40]
b=set(a)
print(b)
b=list(b)
print(b)

lst1=[10,20,30,20,10,50,60,40,80,50,40]
st1=set(lst1)
print(st1)
lst2=list(st1)
print(lst2)

##################
#8. code to clone or copy a list
lst8=[10,20,30,20,10,50,60,40,80,50,40]
new=list(lst8)
print(new)

lst8=[10,20,30,20,10,50,60,40,80,50,40]
new=[]
print(new)
new.extend(lst8)
print(new)

###########################
#9. code to find the list of words that are longer than 
#than 3 or n(any) from given list of words.
def long_words(n,str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len
print(long_words(3,"The quick brown fox jumps over the lazy dog"))
    

###########################
#10. write a python function that takes two lists and returns
# True if they hava at least one comman member
def common_data(list1,list2):
    result = False
    for x in list1:
        for y in list2:
            if x==y:
                result = True
    return result
print(common_data([1,2,3,4,5],[5,6,7,8,9]))
print(common_data([1,2,3,4,5],[6,7,8,9]))

###################################
#11. code to calculate difference between two lists
## unique elements difference and concatenate
list1=[1,3,5,7,9]
list2=[1,2,4,6,7,8]
diff1=list(set(list1)-set(list2))
diff2=list(set(list2)-set(list1))
print(diff1)
print(diff2)
total_diff = diff1 + diff2
print(total_diff)

##################################
#12. Write a python program to convert a list of characters 
# into a string ###IMP
s = ['a','b','c','d']
str1 = ''.join(s)
print(str1)

#########################
#13.Write a python program to find the index of an item in 
# a specified list
num= [10,30,4,-6]
print(num.index(30))

#########################################
#14.  Write a python program to append a list to second list
list1=[1,2,3,0]
list2=['Red','Green','Black']
final_list = list1 + list2
print(final_list)




