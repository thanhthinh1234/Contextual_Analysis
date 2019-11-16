"""
Author: Thinh Mai
Date: 10/15/2019
Purpose: Contextual_Analysis

"""
#load os package
import os


punctuation = ['?','.', ';', '!',':',',']
dict = {}
i = 0

file_name = input('Enter the file name:')

file = open(file_name)
f =file.read()

#Remove punctuation marks from the words
for char in punctuation:
    f = f.replace(char,"")
word_list = f.lower().split()

#Create a dictionary where the key is each word and the value is a list of the word position
for i,word in enumerate(word_list):
    i +=1
    dict[word] = dict.get(word,[])
    dict[word].append(i)

#Print the unique words along with the corresponding word positions (alphabetically)
print('Words and the corresponding positions in File {}'.format(file_name)+" "+'are'+":")
for key in sorted(dict):
    print(key,":",dict[key])


