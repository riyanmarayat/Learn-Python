import pandas
import random

data = pandas.read_csv("data/french_words.csv")
print(len(data))
print(data)
data = data.to_dict(orient="records")
print(data)
word = random.choice(data)
print(word)
index_word = data.index(word)
print(index_word)
data.remove(data[index_word])
print(data)
data = pandas.DataFrame(data)
data.to_csv("data/new_french_words.csv", index=False)
print(len(pandas.read_csv("data/french_words.csv")))

