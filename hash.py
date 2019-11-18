# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 15:43:35 2019

@author: SaiLikhithK
"""

count=0
wordsList=[]
numWords=0
numChars=0
counter=0

with open('wordlist.txt','r') as file:  #wordlist file that you downloaded from internet
    for line in file:
        wordsList+=line.split()
        numWords+=len(wordsList)
        numChars+=len(line)
        count+=1
        
n=len(wordsList)
print("wordsList")
print(wordsList)
print("\n")

i=0
hashof_wordList=[]  #define the hash of the wordlist- this hashlist is what you create using strings you have
m=len(hashof_wordList)

for i in range(0,n):
    print(wordsList[i])
    c=hash(wordsList[i])
    hashof_wordList.append(c)
    
print("hashed wordsList")
print(hashof_wordList)            #check the hased list of your wordlist
print("\n")

count2=0
wordsList2=[]
with open('hashedwordlist.txt','r') as file:   #import the given hashedlist which contains only hashcodes
    for line in file:
        wordsList2+=line.split()
        count2+=1

print("wordsList2")
print(wordsList2)
print("\n")
print("No.of words in wordList2=")
print(count2)
print("\n")

hashed_wordList2=[]
m=len(wordsList2)
for i in range(0,m):
    print(wordsList2[i])
    hashed_wordList2.append(int(wordsList2[i]))
    
print("nwl2")
print(hashed_wordList2)         #append it to new string to remove the single quotes
print("\n")

counter2=0
matched=[]
for k in range(0,n) :
    for i in range(0,m):
        if(hashof_wordList[k]==hashed_wordList2[i]): #compare the given hashed list and hash of the wordlist you have
            counter2+=1
            matched.append(int(hashed_wordList2[i])) #write it into array of matched values

print("The List\n")
print(matched)
print("No.of matches\n")
print(counter2)

print(hashof_wordList)   #print the values of initial hash of wordlist you have from internet
print(hashed_wordList2)  #print the values from given hashed list
print(matched) #print the matched hashed values


    
