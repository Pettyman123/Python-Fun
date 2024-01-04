sentence = input("Enter the sentence: ")

def word_reversal():
    l=[]
    for letter in sentence:
        l.append(letter)
    print("The original string is:",l)
    print("The reverse string is:", l[::-1])
    sentence_1 = ''.join(l[::-1])
    print("The reversed word is:", sentence_1)

word_reversal()    