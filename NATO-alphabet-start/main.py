import pandas as pd

phenetics=pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict={row.letter: row.code for (index, row) in phenetics.iterrows()}
word = input ("Enter a word: ").upper()
result=[phonetic_dict[w] for w in word if w in phonetic_dict]
print(result)