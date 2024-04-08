# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 18:32:39 2022

@author: natha
"""

file = open("questsource.txt","r")
count = 1
newfile = []
for line in file:
    line = line[0:(len(line)-1)]
    if count % 3 !=0:
        newfile.append(line)
    count +=1
file.close()
file=newfile
newfile = []
question = []
count = 1
for line in file:
    if count % 2 == 0:
        question.append(line)
        newfile.append(question)
        question = []
    else:
        question.append(line)
    count+=1
print(newfile)
        
    