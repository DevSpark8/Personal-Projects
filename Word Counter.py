Word = input("Enter the word: ")
Array = [], dictionary = {}

while Word != "":
    words = Word.split()
    Array.extend(words)
    Word = input("Enter the word: ")

for i in Array:
    dictionary[i] = dictionary.get(i, 0) + 1

for i in sorted(dictionary):
    print(f"{i} {dictionary[i]}")