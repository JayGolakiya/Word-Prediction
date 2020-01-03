# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 02:56:39 2019

@author: chirag_vadodariya
"""
#%%
# IMPORTING THE TEXT FOR TRAINING OF THE MODEL
import string
import pickle
from keras.preprocessing.text import Tokenizer
dataset_train = open('try_text.txt' , encoding='ANSI')
text = dataset_train.read()
dataset_train.close()

# PRE-PROCESSING THE DATA IMPORTED(CLEANING)
text = text.replace('--',' ')
text = text.replace('??',' ')
text = text.replace('?',' ')
text = text.replace('_',' ')
text = text.replace('*',' ')
tokens = text.split()
table = str.maketrans('', '', string.punctuation)
tokens = [w.translate(table) for w in tokens]
tokens = [word for word in tokens if word.isalpha()]
tokens = [word.lower() for word in tokens]
#print(tokens)

length = 50 + 1
training_set_clean = list()
t=list()
for i in range(length, len(tokens)):
    seq = tokens[i-length:i]
    line = ' '.join(seq)
    training_set_clean.append(line)
    t.append(line)
#print(len(t))
with open('training_set_clean.txt', 'w') as f:
    for item in t:
        f.write("%s\n" % item)
        

'''with open('training_set_clean.txt', 'wb') as fp:
   pickle.dump(training_set_clean, fp)
'''
#IMPORTING THE TEXT FOR TRAINING OF THE MODEL
dataset_clean = open('training_set_clean.txt' , encoding='ISO-8859-1')

training_set = dataset_clean.read()
dataset_clean.close()

# PRE_PROCESSING THE CLEAN DATASET
#lines = training_set.split('\n')
lines=[l.split('\n') for l in training_set_clean]

#import Tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_sequences(training_set_clean)
tokenizer.fit_on_texts(training_set_clean)
sequences = tokenizer.texts_to_sequences(training_set_clean)


vocab_size = len(tokenizer.word_index) + 1
#print('word_index : ',tokenizer.word_index)
#print(sequences[0])
#print("vocab_size:" + str(vocab_size) )


#%%