sentence = input("Enter the sentence: ")


def word_reversal():
    global l
    l=[]
    for letter in sentence.lower():
        l.append(letter)
    #print("The original string is:",l)
    counter()
    

#def counting_vowels(x):
#    counter = 0
#    for i in l:
#        if i ==x:
#            counter +=1
#    print("the count of",x,"is",counter) 
 
   
def counter():
    dict_vowels ={'a' : 0,
                  'e' : 0,
                  'i' : 0,
                  'o' : 0,
                  'u' : 0}
    
    for ke in l:
        if ke in dict_vowels:
            dict_vowels[ke] +=1
    
    print(dict_vowels)
         
   
word_reversal()    
#counter()