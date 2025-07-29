msg = input("Your secert message:")
words = msg.split()
words.reverse()
sentence = []
vowel = ["a", "e", "i", "o", "u"]
if any(item in vowel for item in msg):
    for i in words:
        words = i
        if words[0].upper() == i[0]:
            sentence.append(words)
else:
    print("INVALID")

space = " "
print(f"{space.join(sentence).lower()}")