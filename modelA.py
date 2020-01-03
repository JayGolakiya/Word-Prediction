from numpy import array
import pickle  
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Embedding
from keras import optimizers
import string
from keras.layers import Dropout
#PRE_PROCESSING THE CLEAN DATASET
#lines = training_set.split('\n')
training_set_clean = [line.rstrip('\n') for line in open('training_set_clean.txt',encoding='ISO-8859-1')]
#lines=[l.split('\n') for l in training_set_clean]
#import Tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_sequences(training_set_clean)
tokenizer.fit_on_texts(training_set_clean)
sequences = tokenizer.texts_to_sequences(training_set_clean)

vocab_size = len(tokenizer.word_index) + 1

sequences = array(sequences)
X_train = sequences[:, :-1]
y_train = sequences[:,-1]
y_train = to_categorical(y_train, num_classes=vocab_size)
seq_length = X_train.shape[1]
print(X_train[0])

                                                    #TRAIN THE MODEL
regressor = Sequential()
regressor.add(Embedding(vocab_size, 20, input_length=seq_length))
regressor.add(LSTM(units=512,return_sequences=True,input_shape=(seq_length,1)))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units=512,return_sequences=True))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units=512,return_sequences=True))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units=128,return_sequences=True))
regressor.add(Dropout(0.4))
regressor.add(LSTM(units=512))
regressor.add(Dropout(0.4))


regressor.add(Dense(512, activation='relu'))
regressor.add(Dense(vocab_size, activation='softmax'))
optim = optimizers.RMSprop(lr=0.001)
regressor.compile(loss='categorical_crossentropy', optimizer=optim, metrics=['accuracy'])
regressor.fit(X_train, y_train, batch_size=256, epochs=1)
                        #SAVE THE MODEL



regressor.save('regressor2.h5')
pickle.dump(tokenizer, open('tokenizer2.pkl', 'wb'))