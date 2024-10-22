import sys
from random import randint
import numpy as np
np.random.seed(42)
from pickle import load
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import heapq

model = load_model('keras_model1.h5')
history = load(open('history1.pkl', 'rb'))
chars = ['\n',' ','!',"'",'(',')',',','-','.','0','1','2','3','4','5','6','7','8','9',':',';','?','_','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

SEQUENCE_LENGTH = 40
step = 3
sentences = []
next_chars = []

def prepare_input(text):
    x = np.zeros((1, SEQUENCE_LENGTH, len(chars)))
    for t, char in enumerate(text):
        x[0, t, char_indices[char]] = 1.
        
    return x

def sample(preds, top_n=3):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds)
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    
    return heapq.nlargest(top_n, range(len(preds)), preds.take)

def predict_completion(text):
    original_text = text
    generated = text
    completion = ''
    while True:
        x = prepare_input(text)
        preds = model.predict(x, verbose=0)[0]
        next_index = sample(preds, top_n=1)[0]
        next_char = indices_char[next_index]
        text = text[1:] + next_char
        completion += next_char
        
        if len(original_text + completion) + 2 > len(original_text) and next_char == ' ':
            return completion
        
def predict_completions(text, n=3):
    x = prepare_input(text)
    preds = model.predict(x, verbose=0)[0]
    next_indices = sample(preds, n)
    return [indices_char[idx] + predict_completion(text[1:] + indices_char[idx]) for idx in next_indices]


if(True):
    #seq = q[:40].lower()
    #seq = input("Enter: ") 
    seq = sys.argv[1]
    seq1 = seq[:40].lower()
    seq1 = seq1 + " "*(40 - len(seq))
    print(seq)
    result = predict_completions(seq1, 3)
    print(' '.join(result))