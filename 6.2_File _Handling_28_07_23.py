# DATE --> 28/07/2023

# File Handling
#------------------------------------------
# what is file ?
#-->block of bytes

with open('pi_digits.txt') as file_object:
    #The open() function needs 
    #one argument: the name of file you want to open
    contents = file_object.read()
print(contents)
#Observe the extra line at the end --> output
######
#to avoid this  rstrip() method is used--> remove all white spaces
with open('pi_digits.txt') as file_object:
    #The open() function needs 
    #one argument: the name of file you want to open
    contents = file_object.read()
print(contents.rstrip())

############################
file_path = 'c:/1-python/pi_digits.txt'
with open('pi_digits.txt') as file_object:
    
    contents = file_object.read()
print(contents.rstrip())

##############################
# reading line by line
filename = 'pi_digits.txt'
#we assign the name of file we're reading from to the variable
with open(filename) as file_object:
    #We again use the with syntax to
    # let python open and close the file properly
    for line in file_object:
        print(line)
        
##This blank lines appear because an invisible newline character
#is at the end of each line in the text file.
#using rstrip() in the each line in the print() call eliminates
#these extra blank lines occured in output
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
        
##############################################
#Working with a File's into memory
#after you have read file into memory
#you can do whatever you want with that data
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.rstrip()
        print(pi_string)
        print(len(pi_string))
        
##############################################
#One of the simplest way to save data is to write it to a file
#When you write text to a file, the o/p will still be available
#after you close the terminal containing your program's output
filename = 'programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love Programming.")
##############################################
#Writing multiple lines
# the write() function doesn't add any new line
# to the text yo write. so if
#you write 
#
#

filename = 'programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love Programming.")
    file_object.write("I love creating new games.")

##############################################
#Including horizontal data

filename = 'programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love Programming.\n")
    file_object.write("I love creating new games.\n")

##############################################
#APPENDING a file --> no old data is lost(erased) , new data is added to the same
# while in WRITE --> all old data is lost and totally new data is added

filename = 'programming.txt'
with open(filename,'a') as file_object:
#We use the 'a' argument to open the file for appending
#rather than writing over the existing file
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in s browser.\n")
    
    

































