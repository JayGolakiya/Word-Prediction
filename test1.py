# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 13:58:25 2019

@author: chirag_vadodariya
"""
import sys
from random import randint
from pickle import load
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences

                                                # IMORTING THE 

#tmp=sys.argv[1]
'''dataset_clean = open('training_set_clean.txt' , encoding='ISO-8859-1')
text = dataset_clean.read()
dataset_clean.close()
t#ext=t
#text=training_set_clean
lines = [ln.split(" ") for ln in text]'''
text = [line.rstrip('\n') for line in open('training_set_clean.txt',encoding='ISO-8859-1')]
lines = [ln.split(" ") for ln in text]
seq_length = len(lines[0]) - 1
seq_length = len(lines[0]) - 1

                                            # LOAD THE MODEL AND TOKENIZER
model = load_model('regressor1.h5')
tokenizer = load(open('tokenizer1.pkl', 'rb'))

seed_text=" "
                                        # PREDICTING
while(True):
    seed_text= sys.argv[1]
    seed_text=seed_text.lower()
    if seed_text == 'exit':
        break;
    else:
        print(seed_text + '\n')
        result=list()
        in_text=seed_text
        for i in range(3): 
            encoded = tokenizer.texts_to_sequences([in_text])[0]
            encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
            yhat = model.predict_classes(encoded, verbose=0)
            out_word = ''
            for word, index in tokenizer.word_index.items():
                if index == yhat:
                    out_word = word
                        #break
            in_text += ' ' + out_word
            result.append(out_word)
	
#DISPLAY THE RESUL
    print(seed_text)
    print(' '.join(result))
    break