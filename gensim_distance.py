import os
import gensim
import multiprocessing
from time import time
# from tensorflow import keras
# from keras.preprocessing.text import Tokenizer

DATA_DIR = 'data/' # general wiki articles about geography
# DATA_DIR = 'set-vazov-razkazi/' # Ivan Vazov works

y = []
x = []

for root, dirs, files in os.walk(DATA_DIR):
    for file in files:
        with open(DATA_DIR + file) as fp:
            text = fp.read().replace('\n', '')
            x.append(text)
            y.append(file)

print('Preprocessing: ')
x = [gensim.utils.simple_preprocess(text) for text in x]

# print('Tokenizing:')
# tk = Tokenizer()
# tk.fit_on_texts(x)
# print(tk)

# print('Padding:')
# x_test = keras.preprocessing.sequence.pad_sequences(tk.texts_to_sequences(x), maxlen=500)

print('Modeling:')
model = gensim.models.Word2Vec(min_count=1, window=5, size=300, workers=multiprocessing.cpu_count())
model.build_vocab(x)
print(model)
train_start = time()
model.train(x, total_examples=model.corpus_count, epochs=30)
train_duration = time() - train_start
print('Trained', model, 'in time: ', train_duration)

# print('Vocab', list(model.wv.vocab))
print("Lookup: city")
print(model.wv.similar_by_word('city'))

word = ''
while word != 'quit':
    word = input('Lookup: ')
    try:
        print(model.wv.similar_by_word(word))
    except KeyError:
        print("Not found")
