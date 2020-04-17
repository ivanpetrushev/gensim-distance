import os
import gensim
import multiprocessing
# from tensorflow import keras
# from keras.preprocessing.text import Tokenizer

y = []
x = []

for root, dirs, files in os.walk('data/'):
    for file in files:
        with open('data/' + file) as fp:
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
model.train(x, total_examples=model.corpus_count, epochs=100)
print('Trained', model)

print('Vocab', list(model.wv.vocab))
print("Lookup: city")
print(model.wv.similar_by_word('city'))

word = ''
while word != 'quit':
    word = input('Lookup: ')
    try:
        print(model.wv.similar_by_word(word))
    except KeyError:
        print("Not found")
