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

with open('Test.txt','r') as file:
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
new_wordList=[]
m=len(new_wordList)

for i in range(0,n):
    print(wordsList[i])
    c=hash(wordsList[i])
    new_wordList.append(c)
    
print("hashed wordsList")
print(new_wordList)
print("\n")

count2=0
wordsList2=[]
with open('Test2.txt','r') as file:
    for line in file:
        wordsList2+=line.split()
        count2+=1

print("wordsList2")
print(wordsList2)
print("\n")
print("No.of words in wordList2=")
print(count2)
print("\n")

new_wordList2=[]
m=len(wordsList2)
for i in range(0,m):
    print(wordsList2[i])
    new_wordList2.append(int(wordsList2[i]))
    
print("nwl2")
print(new_wordList2)
print("\n")

counter2=0
matched=[]
for k in range(0,n) :
    for i in range(0,m):
        if(new_wordList[k]==new_wordList2[i]):
            counter2+=1
            matched.append(int(new_wordList2[i]))

print("The List\n")
print(matched)
print("No.of matches\n")
print(counter2)

print(new_wordList)
print(new_wordList2)
print(matched)


    