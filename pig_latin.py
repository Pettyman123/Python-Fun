
def Pig_latin():

    sentence = input("Enter the word: ")
    l = []
    for i in sentence:
        l.append(i)

    x = l.pop(0)#The first word in sentence is x and we are poping it from index 0

    l.append(x)#We are appendind x in index -1
    
    dict_vowels=['a','e','i','o','u']
    if x in dict_vowels:
        l.append('way')
    else:
        l.append('ay')
        

    strs = ''
    
    for words in l:
        strs += words
    print(strs)

Pig_latin()