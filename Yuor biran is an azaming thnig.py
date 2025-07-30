words = input("Enter a words: ")
word_ = words.split()
Word1 = list(word_[0])
Word2 = list(word_[1])
lenght = len(word_)
if len(Word1) == len(Word2):
    if all(item in Word1 for item in Word2):
        if Word1[0] == Word2[0] and Word1[-1] == Word2[-1]:
            print("SUPER ANAGRAM")
        else:
            print("Huh?")
    else:
        print("Huh?")
else:
    print("Huh?")