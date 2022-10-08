#Function to read the file
def read_file(filename):
    file=open(filename,'r')
    print(file.read())
    print()
    file.close()


#Function to write in a file
#I have provided default mode as append but if user want to rewrite whole file he can use mode as 'w' or any.
def write_file(filename,text,mode='a'):
    file=open(filename,mode)
    file.write(text)
    file.close()


#Function to count how many time a word occured in text file
def count_word(filename,word):
    file=open(filename,'r')
    lines=file.readlines()  #This will store the lines in a list format

    n=len(lines)            #This will store how many total number of lines we have
    count=0
    for i in range(n):
        Words=lines[i].split()   #This will store the words in a list format for the i th indexed list of 'lines'
        for j in Words:
            if(j==word):        
                count+=1    #for each time the word given by user is found, count will be increased by 1 
    print('frequency of "',word,'" is-',count)
    print()
    file.close()

#example- for the file named simpletext.txt

write_file('simpletext.txt','\nhello my name is abc')

read_file('simpletext.txt')

count_word('simpletext.txt','and')


'''
output:

What is file handling in simple words
File Handling is the storing of data in a file using a program
The various operations which can be implemented on a file such as
read write open and close
there are several benefits of file handling
It helps in preserving the data or information
generated after running the program
Using files you need not worry about
the problem of storing data in bulk
we can use file handling with several types of files
hello my name is abc

frequency of " and " is- 1
'''
